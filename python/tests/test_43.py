
import inspect
from importlib import import_module
module_name = "43_multiply_strings"

def test_43():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    num1 = "123"
    num2 = "456"
    Output = "56088"

    assert func(num1, num2) == Output

    num1 = "0"
    num2 = "0"
    Output = "0"

    assert func(num1, num2) == Output
