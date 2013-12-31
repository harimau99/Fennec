"""
C headerfile parser

TODO:
  - To add

"""
import logging
import re
from parser_base import ParserBase

class ParserCHeaders(ParserBase):
    """
    Parser used to check C header files
    """

    accepted_filetypes = [ 'text/x-c' ]

    accepted_filenames = [ None ]

    accepted_extensions = [ '.h' ]

    rules = { }

    @classmethod
    def accepted(klass, filedata):
        return (klass._test_fileextension(filedata.extension))

    def __init__(self, context, settings, node):
        super(ParserCHeaders, self).__init__(context, settings, node)

    def check_double_inclusion(self):
        pass

    def check_simple_defines(self):
        pass

    def check_structs(self):
        pass

    def check_enums(self):
        pass

    def check_unions(self):
        pass

    def check_externals(self):
        pass

    def check_globals(self):
        pass

    def check_typedefs(self):
        pass

    def check_cleanliness(self):
        """
        Quick explanation: There should be nothing else except:
        header, type definitions, variable definitions and function prototypes
        """
        pass

    def post_process(self):
        """Save data into context, perform some meta-checks"""
        pass

    rules = {
                'double_inclusion' : check_double_inclusion,
                'simple_defines': check_simple_defines,
                'structs': check_structs,
                'enums': check_enums,
                'unions': check_unions,
                'externals': check_externals,
                'globals': check_globals,
                'typedefs': check_typedefs,
                'cleanliness': check_cleanliness
            }


name = 'parser_c_headers'
parser = ParserCHeaders
