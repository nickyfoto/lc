
import inspect
from importlib import import_module
module_name = "253_meeting_rooms_ii"

def test_253():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(intervals) == Output
