
import inspect
from importlib import import_module
module_name = "1281_subtract_the_product_and_sum_of_digits_of_an_integer"

def test_1281():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    n = 234
    Output = 15 

    assert func(n) == Output
    n = 4421
    Output = 21
    assert func(n) == Output