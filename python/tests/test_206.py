
import inspect
from importlib import import_module
module_name = "206_reverse_linked_list"
from lcpy import build_head
def test_206():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    head = build_head([1,2,3,4,5])
    Output = build_head([5,4,3,2,1])
    assert func(head) == Output
