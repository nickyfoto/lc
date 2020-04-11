
import inspect
from importlib import import_module
module_name = "285_inorder_successor_in_bst"

def test_285():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(root: 'TreeNode', p: 'TreeNode') -> 'TreeNode' == Output
