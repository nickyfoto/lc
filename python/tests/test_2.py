
import inspect
from importlib import import_module
module_name = "2_add_two_numbers"
from lcpy import build_head

def test_2():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    l1 = [2, 4, 3]
    l1 = build_head(l1)
    l2 = [5, 6, 4]
    l2 = build_head(l2)
    Output = build_head([7, 0, 8])

    assert func(l1, l2) == Output

    l1 = [1]
    l1 = build_head(l1)
    l2 = [9, 9, 9]
    l2 = build_head(l2)
    Output = build_head([0,0,0,1])
    assert func(l1, l2) == Output

    # l1 = [1, 8]
    # l1 = build_head(l1)
    # l2 = [0]
    # l2 = build_head(l2)
    # Output = build_head([1,8])
    # assert func(l1, l2) == Output