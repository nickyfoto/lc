
import inspect
from importlib import import_module
module_name = "79_word_search"

def test_79():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    board = [
 ['A','B','C','E'],
 ['S','F','C','S'],
 ['A','D','E','E']
]
    word = "ABCCED"
    Output = True
    assert func(board, word) == Output

    word = "SEE"
    Output = True
    assert func(board, word) == Output

    word = "ABCB"
    Output = False
    assert func(board, word) == Output

    board = [["a","a"]]
    word = "aaa"
    Output = False
    assert func(board, word) == Output

    board = [["A","B","C","E"],
             ["S","F","E","S"],
             ["A","D","E","E"]]
    word = "ABCESEEEFS"
    Output = True
    assert func(board, word) == Output