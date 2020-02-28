
import inspect
from importlib import import_module
module_name = "518_coin_change_2"

def test_518():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(amount, coins) == Output
