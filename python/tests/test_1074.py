
import inspect
from importlib import import_module
module_name = "1074_number_of_submatrices_that_sum_to_target"

def test_1074():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    
    matrix = [[0,1,0],[1,1,1],[0,1,0]]
    target = 0
    Output = 4
    assert func(matrix, target) == Output
