
import inspect
from importlib import import_module
module_name = "115_distinct_subsequences"

def test_115():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(s, t) == Output
