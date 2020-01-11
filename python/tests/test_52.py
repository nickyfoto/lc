
import inspect
from importlib import import_module
module_name = "52_n_queens_ii"

def test_52():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    n = 4
    Output = 2
    assert func(n) == Output

    # n = 1
    # Output = 1
    # assert func(n) == Output

    # n = 3
    # Output = 0
    # assert func(n) == Output

    # n = 5
    # Output = 10
    # assert func(n) == Output

