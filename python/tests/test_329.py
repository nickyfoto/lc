
import inspect
from importlib import import_module
module_name = "329_longest_increasing_path_in_a_matrix"

def test_329():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    matrix = [
                [9,9,4],
                [6,6,8],
                [2,1,1]
                ] 
    Output = 4 
    

    assert func(matrix) == Output

    matrix = [
     [3,4,5],
     [3,2,6],
     [2,2,1]
    ] 
    Output = 4 
    assert func(matrix) == Output
