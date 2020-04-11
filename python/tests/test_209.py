
import inspect
from importlib import import_module
module_name = "209_minimum_size_subarray_sum"

def test_209():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(s, nums) == Output
