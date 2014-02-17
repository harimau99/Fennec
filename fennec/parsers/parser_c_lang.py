"""
C language parser (headers AND source)

TODO:
  - Once all comments and headers hav been checked, remove them from
    lines and content to prevent false positives

"""
import logging
import re
from parser_base import ParserBase

class ParserCLang(ParserBase):
    """
    Parser used to check C language files
    """

    accepted_filetypes = [ 'text/x-c' ]

    accepted_filenames = [ None ]

    accepted_extensions = [ '.c', '.h' ]

    rules = [ ]

    @classmethod
    def accepted(klass, filedata):
        return (klass._test_fileextension(filedata.extension))

    def __init__(self, context, settings, node):
        super(ParserCLang, self).__init__(context, settings, node)
        self.filename = None
        self.found_author = None
        self.found_created_at = { 'user': None, 'time': None }
        self.found_updated_at = { 'user': None, 'time': None }
        self._remove_chars()

    def check_header(self):
        # check line by line for recipies
        i = 0
        lines_checked = 0
        for line in self.content_lines:
            i += 1
            if i == 1 or i == 11:
                regexp = re.compile("^/\* \*{74} \*/\n$")
                if regexp.search(line) == None:
                    self.log(logging.ERROR,
                        "doesn't have a properly formatted header", line= i)
                else:
                    lines_checked += 1
            if i == 2 or i == 10:
                regexp = re.compile("^/\* {76}\*/\n$")
                if regexp.search(line) == None:
                    self.log(logging.ERROR,
                        "doesn't have a properly formatted header", line= i)
                else:
                    lines_checked += 1
            if i == 3:
                regexp = re.compile("^/\* {56}:::      ::::::::   \*/\n$")
                if regexp.search(line) == None:
                    self.log(logging.ERROR,
                        "doesn't have a properly formatted header", line= i)
                else:
                    lines_checked += 1
            if i == 4:
                regexp = re.compile("^/\* {3}(.{50}) :\+: {6}:\+: {4}:\+: {3}\*/\n$")
                if regexp.search(line) == None:
                    self.log(logging.ERROR,
                        "doesn't have a properly formatted header", line= i)
                else:
                    self.filename = regexp.findall(line)[0]
                    self.filename = self.filename.strip()
                    lines_checked += 1
            if i == 5:
                regexp = re.compile("^/\* {52}\+:\+ \+:\+ {9}\+:\+     \*/\n$")
                if regexp.search(line) == None:
                    self.log(logging.ERROR,
                        "doesn't have a properly formatted header", line= i)
                else:
                    lines_checked += 1
            if i == 6:
                regexp = re.compile("^/\* {3}By: ([a-z-]{3,8}) <([a-z-]{3,8})@student\.42\.fr> {10,20}\+#\+  \+:\+ {7}\+#\+ {8}\*/\n$")
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
                regexp = re.compile("^/\* {48}\+#\+#\+#\+#\+#\+   \+#\+ {11}\*/\n$")
                if regexp.search(line) == None:
                    self.log(logging.ERROR,
                        "doesn't have a properly formatted header", line= i)
                else:
                    lines_checked += 1
            if i == 8:
                regexp = re.compile("^/\* {3}Created: (\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}) by ([a-z-]{3,8}) {10,15}#\+# {4}#\+# {13}\*/\n$")
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
                regexp = re.compile("^/\* {3}Updated: (\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}) by ([a-z-]{3,8}) {9,14}###   ########\.fr {7}\*/\n$")
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

    def check_preprocessor_indentation(self):
        pass

    def check_commas(self):
        i = 0
        for line in self.content_lines:
            i += 1
            regexp = re.compile("^.*(,[^ |\n|\\\n]).*$")
            if regexp.search(line) != None:
                self.log(logging.ERROR,
                    "has a missing space after comma.", line= i)

    def check_semi_columns(self):
        i = 0
        for line in self.content_lines:
            i += 1
            regexp = re.compile("^.*(;[^ |\n]).*$")
            if regexp.search(line) != None:
                self.log(logging.ERROR, "has a missing space after semi column.", line= i)

    def check_c_comments(self):
        self._remove_comments()
        # now check for C comments in correct places (headers and before functions only)

    def check_cpp_comments(self):
        i = 0
        for line in self.content_lines:
            i += 1
            if '//' in line:
                self.log(logging.ERROR, "has a C++ comment (//).", line= i)

    def check_function_prototypes(self):
        # check that function_name contains type and * next to name
        # check that function_args contains max 4 vars
        # check that function_type is new function (after: { ) or prototype(after: ;)
        #regexp = re.compile("^^([a-z_]+)([ |\t]+)(\**[a-z0-9_]+)\(([a-z_]+( \**[a-z0-9_]+))?(, ?[a-z_]+( \**[a-z0-9_]+))?(, ?[a-z_]+( \**[a-z0-9_])+)?(, ?[a-z_]+( \**[a-z0-9_])+)?\);?\n$")
        #if regexp.findall(line) == None:
        pass

    def check_capital_letters(self):
        pass

    def check_bracket_matching(self):
        curly_braces_open = self.content_full.count('{')
        curly_braces_close = self.content_full.count('}')
        if curly_braces_open != curly_braces_close:
            self.log(logging.ERROR, "has a missing curly brace { or }.")
        parenthesis_open = self.content_full.count('(')
        parenthesis_close = self.content_full.count(')')
        if parenthesis_open != parenthesis_close:
            self.log(logging.ERROR, "has a missing parenthesis ( or ).")

    def check_curly_braces_alone_on_line(self):
        pass

    def check_multi_includes(self):
        """Check that there are not multiple useless includes"""
        pass

    def check_system_includes(self):
        pass

    def check_mixed_spaces_and_tabs(self):
        i = 0
        for line in self.content_lines:
            i += 1
            regexp = re.compile("^.*(\t | \t).*$")
            if regexp.search(line) != None:
                self.log(logging.ERROR, "has mixed spaces and tabs.", line= i)

    def _remove_chars(self):
        is_string = False
        is_char = False
        skip_next = False
        for lineidx, line in enumerate(self.content_lines):
            if '\'' or '"' in line:
                newline = list(line)
                for idx, char in enumerate(line):
                    if skip_next == True:
                        skip_next = False
                        newline[idx] = '_'
                        continue
                    if char == '\\':
                        skip_next = True
                        newline[idx] = '_'
                        continue
                    if not is_char and char == '"':
                        is_string = not is_string
                        continue
                    if not is_string and char == '\'':
                        is_char = not is_char
                        continue
                    if is_char or is_string:
                        newline[idx] = '_'
                self.content_lines[lineidx] = ''.join(newline)
        is_string = False
        is_char = False
        skip_next = False
        newfullcontent = list(self.content_full)
        for idx, char in enumerate(self.content_full):
            if skip_next == True:
                skip_next = False
                newfullcontent[idx] = '_'
                continue
            if char == '\\':
                skip_next = True
                newfullcontent[idx] = '_'
                continue
            if not is_char and char == '"':
                is_string = not is_string
                continue
            if not is_string and char == '\'':
                is_char = not is_char
                continue
            if is_char or is_string:
                newfullcontent[idx] = '_'
        self.content_full = ''.join(newfullcontent)

    def _remove_comments(self):
        is_comment = False
        for lineidx, line in enumerate(self.content_lines):
            if '/*' or '*/' in line:
                newline = list(line)
                for idx, char in enumerate(line):
                    if char == '/' and line[idx + 1] == '*':
                        is_comment = True
                        continue
                    if char == '*' and line[idx + 1] == '/':
                        is_comment = False
                        newline[idx] = '_'
                        continue
                    if is_comment:
                        newline[idx] = '_'
                self.content_lines[lineidx] = ''.join(newline)
        is_comment = False
        seen_star = False
        seen_slash = False
        newfullcontent = list(self.content_full)
        for idx, char in enumerate(self.content_full):
            if char == '/' and newfullcontent[idx + 1] == '*':
                is_comment = True
                continue
            if char == '*' and newfullcontent[idx + 1] == '/':
                is_comment = False
                newfullcontent[idx] = '_'
                continue
            if is_comment:
                newfullcontent[idx] = '_'
        self.content_full = ''.join(newfullcontent)

    def post_process(self):
        """Save data into context, perform some meta-checks"""
        pass

    rules = [
                ('header', check_header),
                ('comments', check_c_comments), #changes comments, should be only after header check
                ('preprocessor_indentation', check_preprocessor_indentation),
                ('commas', check_commas),
                ('semi_columns', check_semi_columns),
                ('cpp_comments', check_cpp_comments),
                ('function prototypes', check_function_prototypes),
                ('capital_letters', check_capital_letters),
                ('bracket_matching', check_bracket_matching),
                ('curly_braces_alone_on_line', check_curly_braces_alone_on_line),
                ('multi_includes', check_multi_includes),
                ('sys_includes', check_system_includes),
                ('mixed_space_tabs', check_mixed_spaces_and_tabs)
            ]

name = 'parser_c_lang'
parser = ParserCLang
