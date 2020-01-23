
import inspect
from importlib import import_module
module_name = "396_rotate_function"

def test_396():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    A = [4, 3, 2, 6]
    Output = 26

    assert func(A) == Output

    A = [1,2,3,4,5,6,7,8,9,10]
    Output = 330
    assert func(A) == Output