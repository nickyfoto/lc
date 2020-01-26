
import inspect
from importlib import import_module
module_name = "47_permutations_ii"

def test_47():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    nums = [1,1,2]
    Output = [
                [1,1,2],
                [1,2,1],
                [2,1,1]
                ]

    assert func(nums) == Output
