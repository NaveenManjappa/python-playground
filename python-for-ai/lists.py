from copy import copy, deepcopy
from typing import Any
from collections import deque
from functools import reduce

"""
lists.py

A compact, runnable guide to Python lists. Save and run this file to see
examples and printed results. Comments explain what's happening.

Author: GitHub Copilot
"""


# Helper to print section headers
def section(title: str):
  print("\n" + "=" * 8 + " " + title + " " + "=" * 8)


# 1) Creation and basic properties
section("Creation & Basic Properties")
# empty list
a = []
print("empty list a:", a, "len:", len(a))

# list with literals (heterogeneous)
b = [1, "two", 3.0, True]
print("heterogeneous b:", b)

# list from iterable (range, string, tuple)
from_iter = list(range(5))
print("from range(5):", from_iter)
chars = list("hello")
print("from string 'hello':", chars)
t = tuple((10, 20))
print("from tuple:", list(t))


# 2) Indexing and slicing
section("Indexing & Slicing")
L = ["zero", "one", "two", "three", "four", "five"]
print("L:", L)
print("L[0]:", L[0], "L[-1]:", L[-1])
print("slice L[1:4]:", L[1:4])   # stop is exclusive
print("slice with step L[::2]:", L[::2])
print("reverse with slice L[::-1]:", L[::-1])

# slice assignment modifies list (mutable)
M = [0, 1, 2, 3, 4, 5]
M[2:4] = ["a", "b", "c"]   # replacing two elements with three
print("slice assignment M:", M)


# 3) Iteration patterns
section("Iteration")
for i, val in enumerate(L):
  print(f"index {i} -> {val}")
# iterate two lists together
nums = [1, 2, 3]
names = ["a", "b", "c"]
for n, name in zip(nums, names):
  print("zip:", n, name)


# 4) Common list methods (mutating)
section("Common Mutating Methods")
lst = [3, 1, 4]
print("start:", lst)
lst.append(2)
print("append 2:", lst)
lst.extend([9, 8])
print("extend [9,8]:", lst)
lst.insert(1, "X")
print("insert 'X' at index 1:", lst)
lst.remove("X")
print("remove 'X':", lst)
popped = lst.pop()   # default pops last
print("pop() ->", popped, "list now:", lst)
popped0 = lst.pop(0) # pop by index
print("pop(0) ->", popped0, "list now:", lst)
lst.clear()
print("clear ->", lst)


# 5) Non-mutating helpers
section("Non-mutating Helpers")
data = [5, 2, 7, 2, 9]
print("data:", data)
print("count of 2:", data.count(2))
print("index of 7:", data.index(7))
print("sorted (new list):", sorted(data))
# sorted with key
words = ["apple", "Banana", "cherry"]
print("sorted case-insensitive:", sorted(words, key=str.lower))


# 6) In-place sort and reverse (mutate)
section("In-place sort & reverse")
arr = [3, 1, 4, 1, 5]
arr.sort()   # sorts in place
print("arr.sort() ->", arr)
arr.sort(reverse=True)
print("arr.sort(reverse=True) ->", arr)
arr.reverse()
print("arr.reverse() ->", arr)


# 7) List comprehensions (powerful and pythonic)
section("List Comprehensions")
nums = list(range(10))
# simple mapping
squares = [n * n for n in nums]
print("squares:", squares)
# with condition
evens = [n for n in nums if n % 2 == 0]
print("evens:", evens)
# nested comprehension (matrix flatten)
matrix = [[1, 2], [3, 4]]
flat = [x for row in matrix for x in row]
print("flatten matrix:", flat)
# with conditional inside comprehension
pairs = [(i, j) for i in range(3) for j in range(3) if i != j]
print("pairs excluding i==j:", pairs)


# 8) Nested lists and mutability (shallow vs deep copy)
section("Nested Lists & Copying")
nested = [[1, 2], [3, 4]]
shallow = list(nested)   # shallow copy: copies outer list only
deep = deepcopy(nested)
nested[0].append(99)
print("original nested after append:", nested)
print("shallow sees change:", shallow)  # shares inner lists
print("deep unaffected:", deep)


