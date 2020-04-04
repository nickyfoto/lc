
import inspect
from importlib import import_module
module_name = "283_move_zeroes"

def test_283():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(nums) == Output
