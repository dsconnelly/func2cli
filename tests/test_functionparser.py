from func2cli import FunctionParser
from tests.funcs import add_two, add_with_default, subtract_three

def test_default():
    parser = FunctionParser([add_with_default])

    assert parser.run(['add-with-default', '1']) == 6
    assert parser.run(['add-with-default', '1', '--q', '-2']) == -1

def test_simple():
    parser = FunctionParser([add_two, subtract_three])

    assert parser.run(['add-two', '2', '3']) == 5
    assert parser.run(['subtract-three', '10', '7', '2']) == 1
