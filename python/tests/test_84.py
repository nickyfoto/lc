
import inspect
from importlib import import_module
module_name = "84_largest_rectangle_in_histogram"

def test_84():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    heights = [2,1,5,6,2,3]
    Output = 10

    assert func(heights) == Output
