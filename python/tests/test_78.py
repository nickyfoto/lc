
import inspect
from importlib import import_module
module_name = "78_subsets"

def test_78():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    nums = [1,2,3]
    Output = [
                [3],
                [1],
                [2],
                [1,2,3],
                [1,3],
                [2,3],
                [1,2],
                []
                ]
    assert func(nums) == Output
