
import inspect
from importlib import import_module
module_name = "154_find_minimum_in_rotated_sorted_array_ii"

def test_154():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    nums = [1,3,5]
    Output = 1
    assert func(nums) == Output

    nums = [2,2,2,0,1]
    Output = 0
    assert func(nums) == Output

    nums = [2,3,4,0,1]
    Output = 0
    assert func(nums) == Output

    nums = [1,2,2,2,0,1,1]
    Output = 0
    assert func(nums) == Output

