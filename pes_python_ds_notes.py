# ============================================================
#   PES University · UE20CS901 — Python for Data Science
#   Complete Study Notes: Days 1–4
#   All explanations as inline comments with runnable code
# ============================================================


# ╔══════════════════════════════════════════════════════════╗
# ║         DAY 1 — PYTHON BASICS                           ║
# ╚══════════════════════════════════════════════════════════╝

# ──────────────────────────────────────────
# SECTION 1 — WHAT IS PYTHON?
# ──────────────────────────────────────────

# Python is a programming language that reads your instructions
# line-by-line, top-to-bottom. It is:
#   • Easy to read  — looks almost like English
#   • Dynamically typed — no need to declare types like int x;
#   • Case-sensitive  — name ≠ Name ≠ NAME

# --- Case Sensitivity ---
name = "Alice"      # lowercase variable
Name = "Bob"        # Title-case — DIFFERENT variable!
NAME = "Carol"      # UPPERCASE — yet another different variable!

print(name)         # → Alice
print(Name)         # → Bob
print(NAME)         # → Carol

# --- Dynamic Typing ---
# The same variable can hold different types at different times
x = 10              # x is int now
print(type(x))      # → <class 'int'>

x = "hello"         # now x is str (same name, new type)
print(type(x))      # → <class 'str'>

x = [1, 2, 3]       # now x is list
print(type(x))      # → <class 'list'>


# ──────────────────────────────────────────
# SECTION 2 — VARIABLES
# ──────────────────────────────────────────

# A variable is a name that points to a value in memory.
# Think of it as a labeled box holding something.

# Naming Rules:
#   ✅ Letters, digits, underscore only  → my_age, x1, _temp
#   ❌ Cannot start with a digit         → 1name is invalid
#   ❌ Cannot use Python keywords        → class, if, for are reserved
#   ✅ Case-sensitive                    → name and Name are different

# --- Basic assignment ---
age = 25                # integer
name = "Rajesh"         # string
height = 5.9            # float (decimal number)
is_student = True       # boolean

# --- Multiple assignment on one line ---
a, b, c = 1, 2, 3      # a=1, b=2, c=3
x = y = z = 0           # all three set to 0 simultaneously

# --- Reassignment (overwrite a variable) ---
age = 26                # overwrites 25
age = age + 1           # now 27  (read old value, add 1, store back)
age += 1                # shorthand for age = age + 1  →  now 28


# ──────────────────────────────────────────
# SECTION 3 — DATA TYPES
# ──────────────────────────────────────────

# Python has 8 built-in data type categories:
#
#   Type      Example          Mutable?
#   int       42, -10, 0       ❌ Immutable
#   float     3.14, -2.5       ❌ Immutable
#   bool      True, False      ❌ Immutable
#   complex   3 + 4j           ❌ Immutable
#   str       "hello"          ❌ Immutable
#   list      [1, 2, 3]        ✅ Mutable
#   tuple     (1, 2, 3)        ❌ Immutable
#   dict      {"a": 1}         ✅ Mutable
#   set       {1, 2, 3}        ✅ Mutable
#
# Memory Aid — Immutable types: Int, Float, Bool, Str, Tuple  (IFBST)
# Mutable types: list, dict, set

# --- Immutable: string cannot be changed in-place ---
s = "hello"
# s[0] = "H"           # ❌ TypeError — strings are immutable!
s2 = "H" + s[1:]        # ✅ creates a NEW string "Hello"
print(s)                 # still "hello" — original unchanged
print(s2)                # "Hello"

# --- Immutable: tuple cannot be changed ---
t = (1, 2, 3)
# t[0] = 99             # ❌ TypeError — tuples are immutable!

# --- Mutable: list CAN be changed in-place ---
lst = [1, 2, 3]
lst[0] = 99              # ✅ allowed — modifies the same object
lst.append(4)            # ✅ adds element to the same list
print(lst)               # → [99, 2, 3, 4]

# --- Only immutable types can be dictionary keys ---
locations = {(10, 20): "Office"}    # ✅ tuple is hashable → valid key
# bad = {[1, 2]: "x"}              # ❌ TypeError: list is unhashable


# ──────────────────────────────────────────
# SECTION 4 — TYPE CASTING (CONVERSION)
# ──────────────────────────────────────────

# Type casting = converting a value from one type to another.
# Two kinds:
#   Implicit — Python does it silently (auto-promotion)
#   Explicit — Programmer does it manually using built-in functions

# --- Implicit (Automatic) casting ---
result = 5 + 2.0         # int + float → Python auto-promotes to float
print(result)             # → 7.0  (NOT 7!)
print(type(result))       # → <class 'float'>
# Promotion order: int → float → complex
# Python NEVER auto-converts str ↔ int (would lose meaning)

# --- Explicit casting ---

# TO int
print(int("42"))          # str → int: 42
print(int(3.99))          # float → int: 3  (TRUNCATES, does NOT round!)
print(int(True))          # bool → int: 1
print(int(False))         # bool → int: 0

