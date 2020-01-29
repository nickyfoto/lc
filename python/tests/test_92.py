
import inspect
from importlib import import_module
module_name = "92_reverse_linked_list_ii"
from lcpy import build_head
def test_92():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    # head = build_head([1,2,3,4,5,6])
    # m = 2
    # n = 4
    # Output = build_head([1,4,3,2,5,6])
    # assert func(head, m, n) == Output



    head = build_head([3,5])
    m = 1
    n = 2
    Output = build_head([5,3])
    assert func(head, m, n) == Output



