# ============================================================
#   PES University · UE20CS901 — Python for Data Science
#   Study Notes: Days 5–6
#   Day 5 — Lists & Tuples
#   Day 6 — Dictionaries & Sets
# ============================================================


# ╔══════════════════════════════════════════════════════════╗
# ║         DAY 5 — LISTS & TUPLES                          ║
# ╚══════════════════════════════════════════════════════════╝

# ──────────────────────────────────────────
# SECTION 1 — LIST vs TUPLE (EXAM QUESTION — 3 papers!)
# ──────────────────────────────────────────

# Feature        List [ ]                  Tuple ( )
# Mutable?       ✅ Yes — can change        ❌ No — fixed forever
# Speed          Slower                    Faster
# Memory         More                      Less
# As dict key?   ❌ Not allowed (unhashable) ✅ Yes (hashable)
# Methods        Many: append, pop, sort…   Only count() & index()
# Use when       Data will change           Data is fixed (coords, dates)
#
# Memory Aid:
#   List  = Liquid  (flexible, can change shape)
#   Tuple = Stone   (fixed, cannot change)

# --- LIST — mutable ---
lst = [1, 2, 3]
lst[0] = 99             # ✅ allowed — lists can be modified
lst.append(4)           # ✅ adds element to the end
print(lst)              # → [99, 2, 3, 4]

# --- TUPLE — immutable ---
tup = (1, 2, 3)
# tup[0] = 99           # ❌ TypeError — tuples cannot be changed!
print(tup[0])           # ✅ reading is always fine

# Tuple as dict key — works because tuples are hashable
locations = {(10, 20): "Office", (30, 40): "Home"}
print(locations[(10, 20)])   # → "Office"

# List as dict key — fails because lists are unhashable
# bad = {[1, 2]: "x"}         # ❌ TypeError: unhashable type: 'list'


# ──────────────────────────────────────────
# SECTION 2 — LIST CREATION & ACCESS
# ──────────────────────────────────────────

# --- Creating lists ---
empty      = []                        # empty list
nums       = [1, 2, 3, 4, 5]           # list of ints
mixed      = [1, "hello", 3.14, True]  # lists can mix any types
nested     = [[1, 2], [3, 4], [5, 6]]  # list of lists (matrix)
zeros      = [0] * 5                   # → [0, 0, 0, 0, 0]  (repetition)
range_list = list(range(5))             # → [0, 1, 2, 3, 4]

# --- Accessing elements by index (0-based) ---
print(nums[0])          # → 1   first element
print(nums[-1])         # → 5   last element  (negative = count from end)
print(nums[1:4])        # → [2, 3, 4]  slice (stop is EXCLUSIVE)
print(nums[::-1])       # → [5, 4, 3, 2, 1]  REVERSED  (step = -1)

# --- Length & membership ---
print(len(nums))        # → 5
print(3 in nums)        # → True
print(99 not in nums)   # → True


# ──────────────────────────────────────────
# SECTION 3 — LIST METHODS (CRITICAL)
# ──────────────────────────────────────────

# --- Adding Elements ---
lst = [1, 2, 3]
lst.append(4)           # add ONE element to the END  → [1, 2, 3, 4]
lst.insert(0, 0)        # insert at specific INDEX    → [0, 1, 2, 3, 4]
lst.extend([5, 6])      # add MULTIPLE elements       → [0, 1, 2, 3, 4, 5, 6]
lst += [7, 8]           # same as extend              → [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(lst)

# --- Removing Elements — 4 ways! (EXAM QUESTION — Nov 2023) ---
#
# Method          Removes by       Returns         Raises error?
# del lst[i]      Index            Nothing         No
# lst.clear()     ALL elements     Nothing         No
# lst.remove(v)   First match      None            Yes, if value missing
# lst.pop(i)      Index (last)     The removed     Yes, if index invalid
#                 if no i given)

lst = [10, 20, 30, 20, 40]

# del — remove by index, returns nothing
del lst[1]              # removes value at index 1 (20) → [10, 30, 20, 40]
print(lst)

# pop — remove by index and RETURN the removed value
last  = lst.pop()       # no index = removes LAST element; last=40
first = lst.pop(0)      # removes index 0; first=10
print(lst)              # → [30, 20]

