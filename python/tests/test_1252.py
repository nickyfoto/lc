
import inspect
from importlib import import_module
module_name = "1252_cells_with_odd_values_in_a_matrix"

def test_1252():

    m = import_module(module_name)  

    s = m.Solution()

    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]

    func = getattr(s, fn)

    n = 2
    m = 3
    indices = [[0,1],[1,1]]


    assert func(n, m, indices) == 6
