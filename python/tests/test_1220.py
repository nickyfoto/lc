
import inspect
from importlib import import_module
module_name = "1220_count_vowels_permutation"

def test_1220():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(n) == Output