# 9) Aliasing vs copy (important mutability pitfall)
section("Aliasing vs Copy")
orig = [1, 2, 3]
alias = orig         # both names refer to same list
shallow_copy = orig.copy()
orig.append(4)
print("orig:", orig, "alias:", alias, "shallow_copy:", shallow_copy)


# 10) Unpacking / multiple assignment
section("Unpacking")
a, b, c = [10, 20, 30]
print("a,b,c:", a, b, c)
head, *middle, tail = [0, 1, 2, 3, 4]
print("head, middle, tail:", head, middle, tail)


# 11) Membership, concatenation, repetition
section("Membership & Operators")
L1 = [1, 2, 3]
L2 = [4, 5]
print("3 in L1:", 3 in L1)
print("concat L1+L2:", L1 + L2)
print("repeat L1*2:", L1 * 2)


# 12) Converting between types
section("Conversions")
s = "a,b,c"
print("split:", s.split(","))
print("join:", ",".join(["a", "b", "c"]))
print("list -> tuple:", tuple([1, 2, 3]))
print("list -> set (unique):", set([1, 2, 2, 3]))


# 13) Sorting with a key (complex objects)
section("Sorting with Key")
people = [{"name": "Alice", "age": 30},
      {"name": "Bob", "age": 25},
      {"name": "Carol", "age": 35}]
# sort by age without modifying original using sorted
by_age = sorted(people, key=lambda p: p["age"])
print("people sorted by age:", by_age)
# sort names by length
names = ["alex", "zoe", "benjamin"]
names.sort(key=len)
print("names sorted by length in-place:", names)


# 14) When lists are not appropriate
section("When not to use lists")
# - large-scale numeric computation: prefer numpy arrays for performance & memory
# - need immutable sequence: use tuple
nums_tuple = (1, 2, 3)
print("tuple example (immutable):", nums_tuple)


# 15) Common idioms / patterns
section("Idioms & Patterns")
# swapping
x, y = 1, 2
x, y = y, x
print("swap x,y:", x, y)

# remove duplicates while preserving order
items = [3, 1, 2, 3, 2]
seen = set()
unique_preserved = [x for x in items if not (x in seen or seen.add(x))]
print("unique_preserved:", unique_preserved)

# efficient queue using collections.deque (list pop(0) is O(n))
dq = deque([1, 2, 3])
dq.append(4)
dq.popleft()
print("deque example:", dq)


# 16) Performance notes (brief)
section("Performance Notes")
# - append & pop() at end: amortized O(1)
# - insert/pop(0) or delete in middle: O(n) because elements need shifting
# - membership test: O(n) for list, O(1) average for set/dict
print("append/pop end O(1) amortized; insert/pop(0) O(n); membership O(n)")

# 17) Example: filter, map, reduce
section("Functional Helpers")
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
filtered = list(filter(lambda x: x % 2 == 0, nums))
summed = reduce(lambda a, b: a + b, nums, 0)
print("map doubled:", doubled)
print("filter evens:", filtered)
print("reduce sum:", summed)


# 18) Safe element access: avoid IndexError
section("Safe access")
def safe_get(lst: list, idx: int, default: Any = None):
  return lst[idx] if -len(lst) <= idx < len(lst) else default

sample = [10, 20]
print("safe_get(sample,0):", safe_get(sample, 0))
print("safe_get(sample,5,'NA'):", safe_get(sample, 5, "NA"))


# 19) Misc tips & gotchas (short)
section("Tips & Gotchas")
print("- Don't use mutable default args (use None then create list inside function).")
print("- Differences between list.copy(), list(), copy.copy(), deepcopy() shown above.")
print("- Sorting mixed incomparable types (e.g., int and str) raises TypeError in Python 3.")


# 20) Small quick exercises (try by modifying file)
section("Exercises (try these)")
print("1) Write a comprehension to produce the first 10 prime numbers.")
print("2) Merge and deduplicate two lists while preserving order.")
print("3) Implement flattening of arbitrarily nested lists (recursive).")

# End
section("Done")
print("This file demonstrated common list operations. Edit and rerun to experiment.")