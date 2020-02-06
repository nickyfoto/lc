
import inspect
from importlib import import_module
module_name = "1268_search_suggestions_system"

def test_1268():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    products = ["mobile","mouse","moneypot","monitor","mousepad"]
    searchWord = "mouse"
    Output = [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
    assert func(products, searchWord) == Output

    products = ["havana"]
    searchWord = "havana"
    Output = [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
    assert func(products, searchWord) == Output

    products = ["bags","baggage","banner","box","cloths"]
    searchWord = "bags"
    Output = [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
    assert func(products, searchWord) == Output

    products = ["havana"]
    searchWord = "tatiana"
    Output = [[],[],[],[],[],[],[]]
    assert func(products, searchWord) == Output