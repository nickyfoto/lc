
import inspect
from importlib import import_module
module_name = "1319_number_of_operations_to_make_network_connected"

def test_1319():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    n = 4
    connections = [[0,1],[0,2],[1,2]]
    Output = 1
    assert func(n, connections) == Output

    n = 6
    connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
    Output = 2
    assert func(n, connections) == Output

    n = 6
    connections = [[0,1],[0,2],[0,3],[1,2]]
    Output = -1
    assert func(n, connections) == Output

    n = 5
    connections = [[0,1],[0,2],[3,4],[2,3]]
    Output = 0
    assert func(n, connections) == Output

    n = 11
    connections = [[1,4],[0,3],[1,3],[3,7],[2,7],[0,1],[2,4],[3,6],[5,6],[6,7],[4,7],[0,7],[5,7]]
    Output = 3
    assert func(n, connections) == Output