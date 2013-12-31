"""
C language parser (headers and source)

TODO:
  - To add

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

    rules = { }

    @classmethod
    def accepted(klass, filedata):
        return (klass._test_fileextension(filedata.extension))

    def __init__(self, context, settings, node):
        super(ParserCLang, self).__init__(context, settings, node)

    def check_header(self):
        pass

    def check_preprocessor_indentation(self):
        pass

    def check_commas(self):
        pass

    def check_c_comments(self):
        pass

    def check_cpp_comments(self):
        pass

    def check_function_prototypes(self):
        pass

    def check_capital_letters(self):
        pass

    def check_bracket_matching(self):
        pass

    def check_multi_includes(self):
        """Check that there are not multiple useless includes"""
        pass

    def check_system_includes(self):
        pass

    def post_process(self):
        """Save data into context, perform some meta-checks"""
        pass

    rules = {
                'header'   : check_header,
                'preprocessor_indentation': check_preprocessor_indentation,
                'commas': check_commas,
                'comments': check_c_comments,
                'cpp_comments': check_cpp_comments,
                'function prototypes': check_function_prototypes,
                'capital_letters': check_capital_letters,
                'bracket_matching': check_bracket_matching,
                'multi_includes': check_multi_includes,
                'sys_includes': check_system_includes
            }

name = 'parser_c_lang'
parser = ParserCLang
