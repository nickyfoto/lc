
import inspect
from importlib import import_module
module_name = "138_copy_list_with_random_pointer"

def test_138():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(head) == Output
