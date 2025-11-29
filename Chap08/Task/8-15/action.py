import language_demo
language_demo.print_language('Java')

from language_demo import print_language
language_demo.print_language('Python')

from language_demo import print_language as pl
pl('C++')

import language_demo as ld
ld.print_language('JavaScript')

from language_demo import *
print_language('Go')