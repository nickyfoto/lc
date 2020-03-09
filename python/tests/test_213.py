
import inspect
from importlib import import_module
module_name = "213_house_robber_ii"

def test_213():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    nums = [1,2,3,1]
    Output = 4
    assert func(nums) == Output
