
import inspect
from importlib import import_module
module_name = "487_max_consecutive_ones_ii"

def test_487():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(nums) == Output
