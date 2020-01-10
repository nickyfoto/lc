
import inspect
from importlib import import_module
module_name = "869_reordered_power_of_2"

def test_869():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    N = 1
    Output = True
    assert func(N) == Output


    N = 10
    Output = False
    assert func(N) == Output
    
    N = 16
    Output = True
    assert func(N) == Output
    N = 24
    Output = False
    assert func(N) == Output
    N = 46
    Output = True
    assert func(N) == Output