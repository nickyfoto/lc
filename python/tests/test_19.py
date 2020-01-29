
import inspect
from importlib import import_module
module_name = "19_remove_nth_node_from_end_of_list"
from lcpy import build_head
def test_19():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    head = build_head([1,2,3,4,5])
    n = 2
    Output = build_head([1,2,3,5])

    head = build_head([1,2])
    n = 1

    # head = build_head([1])
    # n = 1

    # head = build_head([1,2])
    # n = 2
    assert func(head, n) == Output