# remove — remove by VALUE (first occurrence only!)
lst = [10, 20, 30, 20]
lst.remove(20)          # removes the FIRST 20 → [10, 30, 20]
print(lst)

# clear — empty the entire list
lst.clear()             # lst = []
print(lst)

# --- Counting & Searching ---
# EXAM QUESTION: "How do you count occurrences in a list?"
lst = ["a", "b", "a", "c", "a"]

print(lst.count("a"))   # → 3  (counts how many times "a" appears)
print(lst.count("x"))   # → 0  (not found — returns 0, no error!)

print(lst.index("b"))   # → 1  (index of first occurrence)
# lst.index("x")        # ❌ ValueError — use .count() first to check!

# Counter — count ALL elements at once
from collections import Counter
print(Counter(lst))     # → Counter({'a': 3, 'b': 1, 'c': 1})

# --- Reversing & Copying ---
lst = [1, 2, 3]

lst.reverse()           # reverses IN-PLACE → [3, 2, 1]  (modifies original)
print(lst)

print(lst[::-1])        # creates a NEW reversed list (original untouched)

copy1 = lst.copy()      # shallow copy (recommended)
copy2 = lst[:]          # slicing trick — same result
copy3 = list(lst)       # constructor — same result


# ──────────────────────────────────────────
# SECTION 4 — sort() vs sorted() (EXAM QUESTION — 2 papers!)
# ──────────────────────────────────────────

# Feature          sort()                sorted()
# Type             Method (lst.sort())   Built-in (sorted(lst))
# Modifies orig?   ✅ Yes (in-place)     ❌ No (new list returned)
# Returns          None                  The sorted list
# Works on         Lists only            Any iterable (list, tuple, str)

nums = [3, 1, 4, 1, 5, 9, 2]

# sort() — modifies the list in-place, returns None
nums.sort()
print(nums)             # → [1, 1, 2, 3, 4, 5, 9]  (original changed!)

# sorted() — returns a NEW sorted list, original untouched
nums = [3, 1, 4, 1, 5, 9, 2]
new_list = sorted(nums)
print(new_list)         # → [1, 1, 2, 3, 4, 5, 9]
print(nums)             # → [3, 1, 4, 1, 5, 9, 2]  ← unchanged!

# Descending order (both support reverse=True)
print(sorted(nums, reverse=True))   # → [9, 5, 4, 3, 2, 1, 1]

# Custom sort key — sort by string length
words = ["banana", "apple", "fig"]
print(sorted(words, key=lambda x: len(x)))   # → ['fig', 'apple', 'banana']

# Sort list of dicts by a specific field
people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
print(sorted(people, key=lambda p: p["age"]))
# → [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}]


# ──────────────────────────────────────────
# SECTION 5 — LIST COMPREHENSIONS
# ──────────────────────────────────────────

# List comprehension = one-line shortcut to build a list
# Pattern: [expression  for item in iterable  if condition]
#
# Equivalent verbose version:
#   result = []
#   for item in iterable:
#       if condition:
#           result.append(expression)

# --- Squares of 0–9 ---
squares = [x**2 for x in range(10)]
print(squares)   # → [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# --- Even numbers from 1–20 (with if filter) ---
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)     # → [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# --- Word lengths ---
words = ["apple", "banana", "fig"]
lengths = [len(w) for w in words]
print(lengths)   # → [5, 6, 3]

# --- Conditional expression (ternary) inside comprehension ---
nums2 = [1, 2, 3, 4, 5]
parity = ["even" if x % 2 == 0 else "odd" for x in nums2]
print(parity)    # → ['odd', 'even', 'odd', 'even', 'odd']

# --- Nested comprehension: flatten a 2D matrix ---
matrix = [[1, 2, 3], [4, 5, 6]]
flat = [val for row in matrix for val in row]
print(flat)      # → [1, 2, 3, 4, 5, 6]

# ⚠️  When NOT to use comprehensions:
#   If logic is complex (multiple conditions, nested ifs, side-effects)
#   use a regular for loop — readability matters more than cleverness!


# ──────────────────────────────────────────
# SECTION 6 — TUPLES
# ──────────────────────────────────────────

# --- Creating tuples ---
empty_tup = ()              # empty tuple
single    = (5,)            # ⚠️ MUST have comma! (5) is just an int, not a tuple
tup       = (1, 2, 3)
no_parens = 1, 2, 3         # parentheses are optional — still a tuple
print(type(no_parens))      # → <class 'tuple'>

