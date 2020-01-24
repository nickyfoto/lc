
import inspect
from importlib import import_module
module_name = "4_median_of_two_sorted_arrays"

def test_4():

    m = import_module(module_name)  
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]
    func = getattr(s, fn)

    
    nums1 = [1, 3]
    nums2 = [2]
    Output = 2.0
    assert func(nums1, nums2) == Output

    nums1 = [1,2,3,4]
    nums2 = [0]
    Output = 2.0
    assert func(nums1, nums2) == Output

    nums1 = [0]
    nums2 = [1,2,3,4]
    Output = 2.0
    assert func(nums1, nums2) == Output

    nums1 = [10]
    nums2 = [1,2,3,4]
    Output = 3.0
    assert func(nums1, nums2) == Output

    nums1 = [1, 2]
    nums2 = [3, 4]
    Output = 2.5
    assert func(nums1, nums2) == Output



    nums1 = [0]
    nums2 = [1,2,3,4,5]
    Output = 2.5
    assert func(nums1, nums2) == Output


    nums1 = [6]
    nums2 = [1,2,3,4,5]
    Output = 3.5
    assert func(nums1, nums2) == Output
    
    
    nums1 = [1,2,3,4,5]
    nums2 = [2,2,4,6,8]
    Output = 3.5
    assert func(nums1, nums2) == Output

    nums1 = []
    nums2 = [2,3]
    Output = 2.5
    assert func(nums1, nums2) == Output

    nums1 = [1]
    nums2 = [1]
    Output = 1
    assert func(nums1, nums2) == Output


    nums1 = [1,2]
    nums2 = [-1,3]
    Output = 1.5
    assert func(nums1, nums2) == Output

    nums1 = [2,2,2]
    nums2 = [2,2,2,2]
    Output = 2
    assert func(nums1, nums2) == Output


    nums1 = [3,5]
    nums2 = [1,2,4,6]
    Output = 3.5
    assert func(nums1, nums2) == Output