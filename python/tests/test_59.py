
import inspect
from importlib import import_module
module_name = "59_spiral_matrix_ii"

def test_59():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    n = 5
    Output = 3
    assert func(n) == Output