# --- Access (same as lists) ---
print(tup[0])               # → 1
print(tup[-1])              # → 3
print(tup[0:2])             # → (1, 2)

# --- Tuple has only 2 methods ---
print(tup.count(2))         # → 1  (count occurrences)
print(tup.index(3))         # → 2  (index of first match)

# --- Tuple unpacking (very Pythonic!) ---
point = (10, 20)
x, y = point               # x=10, y=20 (assigns each element)
print(x, y)

# --- Swap two variables (classic Pythonic trick) ---
a, b = 5, 10
a, b = b, a                # now a=10, b=5 (no temp variable needed!)
print(a, b)

# --- Functions returning multiple values use tuples ---
def stats(lst):
    return min(lst), max(lst), sum(lst) / len(lst)

low, high, avg = stats([3, 7, 2, 8, 5])
print(low, high, avg)       # → 2 8 5.0


# ──────────────────────────────────────────
# SECTION 7 — REUSABLE LIST PATTERNS
# ──────────────────────────────────────────

# --- Pattern: Analyze Numbers (min/max/sum/avg) ---
def analyze_numbers(numbers):
    """Return a dict of statistics for a list of numbers."""
    if not numbers:
        return None
    return {
        'min':   min(numbers),
        'max':   max(numbers),
        'sum':   sum(numbers),
        'avg':   sum(numbers) / len(numbers),
        'count': len(numbers)
    }

print(analyze_numbers([10, 20, 30, 40, 50]))

# --- Pattern: Filter + Map (Mar 2024) ---
def squares_of_evens(numbers):
    """Manual loop: squares of all even numbers."""
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n ** 2)
    return result

def squares_of_evens_v2(numbers):
    """Using filter() + map() — more functional style."""
    evens = filter(lambda x: x % 2 == 0, numbers)
    return list(map(lambda x: x**2, evens))

print(squares_of_evens([1, 2, 3, 4, 5, 6]))    # → [4, 16, 36]
print(squares_of_evens_v2([1, 2, 3, 4, 5, 6])) # → [4, 16, 36]

# --- Pattern: Flatten Nested List (Aug 2021) ---
def flatten(nested_list):
    """Convert [[1,2,3], 4, [5,6]] → [1,2,3,4,5,6]"""
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(item)   # spread the sub-list into flat
        else:
            flat.append(item)   # single value — just append
    return flat

data = [[20, 25, 30], 24, [56, 8], 9, [7, 5]]
f = flatten(data)
print(f)                    # → [20, 25, 30, 24, 56, 8, 9, 7, 5]
print(min(f))               # → 5
print(sum(f) / len(f))      # average of all values

# --- Pattern: Frequency Counter ---
def count_frequencies(items):
    """Count how many times each item appears."""
    freq = {}
    for item in items:
        if item in freq:
            freq[item] += 1     # already seen — increment
        else:
            freq[item] = 1      # first time — initialize to 1
    return freq

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
freq = count_frequencies(words)
print(freq)                 # → {'apple': 3, 'banana': 2, 'cherry': 1}

# Find the most frequent element
most = max(freq, key=freq.get)   # key=freq.get → compare by values
print(f"Most frequent: {most}")  # → apple

# --- Pattern: Longest Consecutive Sequence (Oct 2024) ---
def longest_consecutive(numbers):
    """Find the length of the longest run of consecutive integers."""
    num_set = set(numbers)   # convert to set for O(1) lookups
    longest = 0
    for n in num_set:
        # Only start counting from the BEGINNING of a sequence
        if (n - 1) not in num_set:
            current = n
            length  = 1
            while (current + 1) in num_set:
                current += 1
                length  += 1
            longest = max(longest, length)
    return longest

print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # → 4  (1,2,3,4)


# ──────────────────────────────────────────
# QUICK REFERENCE CHEATSHEET — LISTS
# ──────────────────────────────────────────

# ADD                          REMOVE
# lst.append(x)  1 to end      lst.pop()     last (returns it)
# lst.insert(i,x) at index     lst.pop(i)    by index (returns it)
# lst.extend([…]) multiple     lst.remove(x) by value (first match)
#                              lst.clear()   everything
#                              del lst[i]    by index

