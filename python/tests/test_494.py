
import inspect
from importlib import import_module
module_name = "494_target_sum"

def test_494():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(nums, S) == Output
