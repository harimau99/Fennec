"""
C Source files parser

TODO:
  - To add

"""
import logging
import re
from parser_c_lang import ParserCLang

class ParserCSource(ParserCLang):
    """
    Parser used to check C source files
    """

    accepted_filetypes = [ 'text/x-c' ]

    accepted_filenames = [ None ]

    accepted_extensions = [ '.c' ]

    rules = [ ]

    @classmethod
    def accepted(klass, filedata):
        return (klass._test_fileextension(filedata.extension))

    def __init__(self, context, settings, node):
        super(ParserCSource, self).__init__(context, settings, node)
        super(ParserCSource, self)._remove_comments()

    def check_forbidden_keywords(self):
        i = 0
        for line in self.content_lines:
            i += 1
            regexp = re.compile("^[^\"|/*]*[ |\t]+(case|do|for|goto|switch)[ |\t|:|\(|{|\n]+.*$")
            result = regexp.findall(line)
            if result:
                self.log(logging.ERROR, "has a forbidden keyword.", line = i)


    def check_spaces_around_operators(self):
        i = 0
        lines_checked = 0
        for line in self.content_lines:
            i += 1
            if '&&' in line:
                pos = line.find('&&')
                subline = list(line)
                if subline[pos - 1] in "\t " \
                and subline[pos + 2] in " ":
                    pass
                else:
                    self.log(logging.ERROR, "has no spaces around && operator.", line = i)
            if '||' in line:
                pos = line.find('||')
                subline = list(line)
                if subline[pos - 1] in "\t " \
                and subline[pos + 2] in " ":
                    pass
                else:
                    self.log(logging.ERROR, "has no spaces around || operator.", line = i)
            if '==' in line:
                pos = line.find('==')
                subline = list(line)
                if subline[pos - 1] in "\t " \
                and subline[pos + 2] in " ":
                    pass
                else:
                    self.log(logging.ERROR, "has no spaces around == operator.", line = i)
            if '!=' in line:
                pos = line.find('!=')
                subline = list(line)
                if subline[pos - 1] in "\t " \
                and subline[pos + 2] in " ":
                    pass
                else:
                    self.log(logging.ERROR, "has no spaces around != operator.", line = i)
            if '>=' in line:
                pos = line.find('>=')
                subline = list(line)
                if subline[pos - 1] in "\t >" \
                and subline[pos + 2] in " ":
                    pass
                else:
                    self.log(logging.ERROR, "has no spaces around >= operator.", line = i)
            if '<=' in line:
                pos = line.find('<=')
                subline = list(line)
                if subline[pos - 1] in "\t <" \
                and subline[pos + 2] in " ":
                    pass
                else:
                    self.log(logging.ERROR, "has no spaces around <= operator.", line = i)
            if '<<' in line:
                pos = line.find('<<')
                subline = list(line)
                if subline[pos - 1] in "\t <" \
                and subline[pos + 2] in " =":
                    pass
                else:
                    self.log(logging.ERROR, "has no spaces around << operator.", line = i)
            if '>>' in line:
                pos = line.find('>>')
                subline = list(line)
                if subline[pos - 1] in "\t " \
                and subline[pos + 2] in " =":
                    pass
                else:
                    self.log(logging.ERROR, "has no spaces around >> operator.", line = i)
            if '<<=' in line:
                pos = line.find('<<=')
                subline = list(line)
                if subline[pos - 1] in "\t " \
                and subline[pos + 3] in " ":
                    pass
                else:
                    self.log(logging.ERROR, "has no spaces around <<= operator.", line = i)
            if '>>=' in line:
                pos = line.find('>>=')
                subline = list(line)
                if subline[pos - 1] in "\t " \
                and subline[pos + 3] in " ":
                    pass
                else:
                    self.log(logging.ERROR, "has no spaces around >> operator.", line = i)
            if '<' in line and not line.startswith('#'):
                pos = line.find('<')
                subline = list(line)
                if subline[pos - 1] in "\t " \
                and subline[pos + 1] in " =<":
                    pass
                else:
                    self.log(logging.ERROR, "has no spaces around < operator.", line = i)
            if '>' in line and not line.startswith('#'):
                pos = line.find('>')
                subline = list(line)
                if subline[pos - 1] in "\t " \
                and subline[pos + 1] in " =>":
                    pass
                elif subline[pos - 1] == '-':
                    pass
                else:
                    self.log(logging.ERROR, "has no spaces around > operator.", line = i)

    def check_spaces_after_keywords(self):
        i = 0
        for line in self.content_lines:
            i += 1
            regexp = re.compile("[ |\t|\(|\)|{|}](if|else|return|while)[^ |\n]")
            result = regexp.findall(line)
            if result:
                self.log(logging.ERROR, "has no spaces after keyword (if, else, return, while).", line = i)

    def check_no_spaces_unary_operators(self):
        i = 0
        for line in self.content_lines:
            i += 1
            if '++' in line:
                pos = line.find('++')
                subline = list(line)
                if subline[pos - 1] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_" \
                and subline[pos + 2] in " \t\n;,[]()!":
                    pass
                elif subline[pos - 1] in " \t\n;,[]()*!" \
                and subline[pos + 2] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_*":
                    pass
                else:
                    self.log(logging.ERROR, "has invalid format for ++ operator (no spaces, ...).", line = i)
            if '--' in line:
                pos = line.find('--')
                subline = list(line)
                if subline[pos - 1] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_" \
                and subline[pos + 2] in " \t\n;,[]()!":
                    pass
                elif subline[pos - 1] in " \t\n;,[]()*!" \
                and subline[pos + 2] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_*":
                    pass
                else:
                    self.log(logging.ERROR, "has invalid format for -- operator (no spaces, ...).", line = i)

    def check_max_function_length(self):
        i = 0;
        count_data = list()
        for line in self.content_lines:
            i += 1
            res = line.count('{')
            if res > 0:
                for x in range(res):
                    count_data.append(i)
            res = line.count('}')
            if res > 0:
                for y in range(res):
                    last = count_data.pop()
                total_len = i - last
                if total_len > 26:
                    self.log(logging.ERROR, "has a block of more than 25 lines.", line = i)
                elif total_len == 26:
                    self.log(logging.INFO, "has a block of exactly 25 lines.", line = i)

    def check_function_spacing(self):
        pass

    def check_max_functions_per_file(self):
        pass

    def check_var_initializations(self):
        """
        One var per line with type
        A newline after var initializations
        """
        pass

    def post_process(self):
        """Save data into context, perform some meta-checks"""
        pass

    rules = [
                ('forbidden_keywords', check_forbidden_keywords),
                ('spaces_around_operators', check_spaces_around_operators),
                ('spaces_after_keywords', check_spaces_after_keywords),
                ('no_spaces_unary_operators', check_no_spaces_unary_operators),
                ('max_function_length', check_max_function_length),
                ('function_spacing', check_function_spacing),
                ('max_functions_per_file', check_max_functions_per_file),
                ('var_initializations', check_var_initializations)
            ]


name = 'parser_c_source'
parser = ParserCSource
