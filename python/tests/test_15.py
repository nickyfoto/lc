
import inspect
from importlib import import_module
module_name = "15_3sum"

def test_15():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    nums = [-1, 0, 1, 2, -1, -4]
    Output = [
                [-1, 0, 1],
                [-1, -1, 2]
                ]
    assert func(nums) == Output


    nums = [1,2,3]
    Output = []
    assert func(nums) == Output

    # nums =  [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    # Output = [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
    # assert func(nums) == Output
