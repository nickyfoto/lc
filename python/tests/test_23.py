
import inspect
from importlib import import_module
module_name = "23_merge_k_sorted_lists"
from lcpy import build_head
def test_23():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    lists = [
                build_head([1,4,5]),
                build_head([1,3,4]),
                build_head([2,6])
                ]
    
    Output = None
    assert func(lists) == Output
