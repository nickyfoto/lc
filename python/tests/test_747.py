
import inspect
from importlib import import_module
module_name = "747_largest_number_at_least_twice_of_others"

def test_747():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(nums) == Output
