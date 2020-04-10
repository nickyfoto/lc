
import inspect
from importlib import import_module
module_name = "498_diagonal_traverse"

def test_498():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(matrix) == Output
