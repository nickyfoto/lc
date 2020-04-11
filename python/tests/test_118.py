
import inspect
from importlib import import_module
module_name = "118_pascals_triangle"

def test_118():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    numRows = 5
    Output = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    assert func(numRows) == Output
