
import inspect
from importlib import import_module
module_name = "34_find_first_and_last_position_of_element_in_sorted_array"

def test_34():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    
    nums = [5,7,7,8,8,10]
    target = 8
    Output = [3,4]
    assert func(nums, target) == Output

    # nums = [5,7,7,8,8,10]
    # target = 6
    # Output = [-1,-1]
    # assert func(nums, target) == Output
