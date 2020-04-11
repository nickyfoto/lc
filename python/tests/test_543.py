
import inspect
from importlib import import_module
module_name = "543_diameter_of_binary_tree"

def test_543():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(root) == Output
