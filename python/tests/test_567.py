
import inspect
from importlib import import_module
module_name = "567_permutation_in_string"

def test_567():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    s1 = "ab"
    s2 = "eidbaooo"
    Output = True
    assert func(s1, s2) == Output

    s1 = "ab"
    s2 = "eidboaoo"
    Output = False
    assert func(s1, s2) == Output

    s1 = "adc"
    s2 = "dcda"
    Output = True
    assert func(s1, s2) == Output

    s1 = "abc"
    s2 = "cccccbabbbaaaa"
    Output = True
    assert func(s1, s2) == Output