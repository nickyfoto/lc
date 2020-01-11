
import inspect
from importlib import import_module
module_name = "51_n_queens"

def test_51():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    
    n = 4
    Output = 2
    assert func(n) == Output
