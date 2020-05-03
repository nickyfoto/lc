
import inspect
from importlib import import_module
module_name = "159_longest_substring_with_at_most_two_distinct_characters"

def test_159():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(s) == Output