# SEARCH                       SORT
# lst.count(x)   occurrences   lst.sort()      in-place, None returned
# lst.index(x)   first index   sorted(lst)     new list, original safe
# x in lst       True/False    lst.reverse()   in-place
#                              lst[::-1]       new reversed list

# ⚠️  Common Traps:
#   (5) is an int  — use (5,) for a single-element tuple
#   lst.sort() returns None, not the sorted list!
#   lst.remove(x) raises ValueError if x not in list
#   Modifying a list while iterating it can skip elements


# ╔══════════════════════════════════════════════════════════╗
# ║         DAY 6 — DICTIONARIES & SETS                     ║
# ╚══════════════════════════════════════════════════════════╝

# ──────────────────────────────────────────
# SECTION 1 — DICTIONARIES
# ──────────────────────────────────────────

# A dictionary stores key → value pairs.
# Think of it as a phone book: name (key) maps to phone number (value).
# Lookups are extremely fast — O(1) time complexity.
# Keys must be IMMUTABLE (str, int, tuple) — lists cannot be keys.

# --- Creating a dict ---
empty  = {}                                  # empty dict
prices = {"apple": 100, "banana": 50, "cherry": 200}
prices2 = dict(apple=100, banana=50)         # using dict() constructor

# --- Accessing values ---
print(prices["apple"])          # → 100
# print(prices["mango"])        # ❌ KeyError — key doesn't exist!

# Safe access with .get() — returns None (or default) instead of crashing
print(prices.get("mango"))      # → None  (no error)
print(prices.get("mango", 0))   # → 0     (use 0 as default)

# --- Length & membership (checks KEYS only!) ---
print(len(prices))              # → 3
print("apple" in prices)        # → True   (checks if "apple" is a KEY)
print(100 in prices)            # → False  (100 is a VALUE, not a key!)


# ──────────────────────────────────────────
# SECTION 2 — DICTIONARY OPERATIONS
# ──────────────────────────────────────────

# --- Add / Update (EXAM QUESTION — July 2021) ---
# "How to change the value associated with a key in a dictionary?"
prices = {"apple": 100, "banana": 50}

prices["apple"] = 120           # UPDATE existing key's value
prices["mango"] = 80            # ADD a new key (same syntax as update!)

# Update multiple keys at once
prices.update({"apple": 150, "orange": 90})
prices.update(grape=75)         # keyword argument form
print(prices)

# --- Delete ---
del prices["banana"]            # remove by key (KeyError if missing)
val = prices.pop("apple")       # remove by key and RETURN its value
val = prices.pop("missing", 0)  # safe pop — returns 0 if key missing
prices.popitem()                # remove and return the LAST inserted pair
prices.clear()                  # empty the entire dictionary

# --- Iterating (MOST IMPORTANT dict skill) ---
prices = {"apple": 100, "banana": 50, "cherry": 200}

for key in prices:                  # iterate KEYS (default)
    print(key)

for val in prices.values():         # iterate VALUES
    print(val)

for key, val in prices.items():     # iterate KEY-VALUE pairs (most common)
    print(f"{key}: {val}")

# --- Aggregations on a dict ---
print(sum(prices.values()))                     # total of all values → 350
print(max(prices, key=prices.get))              # key with highest value → 'cherry'
print(min(prices, key=prices.get))              # key with lowest value  → 'banana'

# Sort by value (returns list of tuples)
print(sorted(prices.items(), key=lambda x: x[1]))
# → [('banana', 50), ('apple', 100), ('cherry', 200)]


# ──────────────────────────────────────────
# SECTION 3 — NESTED DICTIONARIES (BILLING PATTERN)
# ──────────────────────────────────────────

# Nested dict = a dictionary whose VALUES are also dictionaries
# Used in every billing/inventory question (6+ exam papers!)

# --- Pattern: Computer Assembly Bill (July 2021) ---
price_list = {
    "HDD":       {"1TB": 5000,  "2TB": 7500,  "4TB": 10000},
    "RAM":       {"8GB": 4000,  "16GB": 6000},
    "Processor": {"I5": 15000,  "I7": 18000}
}

