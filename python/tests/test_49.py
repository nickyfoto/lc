
import inspect
from importlib import import_module
module_name = "49_group_anagrams"

def test_49():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(strs) == Output
