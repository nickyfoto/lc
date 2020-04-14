
import inspect
from importlib import import_module
module_name = "142_linked_list_cycle_ii"

def test_142():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(head) == Output
