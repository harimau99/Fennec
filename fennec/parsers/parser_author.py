
import re
import logging
from parser_base import ParserBase

class ParserAuthor(ParserBase):
    """
    Parser used to check 42 School author files
    """

    accepted_filetypes = [ None ]

    accepted_filenames = [ 'auteur' ]

    accepted_extensions = [ None ]

    @classmethod
    def accepted(klass, filedata):
        return (klass._test_filename(filedata.file_name))

    def __init__(self, context, settings, node):
        super(ParserAuthor, self).__init__(context, settings, node)
        self.found_xlogins = [ ]

    def check_format(self):
        # Double check to prevent missing double \n !! Only way for the moment
        i = 0
        for line in self.content_lines:
            regexp = re.compile("^[a-z-]{3,8}\n$")
            test = regexp.search(line)
            regexp2 = re.compile("^[a-z-]{3,8}$")
            test2 = regexp2.search(line)
            if test == None or test2 == None:
                self.log(logging.CRITICAL, "isn't correctly formatted.")
            else:
                self.found_xlogins.append(test.string[:-1])

    def post_process(self):
        # check if author container already filled in,
        # if yes... more than one author file = CRITICAL
        if self.context['author'] != None:
            self.log(logging.CRITICAL, "is another author file. "
                                        "There should be only one !")
        elif (len(self.found_xlogins) != len(set(self.found_xlogins))) == True:
            self.log(logging.CRITICAL, "has duplicate authors. "
                                        " Check your author files !")
        else:
            self.context['author'] = {
                'node': self.node,
                'node_path': self.node.path,
                'user_names': self.found_xlogins
            }

    rules = [
              ('format', check_format)
            ]


name = 'parser_author'
parser = ParserAuthor
