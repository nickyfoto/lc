
import inspect
from importlib import import_module
module_name = "95_unique_binary_search_trees_ii"

def test_95():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(n) == Output
