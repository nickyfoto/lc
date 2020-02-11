
import inspect
from importlib import import_module
module_name = "61_rotate_list"
from lcpy import build_head
def test_61():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    head = build_head([1,2,3,4,5])
    k = 2
    Output = build_head([4,5,1,2,3])
    assert func(head, k).value_eq(Output)

    head = build_head([0,1,2])
    k = 4
    Output = build_head([2,0,1])
    assert func(head, k).value_eq(Output)

    head = build_head([1,2])
    k = 1
    Output = build_head([2,1])
    assert func(head, k).value_eq(Output)

    head = build_head([1,2,3])
    k = 2000000000
    # k = 2
    Output = build_head([2,3,1])
    assert func(head, k).value_eq(Output)




