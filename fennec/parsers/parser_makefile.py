
import logging
import re
from parser_base import ParserBase

class ParserMakefile(ParserBase):
    """
    Parser used to check text files
    """

    accepted_filetypes = [ None ]

    accepted_filenames = [ 'Makefile' ]

    rules = { }

    @classmethod
    def accepted(klass, filedata):
        return (klass._test_filename(filedata.file_name))

    def __init__(self, context, settings, node):
        super(ParserMakefile, self).__init__(context, settings, node)

    def check_header(self):
        pass

    def check_base_rules(self):
        pass

    def check_use_of_Wflags(self):
        pass

    def check_rule_dotPHONY(self):
        pass

    def check_use_of_gcc(self):
        pass

    # def check_multi_newline(self):
    #     i = 0;
    #     for line in self.content_lines:
    #         i += 1
    #         regexp = re.compile("^\n$")
    #         test = regexp.search(line)
    #         if test != None:
    #             if empty_newline == True:
    #                 self.log(logging.CRITICAL,
    #                         "has multiple newlines.", line = i)
    #             else:
    #                 empty_newline = True;
    #         else:
    #             empty_newline = False

    rules = { 'header'   : check_header }


name = 'parser_makefile'
parser = ParserMakefile
