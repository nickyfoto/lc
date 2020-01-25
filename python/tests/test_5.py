
import inspect
from importlib import import_module
module_name = "5_longest_palindromic_substring"

def test_5():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    # s = "babad"
    # Output = "bab"
    # assert func(s) == Output

    # s = "cbbd"
    # Output = "bb"
    # assert func(s) == Output

    s = "aaaa"
    Output = "aaaa"
    assert func(s) == Output