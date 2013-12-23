
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
        with open(self.node.path) as f:
            self.content = f.read()

    def check_format(self):
        # Double check to prevent missing double \n !! Only way for the moment
        regexp = re.compile("^[a-z-]{3,8}\n$")
        test = regexp.search(self.content)
        regexp2 = re.compile("^[a-z-]{3,8}$")
        test2 = regexp2.search(self.content)
        if test == None or test2 == None:
            self.logger.warning("File {0} isn't correctly formatted.".
                                    format(self.node.file_name));

    rules = { 'format'   : check_format }


name = 'parser_author'
parser = ParserAuthor
