
import inspect
from importlib import import_module
module_name = "6_zigzag_conversion"

def test_6():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    s = "ABAB"
    numRows = 2
    Output = "AABB"
    assert func(s, numRows) == Output

    s = "PAYPALISHIRING"
    numRows = 3
    Output = "PAHNAPLSIIGYIR"

    assert func(s, numRows) == Output


    s = "PAYPALISHIRING"
    numRows = 4
    Output = "PINALSIGYAHRPI"

    assert func(s, numRows) == Output

