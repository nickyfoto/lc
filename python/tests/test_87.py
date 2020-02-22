
import inspect
from importlib import import_module
module_name = "87_scramble_string"

def test_87():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(s1, s2) == Output
