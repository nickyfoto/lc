
import inspect
from importlib import import_module
module_name = "889_construct_binary_tree_from_preorder_and_postorder_traversal"

from lcpy import build_root, null

def test_889():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    pre = [1,2,3]
    post = [2,3,1]
    l = [1,2,3]
    Output = build_root(l)
    root = func(pre, post)
    # print(root, Output)
    assert root == Output

    pre = [1,2,3]
    post = [3,2,1]
    l = [1,2,null,3]
    Output = build_root(l)
    root = func(pre, post)
    # print(root, Output)
    assert root == Output
    
    pre = [1,2,4,3]
    post = [4,2,3,1]
    l = [1,2,3,4]
    Output = build_root(l)
    root = func(pre, post)
    # print(root, Output)
    assert root == Output


    pre = [1,2,4,5,3]
    post = [4,5,2,3,1]
    l = [1,2,3,4,5]
    Output = build_root(l)
    root = func(pre, post)
    # print(root, Output)
    assert root == Output
    
    pre = [1,2,4,5,3,6]
    post = [4,5,2,6,3,1]
    l = [1,2,3,4,5,6]
    Output = build_root(l)
    root = func(pre, post)
    print(root, Output)
    assert root == Output


    # pre = [1,2,4,5,3,6,7]
    # post = [4,5,2,6,7,3,1]
    # l = [1,2,3,4,5,6,7]
    # Output = build_root(l)
    # assert func(pre, post) == Output

    # pre = [2,1]
    # post = [1,2]
    # l = [2, 1]
    # Output = build_root(l)
    # assert func(pre, post) == Output

    # pre = [3,4,1,2]
    # post = [1,4,2,3]
    # l = [3,4,2,1]
    # Output = build_root(l)
    # assert func(pre, post) == Output

    # pre = [3,2,5,4,1]
    # post = [5,1,4,2,3]
    # l = [3,2,null,5,4,null,null,1]
    # Output = build_root(l)
    # assert func(pre, post) == Output


    # pre = [1,10,2,4,3,9,5]
    # post = [4,2,10,9,5,3,1]
    # l = [1,10,3,2,null,9,5,4]
    # Output = build_root(l)
    # # print(func(pre, post), Output)
    # assert func(pre, post) == Output

    pre = [1,10,2,4,8,6,7,3,9,5]
    post = [7,6,8,4,2,10,9,5,3,1]
    l = [1,10,3,2,null,9,5,4,null,null,null,null,null,8,null,6,null,7]
    Output = build_root(l)
    # assert func(pre, post) == Output
    #my output [1,10,3,2,null,9,null,4,null,5,null,8,null,null,null,6,null,7]