
import inspect
from importlib import import_module
module_name = "724_find_pivot_index"

def test_724():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(nums) == Output
