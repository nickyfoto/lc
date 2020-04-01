
import inspect
from importlib import import_module
module_name = "1102_path_with_maximum_minimum_value"

def test_1102():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    A = [[5,4,5],[1,2,6],[7,4,6]]
    Output = 4
    assert func(A) == Output

    A = [[2,2,1,2,2,2],[1,2,2,2,1,2]]
    Output = 2
    assert func(A) == Output

    A = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
    Output = 3
    assert func(A) == Output

    A = [[0,1,0,0,0,1],[0,1,1,0,0,0],[0,0,1,1,0,1],[0,1,1,1,1,0],[1,1,1,1,1,1]]
    Output = 0
    assert func(A) == Output

    A = [[2,5,5,4,3,0,2],
         [1,5,3,1,2,5,5],
         [3,3,3,4,3,3,4],
         [5,5,2,5,2,4,0],
         [3,1,3,3,5,4,5],
         [2,2,3,5,4,5,0],
         [1,0,3,2,4,5,4]]
    Output = 2
    assert func(A) == Output
