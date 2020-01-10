
import inspect
from importlib import import_module
module_name = "145_binary_tree_postorder_traversal"
from lcpy import null, build_root
def test_145():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    root = [1,null,2,3]
    root = build_root(root)
    Output = [3,2,1]

    assert func(root) == Output
