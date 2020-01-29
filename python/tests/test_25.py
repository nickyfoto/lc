
import inspect
from importlib import import_module
module_name = "25_reverse_nodes_in_k_group"
from lcpy import build_head
def test_25():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    head = build_head([1,2,3,4,5])
    k = 2
    Output = build_head([2,1,4,3,5])
    assert func(head, k) == Output


    # head = build_head([1,2,3,4,5])
    # k = 3
    # Output = build_head([3,2,1,4,5])
    # assert func(head, k) == Output
