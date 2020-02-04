
import inspect
from importlib import import_module
module_name = "41_first_missing_positive"

def test_41():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    nums = [1,2,0]
    Output = 3
    assert func(nums) == Output

    nums = [3,4,-1,1]
    Output = 2
    assert func(nums) == Output
  
    nums = [7,8,9,11,12]
    Output = 1
    assert func(nums) == Output
    
    nums = [2]
    Output = 1
    assert func(nums) == Output

