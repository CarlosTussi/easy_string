import sys

# Always run from easy_string/test
sys.path += ["/easy_string_ctl"]

from easy_string import *

if __name__ == '__main__':
    print(word_count("hello world hello"))
    print(word_count("hello world bye world hello bye world"))
