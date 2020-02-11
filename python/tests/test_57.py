
import inspect
from importlib import import_module
module_name = "57_insert_interval"

def test_57():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    Output = [[1,5],[6,9]]
    assert func(intervals, newInterval) == Output


    intervals = [[1,5]]
    newInterval = [0,3]
    Output = [[0,5]]
    assert func(intervals, newInterval) == Output

    intervals = [[1,5]]
    newInterval = [2,3]
    Output = [[1,5]]
    assert func(intervals, newInterval) == Output

    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    Output = [[1,2],[3,10],[12,16]]
    assert func(intervals, newInterval) == Output