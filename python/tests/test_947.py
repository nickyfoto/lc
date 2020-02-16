
import inspect
from importlib import import_module
module_name = "947_most_stones_removed_with_same_row_or_column"

def test_947():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    Output = 5
    assert func(stones) == Output
