
import logging
import re
from parser_base import ParserBase

class ParserText(ParserBase):
    """
    Parser used to check text files
    """

    accepted_filetypes = [ None ]

    accepted_filenames = [ None ]

    rules = { }

    @classmethod
    def accepted(klass, filedata):
        return True

    def __init__(self, context, settings, node):
        super(ParserText, self).__init__(context, settings, node)

    def check_ascii(self):
        i = 0
        for line in self.content_lines:
            i += 1
            try:
                line.decode('ascii')
            except UnicodeDecodeError:
                self.log(logging.WARNING, "isn't pure ASCII.", line = i)

    def check_linelen(self):
        i = 0
        for line in self.content_lines:
            i += 1
            linerep = line.replace('\t', '    ')
            if (line[81:]):
                self.log(logging.CRITICAL, "has more than"
                                            " 80 chars length.", line = i)

    def check_trailing_whitespace(self):
        i = 0
        for line in self.content_lines:
            i += 1
            regexp = re.compile("^.*[ \t]+$")
            test = regexp.search(line)
            if test != None:
                self.log(logging.ERROR, "has trailing whitespace(s)"
                                            " or tab(s)", line = i)

    def check_unusual_characters(self):
        i = 0
        for line in self.content_lines:
            i += 1
            regexp = re.compile("[\v\a\b\f\r]+")
            test = regexp.search(line)
            if test != None:
                self.log(logging.WARNING, "has an unusual character."
                                    " Is it intentional ?", line = i)

    def check_multi_newline(self):
        i = 0
        empty_newline = False
        for line in self.content_lines:
            i += 1
            regexp = re.compile("^\n$")
            test = regexp.search(line)
            if test != None:
                if empty_newline == True:
                    self.log(logging.ERROR,
                            "has multiple newlines.", line = i)
                else:
                    empty_newline = True;
            else:
                empty_newline = False

    rules = { 'ascii'   : check_ascii,
              'linelen'  : check_linelen,
              'trailing_whitespace' : check_trailing_whitespace,
              'unusual_chars': check_unusual_characters,
              'multi_newline': check_multi_newline }


name = 'parser_text'
parser = ParserText
