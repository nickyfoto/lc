
import inspect
from importlib import import_module
module_name = "430_flatten_a_multilevel_doubly_linked_list"

def test_430():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(head: 'Node') -> 'Node' == Output
