
import inspect
from importlib import import_module
module_name = "829_consecutive_numbers_sum"

def test_829():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    N = 15
    Output = 4
    assert func(N) == Output
    N = 9
    Output = 3
    assert func(N) == Output
    N = 5
    Output = 2
    assert func(N) == Output
    
    N = 8504986
    Output = 16
    assert func(N) == Output