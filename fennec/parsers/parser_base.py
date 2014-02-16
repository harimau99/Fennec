
import logging

class ParserBase(object):
    """
    Parser base class
    """

    accepted_filetypes = [ None ]

    accepted_filenames = [ None ]

    accepted_extensions = [ None ]

    rules = [ ]

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

    @classmethod
    def accepted_fileextensions(klass):
        return klass.accepted_extensions

    @classmethod
    def _test_fileextension(klass, fileextension):
        for accepted_fileextension in klass.accepted_extensions:
            if (fileextension == accepted_fileextension):
                return True
        return False

    def __init__(self, context_container, settings, node):
        self.logger = logging.getLogger('fennec')
        self.context = context_container
        self.settings = settings
        self.node = node
        with open(self.node.path, 'U') as f:
            self.content_lines = f.readlines()
        with open(self.node.path, 'U') as f:
            self.content_full = f.read()

    def log(self, level, message, filename = None, line = None):
        if filename == None:
            filedesc = self.node.path_fom_cwd
        else:
            filedesc = filename
        if line == None:
            log_msg = "File \"{0}\" {1}"
            self.logger.log(level, log_msg.format(filedesc, message))
        else:
            log_msg = "File \"{0}\" (line {1}) {2}"
            self.logger.log(level, log_msg.format(filedesc, line, message))

    def post_process(self):
        pass

    def audit(self):
        for rulename, rulefunct in self.rules:
            rulefunct(self)
        self.post_process()

name = 'parser_base'
parser = ParserBase
