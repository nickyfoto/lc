
import inspect
from importlib import import_module
module_name = "1306_jump_game_iii"

def test_1306():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    arr = [4,2,3,0,3,1,2]
    start = 5    
    Output = True
    assert func(arr, start) == Output

    arr = [4,2,3,0,3,1,2]
    start = 0
    Output = True
    assert func(arr, start) == Output

    arr = [3,0,2,1,2]
    start = 2
    Output = False
    assert func(arr, start) == Output