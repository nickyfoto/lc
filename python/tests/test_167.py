
import inspect
from importlib import import_module
module_name = "167_two_sum_ii_input_array_is_sorted"

def test_167():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(numbers, target, debug=False) == Output
