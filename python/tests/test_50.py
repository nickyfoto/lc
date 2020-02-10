
import inspect
from importlib import import_module
module_name = "50_powx_n"

def test_50():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    x = 2.00000
    n = 10
    Output = 1024.0
    assert func(x, n) == Output
    x = 2.00000
    n = 2
    Output = 4.0
    assert func(x, n) == Output

    

    x = 2.00000
    n = 11
    Output = 2048.0
    assert func(x, n) == Output

    # x = 2.10000
    # n = 3
    # Output = 9.26100
    # assert func(x, n) == Output

    x = 2.00000
    n = -2
    Output = 0.25000
    assert func(x, n) == Output



    x = 0.00001
    n = 2147483647
    Output = 0
    assert func(x, n) == Output
