
import inspect
from importlib import import_module
module_name = "74_search_a_2d_matrix"

def test_74():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    matrix = [
 [1,   3,  5,  7],
 [10, 11, 16, 20],
 [23, 30, 34, 50]
]
    target = 3
    Output = True
    assert func(matrix, target) == Output

    matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
    ]
    target = 13
    Output = False
    assert func(matrix, target) == Output

    matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
    ]
    target = 100
    Output = False
    assert func(matrix, target) == Output

    matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
    ]
    target = 50
    Output = True
    assert func(matrix, target) == Output


    matrix = [[1],[3]]
    target = 3
    Output = True
    assert func(matrix, target) == Output