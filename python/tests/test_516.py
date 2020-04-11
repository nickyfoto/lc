
import inspect
from importlib import import_module
module_name = "516_longest_palindromic_subsequence"

def test_516():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    # s = "bbbab"
    # Output = 4
    # assert func(s) == Output

    s = "aaa"
    Output = 3
    assert func(s) == Output
