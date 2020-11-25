import sys
sys.path.append("../app")
from utils import stemmed_words


def test_stemmed_words():
    test_input = [
        ("hello i'm doing my test task", ['hello', 'do', 'test', 'task']),
        ("these are test inputs", ['test', 'input']),
        ("add more inputs here", ['add', 'input'])
    ]

    for inp in test_input:
        result = stemmed_words(inp[0])
        assert result == inp[1]