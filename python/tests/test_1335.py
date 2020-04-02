
import inspect
from importlib import import_module
module_name = "1335_minimum_difficulty_of_a_job_schedule"

def test_1335():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    

    assert func(jobDifficulty, d) == Output
