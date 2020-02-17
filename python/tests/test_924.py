
import inspect
from importlib import import_module
module_name = "924_minimize_malware_spread"

def test_924():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    graph = [[1,1,0],[1,1,0],[0,0,1]]
    initial = [0,1]

    # assert func(graph, initial) == Output


    graph = [[1,0,0,0,0,0],
             [0,1,0,0,0,0],
             [0,0,1,0,0,0],
             [0,0,0,1,1,0],
             [0,0,0,1,1,0],
             [0,0,0,0,0,1]]
    initial = [5,0]
    Output = 0
    assert func(graph, initial) == Output
