
import inspect
from importlib import import_module
module_name = "992_subarrays_with_k_different_integers"

def test_992():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(A, K) == Output
