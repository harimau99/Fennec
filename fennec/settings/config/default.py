"""
Default configuration for Fennec
"""

BR_DEBUG = False;

BR_PARSERS = {
    'parsers.parser_text',
    'parsers.parser_c',
    'parsers.parser_makefile',
    'parsers.parser_author',
}

BR_READ_ENV = True # If set to False, the info will be inferred from the files
