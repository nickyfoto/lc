
import inspect
from importlib import import_module
module_name = "1289_minimum_falling_path_sum_ii"

def test_1289():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(arr) == Output
