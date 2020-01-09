
import inspect
from importlib import import_module
module_name = "1302_deepest_leaves_sum"
from lcpy import build_root, null
def test_1302():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)
    root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
    root = build_root(root)
    Output = 15
    assert func(root) == Output

    root = [50,null,54,98,6,null,null,null,34]
    root = build_root(root)
    Output = 34
    assert func(root) == Output