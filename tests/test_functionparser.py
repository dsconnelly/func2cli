from func2cli import FunctionParser
from tests.funcs import add_two, subtract_three

def test_parse():
    parser = FunctionParser('test', [add_two, subtract_three])

    assert parser.run(['add-two', '2', '3']) == 5
    assert parser.run(['subtract-three', '10', '7', '2']) == 1
