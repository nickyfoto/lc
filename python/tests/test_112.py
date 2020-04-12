
import inspect
from importlib import import_module
module_name = "112_path_sum"

def test_112():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(root, _sum) == Output
