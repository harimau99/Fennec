# -*- coding: utf-8 -*-
"""
C syntax rules for 42 Coding School

Summary:
  - Check header data is concurrent with file data (creation timestamp etc.)
  - Lines must not exceed 80 chars.
  - Maximum 5 functions per file.
  - Header parsing ?
  - Forbidden keywords
  - Forbidden / Allowed functions
  - Pair number of {, ( and [
  - Keyword formatting:
    - return (*)
    - while (*)(check for ; <= are you sure ?)
    - if () //{}
    - else {}
  - Tabs between type & function name
  - Tabs between function and arguments
  - Function without arguments (must have void at least)
  - Maximum 25 lines per function
  - Maximum 4 params in function prototype and/or function declaration
  - Logic between function type and usage ? (complex)
  - Space after ,
  - ; at eol
  - empty line after each block
  - delaration and initialisation on the same line
  - * next to var name and not var type
  - empty line after var declaration and only empty line in function
  - no trailing whitespaces / tabs
  - no space after keyword
  - ternaires imbriqués
  - ternaires hors assignation
  - no french words/only english for vars
  - no caps, only letters, _ and numbers
  - structure begins with s_
  - typedef begins with t_
  - union starts with u_
  - enum starts with e_
  - global starts with g_
  - indentation using tabs and no spaces
  - var name alignment
  - no comments inside functions
  - one declaration / instruction per line except tables, static, global, constant
  - empty line = no tabs or spaces
  - {} = alone on line, nothing else except struct/union/enum
  - new line after if / while/ ...
  - ; not at eol must have space
  - = - + > < / * % ! must have separated by space
  - declarations only at start of block
  - if new line inside control structure if(), while() etc,
    can span multiple lines but must have good indentation
  - function prototypes must have names
  - no more than 5 variables per function block
  - function names must be aligned in headers or in same file
  - one line between function declaration
  - all struct/ enum/ union must be named
  - the struct/enum/union declaration must be in global scope
  - tab between type and name for struct/enum/union but only one space
    for variable declaration ( see man p 11)
  - tab between parameters of typedef
  - alignment for typedef and names (p12)
  - headers can include struct, #define, prototypes and macros
  - all inclusion of .h before function prototypes
  - headers protected agains double inclusion (foo.h => FOO_H)
  - can have comment after endif
  - no .h if not used
  - macros only in .h except for special in .c BSD_SOURCE (???)
  - no multi-line macros
  - only names in CAPS are for macros
  - indentation of preprocessor instructions between # and command
  - no #if, #ifndef or #ifdef after the first function definition in a .c
  - forbidden functions: for, do/while, switch, goto, case
  - no C+= comments (//)
  - Alignment of C comments with **
  - no includes of .c
  - Makefile must have $(NAME), all, clean, fclean and re rules
  - the Makefile must not relink after second time of make
  - no wildcard usage (*.c)
  - no line above standard header
  - 1 tab = 4 cols
  """
import logging
import re

class Ruler:

	name = 'C 42 Unit'

	keywords = ['auto',
				'break',
				'case',
				'char',
				'const',
				'continue',
				'default',
				'do',
				'double',
				'else',
				'enum',
				'extern',
				'float',
				'for',
				'goto',
				'if',
				'int',
				'long',
				'register',
				'return'
				'short',
				'signed',
				'sizeof',
				'static',
				'struct',
				'switch',
				'typedef',
				'union',
				'unsigned',
				'void',
				'volatile',
				'while'
				]

	operators = [ '+', '-', '/', '*', '%', '>', '<',
				  '--', '++', '==', '!=', '>=', '<=',
				  '&&', '||', '!', '&', '|', '^', '~',
				  '<<', '>>', '=', '+=', '-=', '*=',
				  '/=', '%=', '<<=', '>>=', '&=', '^=',
				  '!='
				]
	other_marks = [',', ';', '{', '}', '[', ']']
	special_operators = ['__placeholder__?__placeholder__:__placeholder__',
						 '/*__placeholder__**__placeholder__*/']

	def __init__(self, settings, filename):
		self.logger = logging.getLogger('bernardo.C42')
		self.settings = settings
		self.filename = filename
		with open(filename) as source:
			self.filecontent = source.readlines()
		self.prepare_content();

	def prepare_content(self):
		pass

	def evaluate(self):
		self._spaces_around_operators();
		self._forbidden_keywords();
   		pass

   	def _spaces_around_operators(self):
   		i = 1
   		double_operator = [ '+', '-', '/', '*', '%', '>', '<',
				  '==', '!=', '>=', '<=', '&&', '||', '!', '&', '|', '^', '~',
				  '<<', '>>', '=', '+=', '-=', '*=',
				  '/=', '%=', '<<=', '>>=', '&=', '^=',
				  '!='
				]
   		for line in self.filecontent:
   			i += 1;

   	def _forbidden_keywords(self):
   		i = 1
   		keywords_to_check = [ 'case', 'do', 'for', 'goto', 'switch']
   		for line in self.filecontent:
   			for forbidden in keywords_to_check:
   				if forbidden in line:
   					self.logger.error("Forbidden keyword \"%s\" in file: \"%s\" at line %s", forbidden, self.filename, i);
   			i += 1;
































