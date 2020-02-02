
import inspect
from importlib import import_module
module_name = "33_search_in_rotated_sorted_array"

def test_33():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    nums = [4,5,6,7,0,1,2]
    target = 0
    Output = 4
    assert func(nums, target) == Output

    nums = [4,5,6,7,0,1,2]
    target = 3
    Output = -1
    assert func(nums, target) == Output

    nums = [1,3]
    target = 2
    Output = -1
    assert func(nums, target) == Output
    
    nums = [1,3]
    target = 3
    Output = 1
    assert func(nums, target) == Output

    nums = [5,1,3]
    target = 2
    Output = -1
    assert func(nums, target) == Output