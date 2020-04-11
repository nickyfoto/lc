
import inspect
from importlib import import_module
module_name = "98_validate_binary_search_tree"

def test_98():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(root) == Output
