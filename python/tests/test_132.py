
import inspect
from importlib import import_module
module_name = "132_palindrome_partitioning_ii"

def test_132():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    
    s = 'aab'
    Output = 1
    assert func(s) == Output
