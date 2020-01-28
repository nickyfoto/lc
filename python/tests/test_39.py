
import inspect
from importlib import import_module
module_name = "39_combination_sum"

def test_39():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    candidates = [2,3,5]
    target = 8
    Output = [
                [2,2,2,2],
                [2,3,3],
                [3,5]
                ]
    assert func(candidates, target) == Output
