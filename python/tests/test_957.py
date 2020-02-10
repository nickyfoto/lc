
import inspect
from importlib import import_module
module_name = "957_prison_cells_after_n_days"

def test_957():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    cells = [0,1,0,1,1,0,0,1]
    N = 7
    Output = [0,0,1,1,0,0,0,0]
    assert func(cells, N) == Output

    cells = [1,0,0,1,0,0,1,0]
    N = 1000000000
    Output = [0,0,1,1,1,1,1,0]
    assert func(cells, N) == Output

    cells = [0,0,0,1,1,0,1,0]
    N = 574
    Output = [0,0,0,1,1,0,1,0]
    assert func(cells, N) == Output


    cells = [1,0,0,1,0,0,0,1]
    N = 826
    Output = [0,1,1,0,1,1,1,0]
    assert func(cells, N) == Output