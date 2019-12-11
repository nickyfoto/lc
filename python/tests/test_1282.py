
import inspect
from importlib import import_module
module_name = "1282_group_the_people_given_the_group_size_they_belong_to"

def test_1282():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    
    groupSizes = [3,3,3,3,3,1,3]
    Output = [[5],[0,1,2],[3,4,6]]
    assert func(groupSizes) == Output

    groupSizes = [2,1,3,3,3,2]
    Output = [[1],[0,5],[2,3,4]]
    assert func(groupSizes) == Output