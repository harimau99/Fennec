"""
C Source files parser

TODO:
  - To add

"""
import logging
import re
from parser_base import ParserBase

class ParserCSource(ParserBase):
    """
    Parser used to check C source files
    """

    accepted_filetypes = [ 'text/x-c' ]

    accepted_filenames = [ None ]

    accepted_extensions = [ '.c' ]

    rules = { }

    @classmethod
    def accepted(klass, filedata):
        return (klass._test_fileextension(filedata.extension))

    def __init__(self, context, settings, node):
        super(ParserCSource, self).__init__(context, settings, node)

    def check_forbidden_keywords(self):
        i = 0
        lines_checked = 0
        for line in self.content_lines:
            i += 1
            if i < 11:
                continue
            # Be careful, if the line contains ONE double-quote or and /* => the whole line is skipped
            regexp = re.compile("^[^\"|/*]*[ |\t]+(case|do|for|goto|switch)[ |\t|:|\(|{|\n]+.*$")
            result = regexp.findall(line)
            if result:
                self.log(logging.ERROR, "has a forbidden keyword.", line = i)


    def check_spaces_around_operators(self):
        # i = 0
        # lines_checked = 0
        # for line in self.content_lines:
        #     i += 1
        #     if i < 11:
        #         continue
        #     regexp = re.compile("[^ |\t|+]\+[^ |\n|+|=]")
        #     result = regexp.findall(line)
        #     if result:
        #         self.log(logging.ERROR, "has no spaces around + operator.", line = i)
        pass

    def check_spaces_after_keywords(self):
        i = 0
        lines_checked = 0
        for line in self.content_lines:
            i += 1
            if i < 11:
                continue
            regexp = re.compile("[ |\t|\(|\)|{|}](if|else|return|while)[^ |\n]")
            result = regexp.findall(line)
            if result:
                self.log(logging.ERROR, "has no spaces after keyword (if, else, return, while).", line = i)

    def check_no_spaces_unary_operators(self):
        pass

    def check_max_function_length(self):
        pass

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

    rules = {
                'forbidden_keywords': check_forbidden_keywords,
                'spaces_around_operators': check_spaces_around_operators,
                'spaces_after_keywords': check_spaces_after_keywords,
                'no_spaces_unary_operators': check_no_spaces_unary_operators,
                'max_function_length': check_max_function_length,
                'function_spacing': check_function_spacing,
                'max_functions_per_file': check_max_functions_per_file,
                'var_initializations': check_var_initializations,
            }


name = 'parser_c_source'
parser = ParserCSource
