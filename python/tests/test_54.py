
import inspect
from importlib import import_module
module_name = "54_spiral_matrix"

def test_54():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    matrix = [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
        ]
    Output = [1,2,3,6,9,8,7,4,5]

    assert func(matrix) == Output

    matrix = [
 [1, 2, 3, 4],
 [5, 6, 7, 8],
 [9,10,11,12]
]

    Output = [1,2,3,4,8,12,11,10,9,5,6,7]
    assert func(matrix) == Output