
import inspect
from importlib import import_module
module_name = "131_palindrome_partitioning"

def test_131():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    s = "aab"
    Output = [
                ["aa","b"],
                ["a","a","b"]
                ]
    # assert func(s) == Output
    
    s = "efe"
    Output = [["e","f","e"],["efe"]]
    assert func(s) == Output
