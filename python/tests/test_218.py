
import inspect
from importlib import import_module
module_name = "218_the_skyline_problem"

def test_218():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    Output = [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

    

    assert func(buildings) == Output
