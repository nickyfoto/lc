
import inspect
from importlib import import_module
module_name = "239_sliding_window_maximum"

def test_239():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    Output = [3,3,5,5,6,7]
    assert func(nums, k) == Output
