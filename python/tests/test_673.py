
import inspect
from importlib import import_module
module_name = "673_number_of_longest_increasing_subsequence"

def test_673():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(a) == Output
