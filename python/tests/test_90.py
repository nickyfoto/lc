
import inspect
from importlib import import_module
module_name = "90_subsets_ii"

def test_90():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    nums = [1,2,2]
    Output =  [
                 [2],
                 [1],
                 [1,2,2],
                 [2,2],
                 [1,2],
                 []
                ]
    

    assert func(nums) == Output
