
import inspect
from importlib import import_module
module_name = "17_letter_combinations_of_a_phone_number"

def test_17():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    digits = "23"
    Output = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

    assert func(digits) == Output
