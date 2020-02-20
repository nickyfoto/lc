
import inspect
from importlib import import_module
module_name = "63_unique_paths_ii"

def test_63():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(obstacleGrid) == Output
