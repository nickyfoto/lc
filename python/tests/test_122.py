
import inspect
from importlib import import_module
module_name = "122_best_time_to_buy_and_sell_stock_ii"

def test_122():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(prices) == Output
