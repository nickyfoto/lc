
import inspect
from importlib import import_module
module_name = "719_find_k_th_smallest_pair_distance"

def test_719():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(nums, k) == Output
