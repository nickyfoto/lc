
import inspect
from importlib import import_module
module_name = "31_next_permutation"

def test_31():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    nums = [1,2,3]
    Output = [1,3,2]
    assert func(nums) == Output
    
    nums = [3,2,1]
    Output = [1,2,3]
    assert func(nums) == Output

    nums = [1,1,5]
    Output = [1,5,1]
    assert func(nums) == Output

    nums = [6,8,3,2]
    Output = [8,2,3,6]
    assert func(nums) == Output
    
    nums = [6,8,7,3,2]
    Output = [7,2,3,6,8]
    assert func(nums) == Output

    nums = [3,1,6,6]
    Output = [3,6,1,6]
    assert func(nums) == Output

    nums = [1,5,1]
    Output = [5,1,1]
    assert func(nums) == Output