def calculate_bill(price_list, choices, gst_rate=0.12):
    """
    choices = {"HDD": "1TB", "RAM": "16GB", "Processor": "I5"}
    Looks up each choice in the nested price_list, sums, adds GST.
    """
    subtotal = 0
    for item, choice in choices.items():
        if item in price_list and choice in price_list[item]:
            subtotal += price_list[item][choice]  # nested dict access
    gst   = subtotal * gst_rate
    total = subtotal + gst
    return {'subtotal': subtotal, 'gst': gst, 'total': total}

choices = {"HDD": "1TB", "RAM": "16GB", "Processor": "I5"}
print(calculate_bill(price_list, choices))
# → {'subtotal': 26000, 'gst': 3120.0, 'total': 29120.0}

# --- Pattern: Inventory Management (Oct 2024) ---
inventory = {
    "Pen":    {"qty": 100, "price": 10},
    "Pencil": {"qty": 200, "price": 5},
    "Eraser": {"qty": 50,  "price": 8}
}

def total_value(inventory):
    """Total value = sum of qty × price for each item."""
    total = 0
    for name, details in inventory.items():
        total += details["qty"] * details["price"]
    return total

def add_item(inventory, name, qty, price):
    """Add a new item to inventory."""
    inventory[name] = {"qty": qty, "price": price}

def update_qty(inventory, name, new_qty):
    """Update quantity if item exists."""
    if name in inventory:
        inventory[name]["qty"] = new_qty

print(total_value(inventory))   # → 100×10 + 200×5 + 50×8 = 2400

# --- Pattern: Date Validation using dict (Mar 2024 Scan) ---
days_in_month = {
    "January": 31, "February": 28, "March": 31,
    "April":   30, "May":      31, "June":  30,
    "July":    31, "August":   31, "September": 30,
    "October": 31, "November": 30, "December":  31
}

def validate_date(month, day):
    """Return True if month and day form a valid date."""
    if month not in days_in_month:
        return False
    return 1 <= day <= days_in_month[month]

print(validate_date("January", 15))    # → True
print(validate_date("January", 32))    # → False
print(validate_date("February", 30))   # → False

# --- Pattern: Telephone Keypad (Nov 2023) ---
keypad = {
    '2': 'ABC', '3': 'DEF', '4': 'GHI',
    '5': 'JKL', '6': 'MNO', '7': 'PQRS',
    '8': 'TUV', '9': 'WXYZ'
}

# Build reverse mapping: letter → digit
letter_to_digit = {}
for digit, letters in keypad.items():
    for ch in letters:
        letter_to_digit[ch] = digit     # e.g. letter_to_digit['C'] = '2'

print(letter_to_digit['C'])   # → '2'
print(letter_to_digit['Z'])   # → '9'


# ──────────────────────────────────────────
# SECTION 4 — DICTIONARY COMPREHENSIONS
# ──────────────────────────────────────────

# Pattern: {key_expr: value_expr for item in iterable if condition}

# Word → length mapping
words = ["apple", "banana", "cherry"]
lens = {w: len(w) for w in words}
print(lens)             # → {'apple': 5, 'banana': 6, 'cherry': 6}

# Number → its square
squares = {x: x**2 for x in range(1, 6)}
print(squares)          # → {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filter: only include words shorter than 6 characters
short = {w: len(w) for w in words if len(w) < 6}
print(short)            # → {'apple': 5}

# Swap keys and values (invert a dict)
prices = {"apple": 100, "banana": 50}
swapped = {v: k for k, v in prices.items()}
print(swapped)          # → {100: 'apple', 50: 'banana'}


# ──────────────────────────────────────────
# SECTION 5 — SETS
# ──────────────────────────────────────────

# A set is an UNORDERED collection of UNIQUE elements.
# Primary uses:
#   1. Remove duplicates instantly
#   2. Fast O(1) membership checks
#   3. Set math: union, intersection, difference

# --- Creating sets ---
empty_set = set()                    # ⚠️  {} creates a DICT, not a set!
s  = {1, 2, 3}
s2 = set([1, 2, 2, 3, 3])           # duplicates are automatically removed
print(s2)                            # → {1, 2, 3}

# --- Add / Remove ---
s.add(4)                             # add element → {1, 2, 3, 4}
s.remove(2)                          # remove — raises KeyError if missing!
s.discard(99)                        # remove — silently ignores if missing ✅
print(s)

# --- Membership (O(1) — much faster than list search!) ---
print(3 in s)                        # → True
print(99 in s)                       # → False

# --- Length ---
print(len(s))

