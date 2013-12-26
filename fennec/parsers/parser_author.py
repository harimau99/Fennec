
import re
import logging
from parser_base import ParserBase

class ParserAuthor(ParserBase):
    """
    Parser used to check 42 author files
    """

    accepted_filetypes = [ None ]

    accepted_filenames = [ 'auteur' ]

    @classmethod
    def accepted(klass, filedata):
        return (klass._test_filename(filedata.file_name))

    def __init__(self, context, settings, node):
        super(ParserAuthor, self).__init__(context, settings, node)

    def check_format(self):
        # Double check to prevent missing double \n !! Only way for the moment
        i = 0;
        for line in self.content_lines:
            regexp = re.compile("^[a-z-]{3,8}\n$")
            test = regexp.search(line)
            regexp2 = re.compile("^[a-z-]{3,8}$")
            test2 = regexp2.search(line)
            if test == None or test2 == None:
                self.log(logging.CRITICAL, "isn't correctly formatted.")

    def save_author(self):
        # Save author(s) into context container !
        pass

    rules = { 'format'   : check_format }


name = 'parser_author'
parser = ParserAuthor
