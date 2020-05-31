
import inspect
from importlib import import_module
module_name = "1438_longest_continuous_subarray_with_absolute_diff_less_than_or_equal_to_limit"

def test_1438():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    nums = [8,2,4,7]
    limit = 4
    Output = 2
    assert func(nums, limit) == Output

    nums = [10,1,2,4,7,2]
    limit = 5
    Output = 4
    assert func(nums, limit) == Output

    nums = [4,2,2,2,4,4,2,2]
    limit = 0
    Output = 3
    assert func(nums, limit) == Output