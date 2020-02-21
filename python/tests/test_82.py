
import inspect
from importlib import import_module
module_name = "82_remove_duplicates_from_sorted_list_ii"

def test_82():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(head) == Output
