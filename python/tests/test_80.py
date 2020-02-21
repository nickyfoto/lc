
import inspect
from importlib import import_module
module_name = "80_remove_duplicates_from_sorted_array_ii"

def test_80():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    nums = [1,1,1,2,2,3]
    Output = 5
    assert func(nums) == Output

    nums = [0,0,1,1,1,1,2,3,3]
    Output = 7
    assert func(nums) == Output
