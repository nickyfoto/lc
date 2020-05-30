
import inspect
from importlib import import_module
module_name = "1040_moving_stones_until_consecutive_ii"

def test_1040():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    stones [6,5,4,3,10]
    Output = [2,3]
    

    assert func(stones) == Output
