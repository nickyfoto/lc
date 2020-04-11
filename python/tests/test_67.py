
import inspect
from importlib import import_module
module_name = "67_add_binary"

def test_67():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    a = "1010"
    b = "1011"
    Output = "10101"

    assert func(a, b) == Output
