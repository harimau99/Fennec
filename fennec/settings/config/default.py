"""
Default configuration for Fennec
"""

BR_DEBUG = False;

BR_PARSERS = {
    'parsers.text_parser',
    'parsers.c_parser',
    'parsers.makefile_parser',
    'parsers.authorfile_parser',
}

BR_READ_ENV = True # If set to False, the info will be inferred from the files
