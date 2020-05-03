
import inspect
from importlib import import_module
module_name = "76_minimum_window_substring"

def test_76():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    s = "ADOBECODEBANC"
    t = "ABC"
    Output = "BANC"
    assert func(s, t) == Output
