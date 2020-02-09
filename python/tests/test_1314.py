
import inspect
from importlib import import_module
module_name = "1314_matrix_block_sum"

def test_1314():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    mat = [ [1,2,3],
            [4,5,6],
            [7,8,9]]
    K = 1
    Output = [[12,21,16],[27,45,33],[24,39,28]]
    

    assert func(mat, K) == Output
