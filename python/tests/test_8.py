
import inspect
from importlib import import_module
module_name = "8_string_to_integer_atoi"

def test_8():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    s = "42"
    Output = 42
    assert func(s) == Output

    s = "4193 with words"
    Output = 4193
    assert func(s) == Output

    s = "words and 987"
    Output = 0
    assert func(s) == Output

    s = "    -42"
    Output = -42
    assert func(s) == Output

    s = "-91283472332"
    Output = -2147483648
    assert func(s) == Output

    s = "3.14159"
    Output = 3
    assert func(s) == Output

    s = "  -0012a42"
    Output = -12
    assert func(s) == Output

    s = ".1"
    Output = 0
    assert func(s) == Output

    s = "2147483648"
    Output = 2147483647
    assert func(s) == Output
