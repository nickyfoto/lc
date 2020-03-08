
import inspect
from importlib import import_module
module_name = "116_populating_next_right_pointers_in_each_node"

def test_116():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(root) == Output
