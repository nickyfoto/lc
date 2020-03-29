
import inspect
from importlib import import_module
module_name = "1143_longest_common_subsequence"

def test_1143():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(text1: str, text2: str) -> int == Output
