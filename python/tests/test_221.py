
import inspect
from importlib import import_module
module_name = "221_maximal_square"

def test_221():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(matrix) == Output
