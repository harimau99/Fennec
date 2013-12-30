
import logging
import re
from parser_base import ParserBase

class ParserMakefile(ParserBase):
    """
    Parser used to check Makefiles
    """

    accepted_filetypes = [ None ]

    accepted_filenames = [ 'Makefile' ]

    rules = { }

    @classmethod
    def accepted(klass, filedata):
        return (klass._test_filename(filedata.file_name))

    def __init__(self, context, settings, node):
        super(ParserMakefile, self).__init__(context, settings, node)
        self.has = {
            'NAME_decl': False,
            'all_recipe': False,
            'NAME_recipe': False,
            'clean_recipe': False,
            'fclean_recipe': False,
            're_recipe': False,
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
                regexp = re.compile("^# {4}By: ([a-z- ]{3,8}) <([a-z- ]{3,8})@student\.42\.fr> {10,20}\+#\+  \+:\+ {7}\+#\+ {9}#\n$")
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
                regexp = re.compile("^# {4}Created: (\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}) by ([a-z- ]{3,8}) {10,15}#\+# {4}#\+# {14}#\n$")
                creator_test = regexp.findall(line)
                if not author_test:
                    self.log(logging.ERROR,
                        "doesn't have a properly formatted created at header", line= i)
                else:
                    time_creation, xlogin = author_test[0]
                    self.found_created_at['time'] = time_creation
                    self.found_created_at['user'] = xlogin
                    lines_checked += 1
            if i == 9:
                regexp = re.compile("^# {4}Updated: (\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}) by ([a-z- ]{3,8}) {9,14}###   ########\.fr {8}#\n$")
                creator_test = regexp.findall(line)
                if not author_test:
                    self.log(logging.ERROR,
                        "doesn't have a properly formatted created at header", line= i)
                else:
                    time_creation, xlogin = author_test[0]
                    self.found_updated_at['time'] = time_creation
                    self.found_updated_at['user'] = xlogin
                    lines_checked += 1
            if i > 12:
                break
        if lines_checked != 11:
            self.log(logging.ERROR, "doesn't have a properly formatted header")


    def check_base_rules(self):
        # check if the file has any recipies
        regexp = re.compile("^.*\n([a-zA-Z\$]*):.*$", re.MULTILINE)
        result = regexp.search(self.content_full)
        if result == None:
            self.log(logging.ERROR, "doesn't have ANY recipe.")
            return
        # check line by line for recipies
        i = 0
        for line in self.content_lines:
            i += 1
            if line.startswith('#') or line == '\n':
                continue
            regexp = re.compile("^NAME[ \t]+=.*$")
            if regexp.search(line) != None:
                self.has['NAME_decl'] = True
            # Check recipes
            regexp = re.compile("^all:.*$")
            if regexp.search(line) != None:
                if self.has['all_recipe'] == False:
                    # Check if the "all" recipe is the first one set. This
                    # check is not very optimal because it doesn't detect
                    # un-official recipes that could be added prior to all
                    # -- TODO -- Make a better detection
                    if  self.has['NAME_recipe'] or self.has['clean_recipe'] or \
                        self.has['fclean_recipe'] or self.has['re_recipe']:
                        self.log(logging.ERROR,
                            "doesn't have the \"all\" recipe as first recipe")
                    self.has['all_recipe'] = True
                else:
                    self.log(logging.ERROR,
                             "has more than one \"all\" recipe.", line = i)
            regexp = re.compile("^\$\(NAME\):.*$")
            if regexp.search(line) != None:
                if self.has['NAME_recipe'] == False:
                    self.has['NAME_recipe'] = True
                else:
                    self.log(logging.ERROR,
                             "has more than one \"NAME\" recipe.", line = i)
            regexp = re.compile("^clean:.*$")
            if regexp.search(line) != None:
                if self.has['clean_recipe'] == False:
                    self.has['clean_recipe'] = True
                else:
                    self.log(logging.ERROR,
                             "has more than one \"clean\" recipe.", line = i)
            regexp = re.compile("^fclean:.*$")
            if regexp.search(line) != None:
                if self.has['fclean_recipe'] == False:
                    self.has['fclean_recipe'] = True
                else:
                    self.log(logging.ERROR,
                             "has more than one \"fclean\" recipe.", line = i)
            regexp = re.compile("^re:.*$")
            if regexp.search(line) != None:
                if self.has['re_recipe'] == False:
                    self.has['re_recipe'] = True
                else:
                    self.log(logging.ERROR,
                             "has more than one \"re\" recipe.", line = i)
        if  not self.has['all_recipe']:
            self.log(logging.ERROR, "misses a \"all\" recipe")
        if  not self.has['NAME_recipe']:
            self.log(logging.ERROR, "misses a \"NAME\" recipe")
        if  not self.has['clean_recipe']:
            self.log(logging.ERROR, "misses a \"clean\" recipe")
        if  not self.has['fclean_recipe']:
            self.log(logging.ERROR, "misses a \"fclean\" recipe")
        if  not self.has['re_recipe']:
            self.log(logging.ERROR, "misses a \"re\" recipe")
        # Check if every recipe has the minimal dependencies
        # (iterate again, not very optimized)
        i = 0
        for line in self.content_lines:
            i += 1
            if self.has['all_recipe']:
                regexp = re.compile("^all:.*$")
                if regexp.search(line) != None:
                    regexp = re.compile("^all:.*[ \t]+(\$\(NAME\)[ \t\n]+).*$")
                    if regexp.search(line) == None:
                        self.log(logging.ERROR,
                        "misses \"$(NAME)\" dependency for \"all\" recipe", line = i)
            if self.has['fclean_recipe']:
                regexp = re.compile("^fclean:.*$")
                if regexp.search(line) != None:
                    regexp = re.compile("^fclean:.*[ \t]+(clean)[ \t\n]+.*$")
                    if regexp.search(line) == None:
                        self.log(logging.ERROR,
                        "misses \"clean\" dependency for \"fclean\" recipe", line = i)
            if self.has['re_recipe']:
                regexp = re.compile("^re:.*$")
                if regexp.search(line) != None:
                    regexp = re.compile("^re:.*[ \t]+(fclean)[ \t\n]+.*$")
                    if regexp.search(line) == None:
                        self.log(logging.ERROR,
                        "misses \"fclean\" dependency for \"re\" recipe", line = i)
                    regexp = re.compile("^re:.*[ \t]+(all)[ \t\n]+.*$")
                    if regexp.search(line) == None:
                        self.log(logging.ERROR,
                        "misses \"all\" dependency for \"re\" recipe", line = i)


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

    def post_process(self):
        # check if author is the same as in other container files (mainly author)
        # if different = not ok ? Maybe project with muti-authors ?\
        # check that updated at is after created at
        # save author into container for futher checks
        # -- TODO --
        #self.found_author = None
        #self.found_created_at = { 'user': None, 'time': None }
        #self.found_updated_at = { 'user': None, 'time': None }
        #AFTER HERE COPIED FROM AUTHOR PARSER
        # if self.context['author'] != None:
        #     self.log(logging.CRITICAL, "is another author file. "
        #                                 "There should be only one !")
        # elif (len(self.found_xlogins) != len(set(self.found_xlogins))) == True:
        #     self.log(logging.CRITICAL, "has duplicate authors. "
        #                                 " Check your author files !")
        # else:
        #     self.context['author'] = {
        #         'node': self.node,
        #         'node_path': self.node.path,
        #         'user_names': self.found_xlogins
        #     }
        pass

    rules = { 'header'   : check_header,
              'base_rules': check_base_rules,
              'use_flags': check_use_of_Wflags,
              'phony_rule': check_rule_dotPHONY
            }


name = 'parser_makefile'
parser = ParserMakefile
