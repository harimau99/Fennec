
import logging
from parser_base import ParserBase

class ParserText(ParserBase):
    """
    Parser used to check text files
    """

    accepted_filetypes = [ None ]

    accepted_filenames = [ None ]

    @classmethod
    def accepted(klass, filedata):
        return True

    def __init__(self, context, settings, node):
        super(ParserText, self).__init__(context, settings, node)
        with open(self.node.path) as f:
            self.content = f.readlines()

    def check_ascii(self):
        i = 0
        for line in self.content:
            i += 1
            try:
                line.decode('ascii')
            except UnicodeDecodeError:
                self.logger.warning("File {0} at line {1} isn't pure ascii.".
                                    format(self.node.file_name, i));

    def check_linelen(self):
        i = 0
        for line in self.content:
            i += 1
            linerep = line.replace('\t', '    ')
            if (line[81:]):
                self.logger.warning("File {0} at line {1} contains more than 80 chars.".
                                    format(self.node.file_name, i))

    rules = { 'ascii'   : check_ascii,
              'linelen'  : check_linelen}


name = 'parser_text'
parser = ParserText
