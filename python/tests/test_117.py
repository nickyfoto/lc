
import inspect
from importlib import import_module
module_name = "117_populating_next_right_pointers_in_each_node_ii"

def test_117():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(root) == Output
