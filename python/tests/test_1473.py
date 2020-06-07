
import inspect
from importlib import import_module
module_name = "1473_paint_house_iii"

def test_1473():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(houses, cost, m, n, target) == Output