# --- Set Math Operations ---
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)    # Union:             {1, 2, 3, 4, 5, 6}  (all elements)
print(A & B)    # Intersection:      {3, 4}               (common elements)
print(A - B)    # Difference:        {1, 2}               (in A but not B)
print(A ^ B)    # Symmetric diff:    {1, 2, 5, 6}         (in either, not both)

# Method equivalents (same results)
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))

# --- Common use cases ---

# 1. Remove duplicates from a list (order not preserved!)
nums = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(nums))
print(unique)            # → [1, 2, 3, 4]  (order may vary)

# 2. Check if all elements in a list are unique
def all_unique(lst):
    return len(lst) == len(set(lst))   # if set is smaller, duplicates exist

print(all_unique([1, 2, 3]))    # → True
print(all_unique([1, 2, 2]))    # → False

# 3. Find common elements between two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = list(set(list1) & set(list2))
print(common)            # → [3, 4]


# ──────────────────────────────────────────
# SECTION 6 — SET-BASED ALGORITHMS (EXAM PATTERNS)
# ──────────────────────────────────────────

# --- Pattern: Happy Number — Cycle Detection (Mar 2024 Scan) ---
# EXAM QUESTION: "Write isHappy(n): replace n by sum of squares of digits,
# repeat until 1 (happy) or a cycle is detected (not happy)."

def digit_squares_sum(n):
    """Helper: sum of the squares of each digit of n."""
    total = 0
    while n > 0:
        digit  = n % 10         # extract last digit
        total += digit ** 2     # square it and add
        n    //= 10             # remove last digit
    return total

def is_happy(n):
    """Return True if n is a happy number, False if it cycles."""
    seen = set()                # track every value we've processed
    while n != 1:
        if n in seen:           # O(1) lookup — we've been here before!
            return False        # cycle detected → not happy
        seen.add(n)
        n = digit_squares_sum(n)
    return True                 # reached 1 → happy!

print(is_happy(19))    # → True  (19→82→68→100→1)
print(is_happy(4))     # → False (4→16→37→58→89→145→42→20→4 cycle!)

# --- Pattern: Longest Consecutive Sequence (Oct 2024) ---
# Set allows checking (n-1) and (n+1) in O(1) — much faster than list search

def longest_consecutive(numbers):
    """Find the length of the longest run of consecutive integers."""
    num_set = set(numbers)      # O(1) lookups instead of O(n)
    longest = 0
    for n in num_set:
        # Only start counting from the BEGINNING of a new sequence
        # (if n-1 exists, n is not a start — skip it)
        if (n - 1) not in num_set:
            current = n
            length  = 1
            while (current + 1) in num_set:   # keep extending sequence
                current += 1
                length  += 1
            longest = max(longest, length)
    return longest

print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # → 4  (1, 2, 3, 4)


# ──────────────────────────────────────────
# QUICK REFERENCE CHEATSHEET — DICT & SET
# ──────────────────────────────────────────

# DICT                              SET
# d[k] = v     add/update           s.add(x)         add
# d.get(k)     safe access          s.remove(x)      raises error if missing
# d.get(k, def) with default        s.discard(x)     silent if missing
# d.update({}) multiple updates     A | B   union
# del d[k]     delete               A & B   intersection
# d.pop(k)     delete + return      A - B   difference
# d.keys()     key view             A ^ B   symmetric difference
# d.values()   value view           len(s)  count
# d.items()    key-value pair view  x in s  O(1) membership check
# k in d       True/False (keys!)
#
# ⚠️  Common Traps:
#   {} creates a DICT — use set() for an empty set
#   k in d checks KEYS, not values
#   Dict keys must be hashable (immutable types only)
#   Sets are unordered — don't rely on iteration order
#   set.remove() raises KeyError if missing — use discard() for safety

# ──────────────────────────────────────────
# WHEN TO USE EACH DATA STRUCTURE
# ──────────────────────────────────────────

# List   → ordered sequence, allows duplicates, need index access
# Tuple  → fixed data (coordinates, RGB), use as dict key, faster reads
# Dict   → key→value lookup, billing, inventory, frequency counting
# Set    → uniqueness check, fast membership test, remove duplicates,
#           cycle detection, finding common/different elements

# ============================================================
# End of Days 5–6 Notes — Good luck!
# ============================================================
