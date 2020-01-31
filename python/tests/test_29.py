
import inspect
from importlib import import_module
module_name = "29_divide_two_integers"

def test_29():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    dividend = 10
    divisor = 3
    Output = 3
    assert func(dividend, divisor) == Output

    dividend = 7
    divisor = -3
    Output = -2
    assert func(dividend, divisor) == Output

    # dividend = -2147483648
    # divisor = 1
    # Output = -2147483648
    # assert func(dividend, divisor) == Output

    # dividend = 15
    # divisor = 3
    # Output = 5
    # assert func(dividend, divisor) == Output

    dividend = 2147483647
    divisor = 2
    Output = 1073741823
    assert func(dividend, divisor) == Output
