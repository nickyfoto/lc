
import inspect
from importlib import import_module
module_name = "891_sum_of_subsequence_widths"

def test_891():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    
    # A = [2,1,3]
    # Output = 6
    # assert func(A) == Output
    
    # A = [3,7,2,3]
    # Output = 35
    # assert func(A) == Output

    A = [8,15,30,10,29,10,40,28,31,31,21,10,28,14,25,21,23,14,34,16]
    Output = 28127892
    assert func(A) == Output