# TO float
print(float(10))          # int → float: 10.0
print(float("3.14"))      # str → float: 3.14

# TO str
print(str(42))            # int → str: "42"
print(str(3.14))          # float → str: "3.14"

# TO bool
# Falsy values: 0, 0.0, "", [], {}, None, False
# Everything else is truthy
print(bool(0))            # → False
print(bool(42))           # → True
print(bool(""))           # → False  (empty string)
print(bool("hello"))      # → True   (non-empty string)
print(bool([]))           # → False  (empty list)

# TO list / tuple
print(list((1, 2, 3)))    # tuple → list: [1, 2, 3]
print(tuple([1, 2, 3]))   # list → tuple: (1, 2, 3)
print(list("abc"))         # str → list: ['a', 'b', 'c']

# ⚠️ Common traps:
# int(3.99) = 3, NOT 4 — Python truncates decimals, never rounds
# int("3.14") → ❌ ValueError! Use int(float("3.14")) = 3
# "5" + 3    → ❌ TypeError! Convert first: int("5") + 3 = 8

# --- Safe casting pattern (handles bad input gracefully) ---
def safe_int(value, default=0):
    """Convert value to int, return default if conversion fails."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

print(safe_int("42"))    # → 42
print(safe_int("abc"))   # → 0  (didn't crash)
print(safe_int(None))    # → 0


# ──────────────────────────────────────────
# SECTION 5 — OPERATORS
# ──────────────────────────────────────────

# 1. Arithmetic Operators
print(5 + 3)    # → 8   Addition
print(5 - 3)    # → 2   Subtraction
print(5 * 3)    # → 15  Multiplication
print(5 / 2)    # → 2.5 True division  (always returns float!)
print(5 // 2)   # → 2   Floor division (integer part only)
print(5 % 2)    # → 1   Modulus (remainder)
print(2 ** 3)   # → 8   Exponent (2 to the power 3)

# 2. Comparison Operators — always return True or False
print(5 == 5)   # → True   Equal to
print(5 != 3)   # → True   Not equal
print(5 > 3)    # → True   Greater than
print(5 < 3)    # → False  Less than
print(5 >= 5)   # → True   Greater or equal
print(5 <= 4)   # → False  Less or equal

# 3. Logical Operators
x = 5
print(x > 0 and x < 10)   # True  — both must be true
print(x == 0 or x == 5)   # True  — at least one must be true
print(not (x > 10))        # True  — reverses the result

# 4. Identity & Membership
print(x is None)           # False — checks same object in memory
print(x is not None)       # True
print("a" in "apple")      # True  — element exists in collection
print(5 not in [1, 2, 3])  # True  — element does NOT exist

# ⚠️  == vs is:
#   Use == to compare VALUES  (5 == 5.0 is True)
#   Use is  only for None / True / False checks

# 5. String Operators — only + and * work on strings!
print("Hello" + " World")  # → "Hello World"  (concatenation)
print("Ha" * 3)             # → "HaHaHa"       (repetition)
# "Hello" - "lo"  → ❌ TypeError
# "Hello" / 2     → ❌ TypeError

# Operator precedence (high → low):
#   ** → *, /, //, % → +, - → comparisons → not → and → or


# ──────────────────────────────────────────
# SECTION 6 — INPUT / OUTPUT
# ──────────────────────────────────────────

# input() ALWAYS returns a string — cast to int/float for numbers
# (Commented out to prevent blocking on execution)
# name   = input("Enter your name: ")
# age    = int(input("Enter age: "))          # cast to int
# salary = float(input("Salary: "))           # cast to float
# a, b   = map(int, input("Two numbers: ").split())  # two values

# print() — display output
print("Hello")                         # → Hello
print("Name:", "Alice", "Age:", 25)    # → Name: Alice Age: 25

print("a", "b", "c", sep="-")         # → a-b-c  (custom separator)
print("Hello", end=" ")               # no newline after Hello
print("World")                         # → Hello World  (on same line)

# f-strings — best way to format output
pi = 3.14159
print(f"{pi:.2f}")          # → 3.14       (2 decimal places)
print(f"{1000000:,}")        # → 1,000,000  (with commas)
name2 = "Alice"; age2 = 25
print(f"My name is {name2} and I am {age2}")

# --- Reusable pattern: read N numbers from user ---
def read_numbers(n):
    """Read n numbers from user and return as a list."""
    numbers = []
    for i in range(n):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)
    return numbers
# nums = read_numbers(10)  # uncomment to use interactively


# ──────────────────────────────────────────
# SECTION 7 — RANDOM NUMBERS
# ──────────────────────────────────────────

import random

print(random.random())               # float in [0.0, 1.0)
print(random.randint(1, 100))         # int BOTH endpoints inclusive
print(random.uniform(5, 10))          # float between 5 and 10
print(random.choice(['a', 'b', 'c'])) # random element from list
print(random.choices([1,2,3], k=5))   # 5 picks WITH replacement
print(random.sample([1,2,3,4,5], 3))  # 3 picks WITHOUT replacement

lst2 = [1, 2, 3, 4, 5]
random.shuffle(lst2)                   # shuffles list IN-PLACE
print(lst2)

# Reproducibility: set seed BEFORE other random calls
random.seed(42)
print(random.randint(1, 100))  # always the same number with seed=42


# ╔══════════════════════════════════════════════════════════╗
# ║         DAY 2 — CONTROL FLOW                            ║
# ╚══════════════════════════════════════════════════════════╝

# ──────────────────────────────────────────
# SECTION 1 — IF-ELSE (DECISIONS)
# ──────────────────────────────────────────

# if-else = "If this is true, do X; otherwise do Y"
# ⚠️  Indentation is MANDATORY (4 spaces). Missing it = SyntaxError.

# Basic syntax:
#   if condition:       ← must end with colon
#       do_something()  ← must be indented
#   elif another:
#       do_other()
#   else:
#       fallback()

# --- Grade classification example ---
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(get_grade(95))   # → A
print(get_grade(75))   # → C
print(get_grade(45))   # → F

# --- Tier Classification Pattern (reusable template) ---
# Use with df['col'].apply(classify) in Pandas
def classify(value):
    if value >= 80:    return "High"
    elif value >= 50:  return "Medium"
    else:              return "Low"

# --- Compound conditions ---
age = 25
income = 50000

if age >= 18 and income >= 30000:   # AND: both must be true
    print("Eligible for loan")

if age < 18 or age > 65:            # OR: at least one must be true
    print("Cannot apply")

if not (age < 18):                  # NOT: reverses the condition
    print("Adult")

if 18 <= age <= 65:                 # Python-specific range check shortcut
    print("Working age")            # same as: age >= 18 and age <= 65

# --- Ternary (one-line if-else) ---
status = "Adult" if age >= 18 else "Minor"
print(status)   # → Adult

# ⚠️  Common mistakes:
#   if x = 5 → ❌ use == not = inside conditions
#   Missing colon at end of if line
#   Writing If or IF — must be lowercase if


# ──────────────────────────────────────────
# SECTION 2 — FOR LOOPS
# ──────────────────────────────────────────

# for loop = repeat for each item in a collection
# Use when you KNOW how many times to repeat, or have a sequence

# --- range() — most common iterable ---
for i in range(5):          # 0 to 4 (stop is excluded)
    print(i, end=" ")       # → 0 1 2 3 4
print()

for i in range(2, 7):       # 2 to 6
    print(i, end=" ")       # → 2 3 4 5 6
print()

for i in range(0, 10, 2):   # step of 2
    print(i, end=" ")       # → 0 2 4 6 8
print()

for i in range(10, 0, -1):  # count DOWN
    print(i, end=" ")       # → 10 9 8 7 6 5 4 3 2 1
print()

# --- Iterating over different types ---
fruits = ["apple", "banana", "cherry"]
for f in fruits:            # iterate over a list
    print(f)

for c in "hello":           # iterate over a string character by character
    print(c, end=" ")       # → h e l l o
print()

prices = {"apple": 100, "banana": 50}
for key in prices:                  # dict → keys by default
    print(key, prices[key])

for key, val in prices.items():     # get BOTH key and value
    print(f"{key}: {val}")

# --- enumerate() — get index AND value ---
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")          # 0: apple, 1: banana, 2: cherry

for i, fruit in enumerate(fruits, 1):  # start index at 1 instead of 0
    print(f"{i}: {fruit}")          # 1: apple, 2: banana, 3: cherry

# --- zip() — iterate two lists in parallel ---
names = ["Alice", "Bob"]
ages  = [25, 30]
for name, age_val in zip(names, ages):
    print(f"{name} is {age_val}")

# --- Accumulator Pattern ---
# Purpose: build up a result while looping (sum, count, filtered list)
def sum_list(numbers):
    total = 0               # start at zero
    for num in numbers:
        total += num        # add each element
    return total

def count_evens(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1      # increment when condition met
    return count

def filter_evens(numbers):
    result = []             # start with empty list
    for num in numbers:
        if num % 2 == 0:
            result.append(num)   # append matches
    return result

nums = [1, 2, 3, 4, 5, 6]
print(sum_list(nums))       # → 21
print(count_evens(nums))    # → 3
print(filter_evens(nums))   # → [2, 4, 6]

# --- Search Pattern: Find First Match ---
def find_first_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num      # exit as soon as found
    return None             # nothing found

print(find_first_even([1, 3, 4, 7, 8]))  # → 4
print(find_first_even([1, 3, 5, 7]))     # → None


# ──────────────────────────────────────────
# SECTION 3 — WHILE LOOPS
# ──────────────────────────────────────────

# while loop = repeat AS LONG AS condition is true
# Use when you DON'T know in advance how many times to repeat
# ⚠️  Always change something inside the loop or it runs FOREVER!

i = 1
while i <= 5:
    print(i, end=" ")
    i += 1              # MUST increment — else infinite loop!
print()                 # → 1 2 3 4 5

n = 10
while n > 0:
    print(n, end=" ")
    n -= 1
print()                 # → 10 9 8 7 6 5 4 3 2 1

# --- STOP-Loop Pattern (used in billing/shop problems) ---
# Pattern: while True + break when user types STOP
def collect_items():
    """Keep collecting input until user types STOP."""
    items = []
    while True:
        entry = input("Enter item (or STOP to finish): ").strip().upper()
        if entry == "STOP":
            break           # exit the loop
        items.append(entry)
    return items
# items = collect_items()   # uncomment to use interactively

# --- for vs while quick guide ---
# Use for:   known count, iterating over list/dict/string
# Use while: unknown count, condition-driven, user input loops


# ──────────────────────────────────────────
# SECTION 4 — BREAK & CONTINUE
# ──────────────────────────────────────────

# break    = exit the loop immediately (completely)
# continue = skip current iteration, jump to next one

# --- break: stop as soon as target found ---
numbers = [10, 20, 30, 40, 50]
target = 30
for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break           # stop checking the rest
    print(f"Checked {num}")
# Output: Checked 10 / Checked 20 / Found 30!

# --- continue: skip even numbers, print only odds ---
for i in range(10):
    if i % 2 == 0:
        continue        # skip even, go to next iteration
    print(i, end=" ")  # prints 1 3 5 7 9
print()


# ──────────────────────────────────────────
# SECTION 5 — NESTED LOOPS
# ──────────────────────────────────────────

# Outer loop runs once → inner loop runs completely → outer moves next
# Complexity: O(n²) — avoid 3+ levels where possible

# --- Multiplication table ---
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}×{j}={i*j}", end="  ")
    print()     # newline after each row
# 1×1=1  1×2=2  1×3=3
# 2×1=2  2×2=4  2×3=6
# 3×1=3  3×2=6  3×3=9

# --- Iterate over a matrix (list of lists) ---
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()


# ──────────────────────────────────────────
# SECTION 6 — KEY PATTERNS FROM EXAM PAPERS
# ──────────────────────────────────────────

# --- Pattern 1: Validation Loop (re-prompt on bad input) ---
def get_valid_choice(options):
    """Keep asking until user gives a valid choice."""
    while True:
        choice = input(f"Choose from {options}: ").strip()
        if choice in options:
            return choice
        print("Invalid! Try again.")
# size = get_valid_choice(["S", "M", "L"])

# --- Pattern 2: Counting into Grade Buckets ---
def categorize_into_grades(scores):
    A, B, C, D, F = [], [], [], [], []
    for score in scores:
        if score >= 90:    A.append(score)
        elif score >= 80:  B.append(score)
        elif score >= 70:  C.append(score)
        elif score >= 60:  D.append(score)
        else:              F.append(score)
    return [A, B, C, D, F]

print(categorize_into_grades([95, 82, 71, 65, 40]))

# --- Pattern 3: Loop with Index using enumerate ---
def print_numbered(items):
    for position, item in enumerate(items, 1):
        print(f"  {position}. {item}")

print_numbered(["apple", "banana", "cherry"])


# ╔══════════════════════════════════════════════════════════╗
# ║         DAY 3 — FUNCTIONS                               ║
# ╚══════════════════════════════════════════════════════════╝

# ──────────────────────────────────────────
# SECTION 1 — WHAT IS A FUNCTION?
# ──────────────────────────────────────────

# A function is a reusable block of code:
#   INPUT → FUNCTION → OUTPUT
#
# Why use functions?
#   Reusability  — write once, use many times
#   Readability  — calculate_tax(income) reads like English
#   Testing      — easy to verify each piece in isolation
#   Abstraction  — hide complexity behind a simple name
#
# Exam tip: wrap EVERY solution in a function!


# ──────────────────────────────────────────
# SECTION 2 — DEFINING FUNCTIONS (def)
# ──────────────────────────────────────────

# Syntax:
#   def function_name(parameter1, parameter2):
#       # body (indented 4 spaces)
#       return result       # optional — if omitted, returns None

def add(a, b):
    return a + b            # sends value BACK to caller

result = add(3, 5)          # call with arguments 3 and 5
print(result)               # → 8

# --- Returning multiple values (as a tuple) ---
def min_max(numbers):
    return min(numbers), max(numbers)   # returns a tuple

low, high = min_max([3, 1, 4, 5, 9, 2])
print(low, high)    # → 1 9

# ⚠️  Common mistakes:
#   Forgetting the colon at end of def line
#   Not indenting the body
#   Using print() instead of return — print shows on screen,
#     return sends the value back for further use
#   Writing function_name without () — gets the function object itself!


# ──────────────────────────────────────────
# SECTION 3 — PARAMETERS AND ARGUMENTS
# ──────────────────────────────────────────

# Parameter = variable in the def line
# Argument  = actual value passed when calling the function

# 1. Positional Arguments — order matters!
def describe(name, age, city):
    print(f"{name}, {age}, from {city}")

describe("Alice", 25, "Bengaluru")   # order must match parameters!

# 2. Keyword Arguments — use names, order doesn't matter
describe(age=25, city="Bengaluru", name="Alice")   # same result

# 3. Default Parameters ⭐ (EXAM FAVOURITE)
# Parameters can have default values used when caller doesn't pass them
# ⚠️  RULE: defaults MUST come AFTER non-default parameters!
#    def fn(a=1, b): ❌  SyntaxError
#    def fn(a, b=1): ✅  Correct

def greet(name, message="Hello"):   # message has a default
    print(f"{message}, {name}!")

greet("Alice")              # uses default  → "Hello, Alice!"
greet("Bob", "Hi")          # overrides     → "Hi, Bob!"

def power(base, exponent=2):
    return base ** exponent

print(power(5))             # → 25  (5²)
print(power(5, 3))          # → 125 (5³)


# ──────────────────────────────────────────
# SECTION 4 — *args and **kwargs (CRITICAL)
# ──────────────────────────────────────────

# *args   — accept any number of POSITIONAL arguments → collected as a TUPLE
# **kwargs — accept any number of KEYWORD arguments  → collected as a DICT
#
# Memory Aid:
#   *args   = "Accept any number of Positional → tuple"
#   **kwargs = "Accept any number of Key=Value → dict"
#   The names args/kwargs are conventions — * and ** are what matter

# --- *args example ---
def total(*args):
    print("args type:", type(args))   # always a tuple
    print("args:", args)
    return sum(args)

print(total(1, 2, 3))           # → 6
print(total(10, 20, 30, 40))    # → 100
print(total())                  # → 0  (empty tuple)

# --- **kwargs example ---
def describe_person(**kwargs):
    print("kwargs type:", type(kwargs))   # always a dict
    for key, val in kwargs.items():
        print(f"  {key}: {val}")

describe_person(name="Alice", age=25, city="Bengaluru")

# --- Combining all in the correct ORDER ---
# Order MUST be: positional → *args → defaults → **kwargs
def complete_function(required, *args, default=10, **kwargs):
    print(f"required = {required}")
    print(f"args     = {args}")
    print(f"default  = {default}")
    print(f"kwargs   = {kwargs}")

complete_function("hi", 1, 2, 3, default=99, x=10, y=20)

# --- Practical: *args for statistics ---
def stats(*numbers):
    """Accept any number of numbers and return statistics."""
    if not numbers:
        return None
    return {
        'count': len(numbers),
        'sum':   sum(numbers),
        'min':   min(numbers),
        'max':   max(numbers),
        'avg':   sum(numbers) / len(numbers)
    }

print(stats(10, 20, 30, 40, 50))


# ──────────────────────────────────────────
# SECTION 5 — LAMBDA (ANONYMOUS FUNCTIONS)
# ──────────────────────────────────────────

# Lambda = tiny, one-line, nameless function
# Syntax:  lambda arguments: expression
# No def, no return, no name needed
#
# Memory Aid — LIE:  Lambda · Inputs · Expression
# Can only have ONE expression (use def for anything more complex)

# --- Basic lambdas ---
square = lambda x: x ** 2
print(square(5))                    # → 25

add_two = lambda a, b: a + b
print(add_two(3, 7))                # → 10

# --- With map(): apply function to every element ---
nums3 = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums3))
print(squares)                      # → [1, 4, 9, 16, 25]

# --- With filter(): keep only elements that match condition ---
evens = list(filter(lambda x: x % 2 == 0, nums3))
print(evens)                        # → [2, 4]

# --- With sorted(): custom sort key ---
words = ["banana", "apple", "fig"]
by_length = sorted(words, key=lambda x: len(x))
print(by_length)                    # → ['fig', 'apple', 'banana']

# --- With reduce(): combine all into one value ---
from functools import reduce
total2 = reduce(lambda a, b: a + b, nums3)
print(total2)                       # → 15

# --- Exam question: sum all elements in a list using lambda ---
sum_lambda = lambda lst: sum(lst)
print(sum_lambda([5, 8, 10, 20, 50, 100]))   # → 193

# Immediate invocation (IIFE style):
result2 = (lambda lst: sum(lst))([5, 8, 10, 20, 50, 100])
print(result2)                      # → 193

# --- With pandas (commented — no DataFrame here) ---
# df['category'] = df['age'].apply(lambda x: 'adult' if x >= 18 else 'minor')


# ──────────────────────────────────────────
# SECTION 6 — GLOBAL KEYWORD
# ──────────────────────────────────────────

# LEGB Rule — Python searches variables in this order:
#   Local → Enclosing → Global → Built-in

# Problem without global keyword:
count = 0           # global variable

def increment_wrong():
    # count = count + 1  ← ❌ UnboundLocalError
    # Python sees "count =" → assumes it's LOCAL
    # But local count not defined yet → crash!
    pass

# Solution: use global keyword
def increment():
    global count        # tell Python: use the global variable
    count += 1

increment()
increment()
print(count)            # → 2 ✅

# Reading a global is FINE without the global keyword:
PI = 3.14159

def circle_area(r):
    return PI * r ** 2   # reading PI — no global keyword needed

print(circle_area(5))    # → 78.54

# Memory Aid: "Read freely, Write needs global"


# ──────────────────────────────────────────
# SECTION 7 — RECURSION
# ──────────────────────────────────────────

# Recursion = a function that calls itself
# Recipe for every recursive function:
#   1. Base case  — when does it STOP? (must have or → infinite!)
#   2. Recursive case — call self with a SMALLER input

# --- Factorial ---
def factorial(n):
    if n <= 1:              # BASE CASE: stop here
        return 1
    return n * factorial(n - 1)   # RECURSIVE CASE

print(factorial(5))   # → 120
# How it unwinds:
#   factorial(5) = 5 × factorial(4)
#   factorial(4) = 4 × factorial(3)
#   factorial(3) = 3 × factorial(2)
#   factorial(2) = 2 × factorial(1)
#   factorial(1) = 1  ← base case
#   Then: 1→2→6→24→120

# --- Fibonacci ---
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print([fib(i) for i in range(10)])   # → [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# ⚠️  Python's recursion limit is 1000 by default.
#     For deep recursion, use loops instead.


# ──────────────────────────────────────────
# SECTION 8 — DOCSTRINGS & TYPE HINTS
# ──────────────────────────────────────────

# Type hints  : annotate parameter and return types (not enforced, just for clarity)
# Docstring   : string right after def — appears in help()
# Exam tip    : add a one-line docstring under every function!

def calculate_bmi(weight: float, height: float) -> float:
    """Compute BMI given weight in kg and height in m."""
    return weight / (height ** 2)

print(calculate_bmi(70, 1.75))    # → 22.86
# help(calculate_bmi)             # shows the docstring


# ──────────────────────────────────────────
# SECTION 9 — REUSABLE FUNCTION TEMPLATES
# ──────────────────────────────────────────

# Template 1: Validation Function
def is_valid_username(value):
    """Check multiple rules; return False on first failure."""
    if len(value) < 4:        return False  # too short
    if not value[0].isalpha(): return False  # must start with letter
    return True

# Template 2: Filter + Transform
def process_list(items, condition_fn, transform_fn):
    """Filter items by condition, then transform each match."""
    result = []
    for item in items:
        if condition_fn(item):
            result.append(transform_fn(item))
    return result

# squares of even numbers
nums4 = [1, 2, 3, 4, 5]
print(process_list(nums4, lambda x: x % 2 == 0, lambda x: x**2))
# → [4, 16]

# Template 3: Aggregator
def aggregate(items, condition_fn):
    """Count and collect items meeting a condition."""
    matches = [item for item in items if condition_fn(item)]
    return {
        'count': len(matches),
        'sum':   sum(matches) if matches else 0,
        'list':  matches
    }

# Template 4: Two-Stage Bill Calculator
def calculate_bill(items_dict, tax_rate=0.12):
    """Stage 1: subtotal. Stage 2: apply tax, return total."""
    subtotal = sum(items_dict.values())
    tax      = subtotal * tax_rate
    total    = subtotal + tax
    return {'subtotal': subtotal, 'tax': round(tax, 2), 'total': round(total, 2)}

print(calculate_bill({"pen": 10, "book": 150, "bag": 500}))


# ╔══════════════════════════════════════════════════════════╗
# ║         DAY 4 — STRINGS                                 ║
# ╚══════════════════════════════════════════════════════════╝

# ──────────────────────────────────────────
# SECTION 1 — STRING BASICS
# ──────────────────────────────────────────

# A string is a sequence of characters.
# Strings are IMMUTABLE — once created, they cannot be changed.

s1 = "Hello"            # double quotes
s2 = 'World'            # single quotes — same thing

print(len(s1))          # → 5  (number of characters)
print(s1 + " " + s2)    # → "Hello World"  (concatenation with +)
print(s1 * 3)           # → "HelloHelloHello"  (repetition with *)
print("ell" in s1)      # → True  (membership test)

# Strings are immutable:
s = "hello"
# s[0] = "H"            # ❌ TypeError!
s = "H" + s[1:]         # ✅ creates a NEW string "Hello"


# ──────────────────────────────────────────
# SECTION 2 — STRING SLICING (CRITICAL — 5 exam papers!)
# ──────────────────────────────────────────

# Syntax: string[start : stop : step]
#   start = where to begin     (inclusive, default 0)
#   stop  = where to end       (EXCLUSIVE, default len)
#   step  = how many to skip   (default 1)
#
# Memory Aid:  "Start In, End Out" — start is included, stop is NOT
#
# Index visualization for "PythonProgramming":
#   P  y  t  h  o  n  P  r  o  g  r  a  m  m  i  n  g
#   0  1  2  3  4  5  6  7  8  9 ...
#  -17 -16 -15 ...                                    -1

# --- Exam question: extract "thonPro" from "PythonProgramming" ---
s = "PythonProgramming"
# 't' is at index 2, last char needed 'o' is at index 8
# stop must be 9 (exclusive), so [2:9]
result = s[2:9]
print(result)           # → "thonPro" ✅

# --- All slicing patterns ---
s = "Hello World"
print(s[0])             # → 'H'           single character
print(s[-1])            # → 'd'           last character
print(s[0:5])           # → 'Hello'       chars 0–4
print(s[:5])            # → 'Hello'       start defaults to 0
print(s[6:])            # → 'World'       end defaults to len
print(s[:])             # → 'Hello World' full copy
print(s[-5:])           # → 'World'       last 5 characters
print(s[:-6])           # → 'Hello'       all except last 6
print(s[::2])           # → 'HloWrd'      every 2nd character
print(s[::-1])          # → 'dlroW olleH' REVERSED! ← very common!
print(s[1:8:2])         # → 'el o'        every 2nd from index 1 to 8

# Shortcuts to remember:
#   s[:n]   → first n characters
#   s[-n:]  → last n characters
#   s[::-1] → reverse (works on lists too!)


# ──────────────────────────────────────────
# SECTION 3 — find() vs index() (EXAM QUESTION)
# ──────────────────────────────────────────

# find()  — returns index if found, returns -1 if NOT found  (safe!)
# index() — returns index if found, raises ValueError if NOT found (risky!)

s = "Hello Python World"

# find() — safe to use anywhere
print(s.find("Python"))     # → 6   found at index 6
print(s.find("Java"))       # → -1  not found, no crash!

# index() — crashes if not found
print(s.index("Python"))    # → 6
# s.index("Java")           # ❌ ValueError!

# Safe pattern when using index():
if "Java" in s:
    print(s.index("Java"))
else:
    print("Not found")

# Memory Aid:
#   find  = "Find or return -1"
#   index = "Index or Explode!"


# ──────────────────────────────────────────
# SECTION 4 — STRING METHODS (TOP 30)
# ──────────────────────────────────────────

s = "Hello World"

# --- Case manipulation ---
print(s.upper())          # → "HELLO WORLD"
print(s.lower())          # → "hello world"
print(s.title())          # → "Hello World"   (each word capitalized)
print(s.capitalize())     # → "Hello world"   (only first letter of string)
print(s.swapcase())       # → "hELLO wORLD"

# --- Whitespace trimming ---
s2 = "   Hello   "
print(s2.strip())         # → "Hello"     (both ends)
print(s2.lstrip())        # → "Hello   "  (left only)
print(s2.rstrip())        # → "   Hello"  (right only)
print("##Hi##".strip("#"))  # strips specific chars

# --- Search & Replace ---
print(s.find("World"))               # → 6
print(s.count("l"))                  # → 3   (counts occurrences)
print(s.replace("World", "Python"))  # → "Hello Python"
print(s.startswith("Hello"))         # → True
print(s.endswith("World"))           # → True

# --- Type-check methods (all return True/False) ---
print("abc".isalpha())       # True  — only letters
print("123".isdigit())       # True  — only digits
print("abc123".isalnum())    # True  — letters + digits, no spaces
print("hello".islower())     # True
print("HELLO".isupper())     # True
print("Hello World".istitle()) # True
print("   ".isspace())       # True  — only whitespace

# --- Split & Join ---
s3 = "apple,banana,cherry"
parts = s3.split(",")              # → ['apple', 'banana', 'cherry']
print(parts)

words = "hello world python".split()  # splits on whitespace by default
print(words)                           # → ['hello', 'world', 'python']

joined = "-".join(["a", "b", "c"])     # → "a-b-c"  (reverse of split)
print(joined)

# --- Padding & Alignment ---
print("5".zfill(3))           # → "005"    (zero-pad to width 3)
print("abc".center(7, "*"))   # → "**abc**"
print("abc".ljust(7, "."))    # → "abc...."
print("abc".rjust(7, "."))    # → "....abc"


# ──────────────────────────────────────────
# SECTION 5 — STRING VALIDATION PATTERNS
# ──────────────────────────────────────────

# Universal Validation Pattern:
#   1. Check length first
#   2. Check first character
#   3. Check each character in a loop
#   4. Check last character
#   5. Return False on first failure, True if all pass

# --- Username Validation (Mar2024 + Nov2023) ---
def UsernameValidation(s):
    """Validate username: length 4-25, starts with letter,
    only letters/digits/underscore, cannot end with underscore."""
    if len(s) < 4 or len(s) > 25:   # Rule 1: length
        return 'false'
    if not s[0].isalpha():            # Rule 2: must start with letter
        return 'false'
    for c in s:                       # Rule 3: allowed characters
        if not (c.isalnum() or c == '_'):
            return 'false'
    if s[-1] == '_':                  # Rule 4: cannot end with _
        return 'false'
    return 'true'

print(UsernameValidation("alice_123"))  # → true
print(UsernameValidation("alice_"))     # → false  (ends with _)
print(UsernameValidation("1alice"))     # → false  (starts with digit)
print(UsernameValidation("ab"))         # → false  (too short)

# --- Password Strength (Nov 2023) ---
def password_strength(pwd):
    """Score a password 0-8 based on complexity rules."""
    score = 0
    if len(pwd) >= 8:                           score += 2
    if any(c.isupper() for c in pwd):           score += 1
    if any(c.islower() for c in pwd):           score += 1
    if any(c.isdigit() for c in pwd):           score += 2
    if any(c in "!@#$%^&*" for c in pwd):       score += 2
    return score

print(password_strength("abc"))        # → 1   (only lowercase)
print(password_strength("Pass@123"))   # → 8   (all criteria met)

# --- Extract Alphanumeric Tokens (Mar 2024) ---
def find_special_codes(message):
    """Return only tokens that are purely alphanumeric (no special chars)."""
    tokens = message.split()
    return [token for token in tokens if token.isalnum()]

print(find_special_codes("abc 123 ab@c hello! ok99"))
# → ['abc', '123', 'ok99']

# --- Number Plate Even/Odd Classification (Model Set) ---
def classify_plates(plates):
    """Split plate strings and classify by last numeric part."""
    result = {'Even': [], 'Odd': []}
    for plate in plates:
        parts = plate.split()
        for part in reversed(parts):    # find last numeric segment
            if part.isdigit():
                if int(part) % 2 == 0:
                    result['Even'].append(plate)
                else:
                    result['Odd'].append(plate)
                break
    return result

plates = ["KA 02 4592", "DL 09 8765", "MH 14 1234"]
print(classify_plates(plates))

# --- Telephone Keypad Match (Nov 2023) ---
def telephone_match(num, s):
    """Check if string s matches phone number on a telephone keypad."""
    keypad = {'2': 'ABC', '3': 'DEF', '4': 'GHI',
              '5': 'JKL', '6': 'MNO', '7': 'PQRS',
              '8': 'TUV', '9': 'WXYZ'}
    if len(num) != len(s):
        return False
    for digit, letter in zip(num, s.upper()):
        if digit not in keypad or letter not in keypad[digit]:
            return False
    return True

print(telephone_match("22426", "CABIN"))    # → True
print(telephone_match("22426", "DABIN"))    # → False


# ──────────────────────────────────────────
# SECTION 6 — STRING FORMATTING (f-strings)
# ──────────────────────────────────────────

name3 = "Alice"
age3  = 25
gpa   = 3.847

print(f"{name3} is {age3} years old")     # basic interpolation
print(f"GPA: {gpa:.2f}")                  # → "GPA: 3.85"  (2 decimal places)
print(f"{age3:>5}")                        # → "   25"  (right-align in 5 cols)
print(f"{age3:<5}")                        # → "25   "  (left-align)
print(f"{age3:^5}")                        # → " 25  "  (center)
print(f"{1234567:,}")                      # → "1,234,567"  (comma separator)
print(f"{0.85:.1%}")                       # → "85.0%"  (percentage format)
print(f"Next year: {age3 + 1}")            # expressions work inside {}
print(f"Upper: {name3.upper()}")           # method calls work too


# ──────────────────────────────────────────
# QUICK REFERENCE CHEATSHEET (as comments)
# ──────────────────────────────────────────

# SLICING          SEARCH             TYPE CHECKS
# s[:n]   first n  s.find(x)  or -1  isalpha()  letters only
# s[-n:]  last n   s.index(x) or ERR isdigit()  digits only
# s[::-1] reverse  s.count(x) count  isalnum()  letters+digits
# s[::2]  every 2  x in s     T/F    isspace()  whitespace only

# *args / **kwargs
# *args   → tuple  (any number of positional args)
# **kwargs → dict  (any number of keyword args)
# Order: positional → *args → defaults → **kwargs

# SCOPE (LEGB): Local → Enclosing → Global → Built-in
# Read global freely. Write global? Use the global keyword.

# FALSY VALUES: 0, 0.0, "", [], {}, None, False
# Everything else is truthy.

# MUTABLE   : list, dict, set
# IMMUTABLE : int, float, bool, str, tuple, frozenset, bytes

# ============================================================
# End of Notes — Good luck on your exam!
# ============================================================
