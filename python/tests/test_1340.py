
import inspect
from importlib import import_module
module_name = "1340_jump_game_v"

def test_1340():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    arr = [6,4,14,6,8,13,9,7,10,6,12]
    d = 2    
    Output = 4
    assert func(arr, d) == Output
