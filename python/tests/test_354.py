
import inspect
from importlib import import_module
module_name = "354_russian_doll_envelopes"

def test_354():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    envelopes = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
    Output = 5

    assert func(envelopes) == Output
