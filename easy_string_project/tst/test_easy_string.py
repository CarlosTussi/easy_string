import sys
sys.path += ["../src/easy_string"]

from easy_string import *

def test_word_count():
    assert word_count("hello world hello") == {'hello': 2, 'world': 1}
    assert word_count("") == {}
    

def test_remove_word():
    pass
