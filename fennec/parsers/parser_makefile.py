"""
Makefile parser

TODO:
  - Try compiling and report relinking errors
  - Remove cheater protection check
  - check targets for circular calls
  - check for wildcards (outside comments)

"""
import logging
import re
import time
from parser_base import ParserBase

class ParserMakefile(ParserBase):
    """
    Parser used to check Makefiles
    """

    accepted_filetypes = [ None ]

    accepted_filenames = [ 'Makefile' ]

    accepted_extensions = [ None ]

    rules = { }

    @classmethod
    def accepted(klass, filedata):
        return (klass._test_filename(filedata.file_name))

    def __init__(self, context, settings, node):
        super(ParserMakefile, self).__init__(context, settings, node)
        self.has = {
            'NAME_decl': False,
            'all_target': False,
            'NAME_target': False,
            'clean_target': False,
            'fclean_target': False,
            're_target': False,
            'wall_flag': False,
            'werror_flag': False,
            'wextra_flag': False,
            'phony_rule': False
        }
        self.found_author = None
        self.found_created_at = { 'user': None, 'time': None }
        self.found_updated_at = { 'user': None, 'time': None }

    def check_header(self):
        # check line by line for recipies
        i = 0
        lines_checked = 0
        for line in self.content_lines:
            i += 1
            if i == 1 or i == 11:
                regexp = re.compile("^# \*{76} #\n$")
                if regexp.search(line) == None:
                    self.log(logging.ERROR,
                        "doesn't have a properly formatted header", line= i)
                else:
                    lines_checked += 1
            if i == 2 or i == 10:
                regexp = re.compile("^# {78}#\n$")
                if regexp.search(line) == None:
                    self.log(logging.ERROR,
                        "doesn't have a properly formatted header", line= i)
                else:
                    lines_checked += 1
            if i == 3:
                regexp = re.compile("^# {57}:::      ::::::::    #\n$")
                if regexp.search(line) == None:
                    self.log(logging.ERROR,
                        "doesn't have a properly formatted header", line= i)
                else:
                    lines_checked += 1
            if i == 4:
                regexp = re.compile("^# {4}.{50} :\+: {6}:\+: {4}:\+: {4}#\n$")
                if regexp.search(line) == None:
                    self.log(logging.ERROR,
                        "doesn't have a properly formatted header", line= i)
                else:
                    lines_checked += 1
            if i == 5:
                regexp = re.compile("^# {53}\+:\+ \+:\+         \+:\+      #\n$")
                if regexp.search(line) == None:
                    self.log(logging.ERROR,
                        "doesn't have a properly formatted header", line= i)
                else:
                    lines_checked += 1
            if i == 6:
                regexp = re.compile("^# {4}By: ([a-z-]{3,8}) <([a-z-]{3,8})@student\.42\.fr> {10,20}\+#\+  \+:\+ {7}\+#\+ {9}#\n$")
                author_test = regexp.findall(line)
                if not author_test:
                    self.log(logging.ERROR,
                        "doesn't have a properly formatted author header", line= i)
                else:
                    xlogin1, xlogin2 = author_test[0]
                    if xlogin1 != xlogin2:
                        self.log(logging.ERROR,
                            "the login and email aren't the same", line= i)
                    else:
                        self.found_author = xlogin1
                        lines_checked += 1
            if i == 7:
                regexp = re.compile("^# {49}\+#\+#\+#\+#\+#\+   \+#\+ {12}#\n$")
                if regexp.search(line) == None:
                    self.log(logging.ERROR,
                        "doesn't have a properly formatted header", line= i)
                else:
                    lines_checked += 1
            if i == 8:
                regexp = re.compile("^# {4}Created: (\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}) by ([a-z-]{3,8}) {10,15}#\+# {4}#\+# {14}#\n$")
                creator_test = regexp.findall(line)
                if not creator_test:
                    self.log(logging.ERROR,
                        "doesn't have a properly formatted created at header", line= i)
                else:
                    time_creation, xlogin = creator_test[0]
                    self.found_created_at['time'] = time_creation
                    self.found_created_at['user'] = xlogin
                    lines_checked += 1
            if i == 9:
                regexp = re.compile("^# {4}Updated: (\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}) by ([a-z-]{3,8}) {9,14}###   ########\.fr {8}#\n$")
                updator_test = regexp.findall(line)
                if not updator_test:
                    self.log(logging.ERROR,
                        "doesn't have a properly formatted created at header", line= i)
                else:
                    time_creation, xlogin = updator_test[0]
                    self.found_updated_at['time'] = time_creation
                    self.found_updated_at['user'] = xlogin
                    lines_checked += 1
            if i > 12:
                break
        if lines_checked != 11:
            self.log(logging.ERROR, "doesn't have a properly formatted header")


    def check_base_rules(self):
        # check if the file has any recipies
        regexp = re.compile("^.*\n([\$\(\)a-zA-Z0-9/\.%]*):.*$", re.MULTILINE)
        result = regexp.findall(self.content_full)
        if result == None:
            self.log(logging.ERROR, "doesn't have ANY target.")
            return
        # check if the "all" target is the first
        if result[0] != 'all' and result[0] != '.PHONY':
            self.log(logging.ERROR,
            "has \"{0}\" as the default target instead of \"all\".".format(result[0]))
        # check line by line (to show line) for targets
        i = 0
        for line in self.content_lines:
            i += 1
            if line.startswith('#') or line == '\n':
                continue
            regexp = re.compile("^NAME[ \t]+=.*$")
            if regexp.search(line) != None:
                self.has['NAME_decl'] = True
            # Check targets
            regexp = re.compile("^all:.*$")
            if regexp.search(line) != None:
                if self.has['all_target'] == False:
                    self.has['all_target'] = True
                else:
                    self.log(logging.ERROR,
                             "has more than one \"all\" target.", line = i)
            regexp = re.compile("^\$\(NAME\):.*$")
            if regexp.search(line) != None:
                if self.has['NAME_target'] == False:
                    self.has['NAME_target'] = True
                else:
                    self.log(logging.ERROR,
                             "has more than one \"NAME\" target.", line = i)
            regexp = re.compile("^clean:.*$")
            if regexp.search(line) != None:
                if self.has['clean_target'] == False:
                    self.has['clean_target'] = True
                else:
                    self.log(logging.ERROR,
                             "has more than one \"clean\" target.", line = i)
            regexp = re.compile("^fclean:.*$")
            if regexp.search(line) != None:
                if self.has['fclean_target'] == False:
                    self.has['fclean_target'] = True
                else:
                    self.log(logging.ERROR,
                             "has more than one \"fclean\" target.", line = i)
            regexp = re.compile("^re:.*$")
            if regexp.search(line) != None:
                if self.has['re_target'] == False:
                    self.has['re_target'] = True
                else:
                    self.log(logging.ERROR,
                             "has more than one \"re\" target.", line = i)
        if not self.has['all_target']:
            self.log(logging.ERROR, "misses a \"all\" target")
        if not self.has['NAME_target']:
            self.log(logging.ERROR, "misses a \"NAME\" target")
        if not self.has['clean_target']:
            self.log(logging.ERROR, "misses a \"clean\" target")
        if not self.has['fclean_target']:
            self.log(logging.ERROR, "misses a \"fclean\" target")
        if not self.has['re_target']:
            self.log(logging.ERROR, "misses a \"re\" target")
        # Check if every target has the minimal dependencies
        # (iterate again, not very optimized)
        i = 0
        for line in self.content_lines:
            i += 1
            if self.has['all_target']:
                regexp = re.compile("^all:.*$")
                if regexp.search(line) != None:
                    regexp = re.compile("^all:.*[ \t]+(\$\(NAME\)[ \t\n]+).*$")
                    if regexp.search(line) == None:
                        self.log(logging.ERROR,
                        "misses \"$(NAME)\" dependency for \"all\" target", line = i)
            if self.has['fclean_target']:
                regexp = re.compile("^fclean:.*$")
                if regexp.search(line) != None:
                    regexp = re.compile("^fclean:.*[ \t]+(clean)[ \t\n]+.*$")
                    if regexp.search(line) == None:
                        self.log(logging.ERROR,
                        "misses \"clean\" dependency for \"fclean\" target", line = i)
            if self.has['re_target']:
                regexp = re.compile("^re:.*$")
                if regexp.search(line) != None:
                    regexp = re.compile("^re:.*[ \t]+(fclean)[ \t\n]+.*$")
                    if regexp.search(line) == None:
                        self.log(logging.ERROR,
                        "misses \"fclean\" dependency for \"re\" target", line = i)
                    regexp = re.compile("^re:.*[ \t]+(all)[ \t\n]+.*$")
                    if regexp.search(line) == None:
                        self.log(logging.ERROR,
                        "misses \"all\" dependency for \"re\" target", line = i)

    def check_use_of_Wflags(self):
        i = 0
        for line in self.content_lines:
            i += 1
            if line.startswith('#') or line == '\n':
                continue
            regexp = re.compile("^.*(-Wall).*$")
            if regexp.search(line) != None:
                self.has['wall_flag'] = True
            regexp = re.compile("^.*(-Wextra).*$")
            if regexp.search(line) != None:
                self.has['wextra_flag'] = True
            regexp = re.compile("^.*(-Werror).*$")
            if regexp.search(line) != None:
                self.has['werror_flag'] = True
        if self.has['wall_flag'] == False or \
            self.has['werror_flag'] == False or \
            self.has['wextra_flag'] == False:
            self.log(logging.ERROR,
                        "doesn't have all the compilation flags: -Wall -Wextra -Werror")

    def check_rule_dotPHONY(self):
        i = 0
        for line in self.content_lines:
            i += 1
            if line.startswith('#') or line == '\n':
                continue
            regexp = re.compile("^\.PHONY:.*$")
            if regexp.search(line) != None:
                if self.has['phony_rule'] == False:
                    self.has['phony_rule'] = True
                else:
                    self.log(logging.ERROR,
                             "has more than one \".PHONY\" target.", line = i)
        # Check if .PHONY has the minimal "dependencies": all clean fclean re
        i = 0
        for line in self.content_lines:
            i += 1
            if self.has['phony_rule']:
                regexp = re.compile("^\.PHONY:.*$")
                if regexp.search(line) != None:
                    regexp = re.compile("^\.PHONY:.*[ \t]+(all)[ \t\n]+.*$")
                    if regexp.search(line) == None:
                        self.log(logging.ERROR,
                        "misses \"all\" rule in \".PHONY\" target", line = i)
                    regexp = re.compile("^\.PHONY:.*[ \t]+(clean)[ \t\n]+.*$")
                    if regexp.search(line) == None:
                        self.log(logging.ERROR,
                        "misses \"clean\" rule in \".PHONY\" target", line = i)
                    regexp = re.compile("^\.PHONY:.*[ \t]+(fclean)[ \t\n]+.*$")
                    if regexp.search(line) == None:
                        self.log(logging.ERROR,
                        "misses \"fclean\" rule in \".PHONY\" target", line = i)
                    regexp = re.compile("^\.PHONY:.*[ \t]+(re)[ \t\n]+.*$")
                    if regexp.search(line) == None:
                        self.log(logging.ERROR,
                        "misses \"re\" rule in \".PHONY\" target", line = i)

    def check_wildcards(self):
        i = 0
        for line in self.content_lines:
            i += 1
            if line.startswith('#') or line == '\n':
                continue
            if '*' in line:
                self.log(logging.ERROR,
                    "contains usage of a forbidden $(wildcard (*)).", line = i)
            elif '$(wildcard' in line:
                self.log(logging.ERROR,
                    "contains usage of a forbidden $(wildcard) function.", line = i)

    def post_process(self):
        if self.found_author != self.found_created_at['user']:
            self.log(logging.WARNING,
                "has a different author({0}) than creator({1}). Suspicious !".format(
                self.found_author, self.found_created_at['user']))
        created_time = time.strptime(self.found_created_at['time'], "%Y/%m/%d %H:%M:%S")
        updated_time = time.strptime(self.found_updated_at['time'], "%Y/%m/%d %H:%M:%S")
        if updated_time < created_time:
            self.log(logging.WARNING,
                    "has an updated timestamp BEFORE the created timestamp. Suspicious !")
        if self.context['author'] != None:
            # Check that all the logins found in the Makefile correspond to the author file
            if self.found_author not in self.context['author']['user_names']:
                self.log(logging.WARNING,
                    "has an author that is not in the author file. VERY SUSPICIOUS !")
            if self.found_created_at['user'] not in self.context['author']['user_names']:
                self.log(logging.WARNING,
                    "has a creator that is not in the author file. VERY SUSPICIOUS !")
            if self.found_updated_at['user'] not in self.context['author']['user_names']:
                self.log(logging.WARNING,
                    "has a updator that is not in the author file. VERY SUSPICIOUS !")
        makefile_info = {
            'author': self.found_author,
            'created_data': { 'user': self.found_created_at['user'], 'time': self.found_created_at['time'] },
            'updated_data': { 'user': self.found_updated_at['user'], 'time': self.found_updated_at['time'] }
        }
        self.context['makefile'].append(makefile_info)

    rules = { 'header'   : check_header,
              'base_rules': check_base_rules,
              'use_flags': check_use_of_Wflags,
              'phony_rule': check_rule_dotPHONY,
              'wildcards': check_wildcards
            }


name = 'parser_makefile'
parser = ParserMakefile
