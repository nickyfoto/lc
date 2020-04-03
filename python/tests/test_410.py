
import inspect
from importlib import import_module
module_name = "410_split_array_largest_sum"

def test_410():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    nums = [7,2,5,10,8]
    m = 2
    Output = 18
    assert func(nums, m) == Output
