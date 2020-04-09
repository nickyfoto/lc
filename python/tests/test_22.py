
import inspect
from importlib import import_module
module_name = "22_generate_parentheses"

def test_22():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(n) == Output
