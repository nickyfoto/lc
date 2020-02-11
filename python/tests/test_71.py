
import inspect
from importlib import import_module
module_name = "71_simplify_path"

def test_71():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    path = "/home/"
    Output = '/home'
    assert func(path) == Output

    path = "/../"
    Output = '/'
    assert func(path) == Output

    path = "/home//foo/"
    Output = "/home/foo"
    assert func(path) == Output

    path = "/a/./b/../../c/"
    Output = "/c"
    assert func(path) == Output

    path = "/a/../../b/../c//.//"
    Output = "/c"
    assert func(path) == Output

    path = "/a//b////c/d//././/.."
    Output = "/a/b/c"
    assert func(path) == Output

