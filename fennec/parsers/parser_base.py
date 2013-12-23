
class ParserBase(object):
    """
    Parser base class
    """

    accepted_filetypes = [ ]

    accepted_filenames = [ ]

    rules = { }

    @classmethod
    def accepted(klass, filedata):
        return False

    @classmethod
    def accepted_filetypes(klass):
        return klass.accepted_filetypes

    @classmethod
    def _test_filetype(klass, filetype):
        for accepted_filetype in klass.accepted_filetypes:
            if (filetype == accepted_filetype):
                return True
        return False

    @classmethod
    def accepted_filenames(klass):
        return klass.accepted_filenames

    @classmethod
    def _test_filename(klass, filename):
        for accepted_filename in klass.accepted_filenames:
            if (filename == accepted_filename):
                return True
        return False

    def __init__(self, settings, node):
        pass

    def audit(self):
        for rulename, rulefunct in self.rules.iteritems():
            rulefunct(self)

name = 'parser_base'
parser = ParserBase
