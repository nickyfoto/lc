
import inspect
from importlib import import_module
module_name = "62_unique_paths"

def test_62():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    
    m = 7
    n = 3
    Output = 28
    assert func(m, n) == Output
