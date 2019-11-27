"""
pytest -svv test_1252.py
"""

exec(open('1252.cells-with-odd-values-in-a-matrix.py').read())


def test_1252():
    s = Solution()
    points = [[1,1],[3,4],[-1,0]]
    n = 2
    m = 3
    indices = [[0,1],[1,1]]
    assert s.oddCells(n, m, indices) == 6
    n = 2
    m = 2
    indices = [[1,1],[0,0]]
    assert s.oddCells(n, m, indices) == 0