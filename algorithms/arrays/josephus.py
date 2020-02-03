"""
There are people sitting in a circular fashion,
print every third member while removing them,
the next counter starts immediately after the member is removed.
Print till all the members are exhausted.

For example:
Input: consider 123456789 members sitting in a circular fashion,
Output: 369485271
"""

"""
circular 圆圈不回头
123456789 index result
12|456789 2     3
1245|789  4     6
124578|   6     9
12|578    2     4
1257|     4     8
12|7      2     5










"""


def josephus(int_list, skip):
    skip = skip - 1  # list starts with 0 index
    idx = 0
    len_list = (len(int_list))
    while len_list > 0:
        idx = (skip + idx) % len_list  # hash index to every 3rd
        yield int_list.pop(idx)
        len_list -= 1
