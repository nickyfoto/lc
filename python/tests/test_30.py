
import inspect
from importlib import import_module
module_name = "30_substring_with_concatenation_of_all_words"

def test_30():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    s = "barfoothefoobarman"
    words = ["foo","bar"]
    Output = [0, 9]
    assert func(s, words) == Output

    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","word"]
    Output = []
    assert func(s, words) == Output

    s = "barfoofoobarthefoobarman"
    words = ["bar","foo","the"]
    Output = [6,9,12]
    assert func(s, words) == Output

    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","good"]
    Output = [8]
    assert func(s, words) == Output

    s = "foobarfoobar"
    words = ["foo","bar"]
    Output = [0,3,6]
    assert func(s, words) == Output

    s = "aaaaaaaa"
    words = ["aa","aa","aa"]
    Output = [0,1,2]
    assert func(s, words) == Output


    s = "barfoothexfoobarman"
    words = ["foo","bar"]
    Output = [0, 10]
    assert func(s, words) == Output