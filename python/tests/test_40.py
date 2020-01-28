
import inspect
from importlib import import_module
module_name = "40_combination_sum_ii"

def test_40():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    candidates = [10,1,2,7,6,1,5]
    target = 8
    Output = [
                [1, 7],
                [1, 2, 5],
                [2, 6],
                [1, 1, 6]
                ]

    # assert func(candidates, target) == Output

    candidates = [2,5,2,1,2]
    target = 5
    Output = [
                [1,2,2],
                [5]
                ]

    assert func(candidates, target) == Output