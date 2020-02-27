
import inspect
from importlib import import_module
module_name = "1239_maximum_length_of_a_concatenated_string_with_unique_characters"

def test_1239():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    arr = ["un", "iq", "ue"]
    Output = 4
    assert func(arr) == Output

    arr = ["cha","r","act","ers"]
    Output = 6
    assert func(arr) == Output

    arr = ["abcdefghijklmnopqrstuvwxyz"]
    Output = 26
    assert func(arr) == Output

    arr = ["jnfbyktlrqumowxd","mvhgcpxnjzrdei"]
    Output = 16
    assert func(arr) == Output

    arr = ["qrlkpcohtvzemiuf","wkiyvbfjd","jniwbdrqme"]
    Output = 16
    assert func(arr) == Output