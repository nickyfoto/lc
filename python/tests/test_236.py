
import inspect
from importlib import import_module
module_name = "236_lowest_common_ancestor_of_a_binary_tree"

def test_236():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode' == Output
