
import inspect
from importlib import import_module
module_name = "48_rotate_image"

def test_48():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    matrix = [
 [1,2,3],
 [4,5,6],
 [7,8,9]
]
    Output = [
 [7,4,1],
 [8,5,2],
 [9,6,3]
]
    assert func(matrix) == Output
