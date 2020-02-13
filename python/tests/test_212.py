
import inspect
from importlib import import_module
module_name = "212_word_search_ii"

def test_212():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    board = [
 ['o','a','a','n'],
 ['e','t','a','e'],
 ['i','h','k','r'],
 ['i','f','l','v']
]
    words = ["oath","pea","eat","rain"]
    Output = ["eat","oath"]
    assert func(board, words) == Output

    board = [["a","a"]]
    words = ["a"]
    Output = ["a"]
    assert func(board, words) == Output

    board = [["a","b"],["a","a"]]
    words = ["aba","baa","bab","aaab","aaa","aaaa","aaba"]
    Output = ["aaa","aaab","aaba","aba","baa"]
    assert func(board, words) == Output
