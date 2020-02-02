
import inspect
from importlib import import_module
module_name = "32_longest_valid_parentheses"

def test_32():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    s = ")()())"
    Output = 4
    assert func(s) == Output

    s = "(()"
    Output = 2
    assert func(s) == Output

    s = "()()"
    Output = 4
    assert func(s) == Output

    s = "()())()"
    Output = 4
    assert func(s) == Output


    s = "()())()()()()"
    Output = 8
    assert func(s) == Output

    s = "()())"
    Output = 4
    assert func(s) == Output


    s = "()(()"
    Output = 2
    assert func(s) == Output
    
    s = "(()()"
    Output = 4
    assert func(s) == Output
    

    s = "(()(((()"
    Output = 2
    assert func(s) == Output

    s = "()(())"
    Output = 6
    assert func(s) == Output

