
import inspect
from importlib import import_module
module_name = "189_rotate_array"

def test_189():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(nums, k) == Output
