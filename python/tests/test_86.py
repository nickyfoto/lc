
import inspect
from importlib import import_module
module_name = "86_partition_list"

def test_86():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(head, x) == Output
