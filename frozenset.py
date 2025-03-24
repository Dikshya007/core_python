"""
A frozenset is an immutable version of a set in Python. It allows you to add non-mutable properties
 to all basic data types and collection data structures. Unlike a regular set, once a frozenset is created,
   its elements cannot be changed (no adding or removing elements).
   Syntax:
   variable = frozenset(iterable)
"""
set1={1,2,3,4,6}
print(set1)
set2=frozenset(set1)
print(set2)
set1.add(10)
print(set1)
set2.add(12)
print(set2)