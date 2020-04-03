
import inspect
from importlib import import_module
module_name = "287_find_the_duplicate_number"

def test_287():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(nums) -> int == Output
