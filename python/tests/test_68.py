
import inspect
from importlib import import_module
module_name = "68_text_justification"

def test_68():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

#     words = ["This", "is", "an", "example", "of", "text", "justification."]
#     maxWidth = 16
#     Output = [
# "This    is    an",
# "example  of text",
# "justification.  "
# ]
#     # assert func(words, maxWidth) == Output

#     words = ["What","must","be","acknowledgment","shall","be"]
#     maxWidth = 16
#     Output = [
# "What   must   be",
# "acknowledgment  ",
# "shall be        "
# ]
#     # assert func(words, maxWidth) == Output




#     words = \
# ["Science","is","what","we","understand","well","enough","to","explain",
# "to","a","computer.","Art","is","everything","else","we","do"]
#     maxWidth = 20
#     Output = [
# "Science  is  what we",
# "understand      well",
# "enough to explain to",
# "a  computer.  Art is",
# "everything  else  we",
# "do                  "
# ]
#     assert func(words, maxWidth) == Output

    words = ["Here","is","an","example","of","text","justification."]
    maxWidth = 14
    Output = None
    assert func(words, maxWidth) == Output
