
import inspect
from importlib import import_module
module_name = "223_rectangle_area"

def test_223():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    Output = 45
    assert func(-3, 0, 3, 4, 0, -1, 9,  2) == Output
    Output = 24
    assert func(-2, -2, 2, 2, -3, -3, 3, -1) == Output