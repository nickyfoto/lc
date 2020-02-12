
import inspect
from importlib import import_module
module_name = "72_edit_distance"

def test_72():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    word1 = "horse"
    word2 = "ros"
    Output = 3

    assert func(word1, word2) == Output

    word1 = "intention"
    word2 = "execution"
    Output = 5
    assert func(word1, word2) == Output
