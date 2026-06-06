# ============================================================
#   PES University · UE20CS901 — Python for Data Science
#   Study Notes: Days 7–10
#   Day 7  — NumPy
#   Day 8  — Pandas Basics
#   Day 9  — Pandas Advanced
#   Day 10 — Data Visualization
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ╔══════════════════════════════════════════════════════════╗
# ║         DAY 7 — NUMPY                                   ║
# ╚══════════════════════════════════════════════════════════╝

# ──────────────────────────────────────────
# SECTION 1 — INTRO TO NUMPY
# ──────────────────────────────────────────

# NumPy = "Numerical Python"
# Core data structure: ndarray (n-dimensional array)
# Much faster than Python lists for numerical operations
#
# Key Features (for theory/Section A questions):
#   ndarray          — multi-dimensional homogeneous arrays
#   Vectorized ops   — apply operations on entire arrays without loops
#   Broadcasting     — operate on arrays of different shapes
#   Speed            — implemented in C, far faster than Python lists
#   Memory efficient — stores raw numeric data, no Python object overhead
#   Linear algebra   — matrix ops, decomposition, eigenvalues
#   Random module    — np.random for random number generation
#   Foundation       — pandas, SciPy, scikit-learn all build on NumPy
#
# Array vs List:
#   Python List  → can hold mixed types, slow, more memory
#   NumPy Array  → homogeneous (same type), fast, vectorized math

# --- Basic array from a list ---
a = np.array([1, 2, 3, 4, 5])
print(a)              # [1 2 3 4 5]
print(type(a))        # <class 'numpy.ndarray'>

# --- Vectorized math — NO LOOPS needed! ---
print(a * 2)          # [2 4 6 8 10]
print(a + a)          # [2 4 6 8 10]
print(a ** 2)         # [1 4 9 16 25]


# ──────────────────────────────────────────
# SECTION 2 — CREATING ARRAYS
# ──────────────────────────────────────────

# --- From Python structures ---
np.array([1, 2, 3])              # 1D array
np.array([[1, 2], [3, 4]])       # 2D matrix (list of lists)

# --- Special arrays ---
print(np.zeros((3, 4)))          # 3×4 filled with 0.0
print(np.ones((2, 3)))           # 2×3 filled with 1.0
print(np.full((3, 3), 7))        # 3×3 filled with 7
print(np.eye(3))                 # 3×3 identity matrix (1s on diagonal)
print(np.identity(4))            # same as eye(4)
print(np.diag([1, 2, 3]))        # diagonal matrix with given values

# --- Range arrays ---
print(np.arange(10))             # [0 1 2 3 4 5 6 7 8 9]
print(np.arange(2, 10, 2))       # [2 4 6 8]  (start, stop, step)
print(np.linspace(0, 1, 5))      # [0. 0.25 0.5 0.75 1.]  (5 EVENLY SPACED points)

# --- EXAM QUESTION: arange vs linspace ---
# np.arange(start, stop, step) — specifies the STEP SIZE,  stop is EXCLUDED
# np.linspace(start, stop, num) — specifies the NUMBER OF POINTS, stop is INCLUDED
print(np.arange(0, 1, 0.25))     # [0.   0.25 0.5  0.75]   (4 values, 1 not included)
print(np.linspace(0, 1, 5))      # [0.   0.25 0.5  0.75 1.] (5 values, 1 IS included)

# --- Random arrays ---
print(np.random.rand(3, 3))         # 3×3 floats in [0, 1)
print(np.random.randint(1, 100, 5)) # 5 random ints in [1, 100)
print(np.random.normal(0, 1, 10))   # 10 values from normal distribution N(0,1)

# --- Array properties ---
a2 = np.array([[1, 2, 3], [4, 5, 6]])
print(a2.shape)    # (2, 3)   — (rows, columns)
print(a2.ndim)     # 2        — number of dimensions
print(a2.size)     # 6        — total number of elements
print(a2.dtype)    # int64    — data type of elements


# ──────────────────────────────────────────
# SECTION 3 — IDENTITY MATRIX (np.eye) — EXAM QUESTION (July 2021)
# ──────────────────────────────────────────

# Identity matrix: square matrix with 1s on the MAIN DIAGONAL and 0s everywhere else
# Key property:  A × I = A  (like multiplying a number by 1)
#
# Memory Aid: np.eye = "Eye on the Diagonal" — looks like the letter I

I3 = np.eye(3)
print(I3)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

print(np.eye(3, dtype=int))   # integer version
# [[1 0 0]
#  [0 1 0]
#  [0 0 1]]

# Verify: A × I = A
A = np.array([[2, 3], [4, 5]])
I = np.eye(2)
print(A @ I)        # → same as A  (@ is matrix multiplication)


# ──────────────────────────────────────────
# SECTION 4 — reshape() vs resize() — EXAM QUESTION (3 papers!)
# ──────────────────────────────────────────

# Feature          reshape()                  resize()
# Returns          NEW array (a view)         None (modifies IN-PLACE)
# Original array   Unchanged                  MODIFIED
# Total elements   Must stay the same         Can change (fills 0 or repeats)
#
# Memory Aid:
#   reshape = "show me Reshaped" (returns new view, original safe)
#   resize  = "Resize me"        (changes original in-place)

a = np.array([1, 2, 3, 4, 5, 6])

# reshape — new view, ORIGINAL UNCHANGED
b = a.reshape(2, 3)   # 2 rows × 3 cols = 6 elements total (must match!)
print(b)
# [[1 2 3]
#  [4 5 6]]
print(a)               # [1 2 3 4 5 6] ← still unchanged

# Use -1 to let NumPy auto-compute ONE dimension
c = a.reshape(3, -1)   # 3 rows, NumPy calculates 6/3 = 2 cols
print(c.shape)         # (3, 2)

# resize — modifies IN-PLACE, original is changed
a.resize(3, 2)         # same total elements (6), different shape
print(a)
# [[1 2]
#  [3 4]
#  [5 6]]

# resize to MORE elements — fills with 0s
a = np.array([1, 2, 3])
a.resize(2, 3)          # 6 elements but only 3 available → pad with 0s
print(a)
# [[1 2 3]
#  [0 0 0]]


# ──────────────────────────────────────────
# SECTION 5 — vstack, hstack & split — EXAM QUESTION (Mar 2024)
# ──────────────────────────────────────────

# Function         Purpose                    Memory Aid
# np.vstack        Stack VERTICALLY (↕)       V = Vertical = adds ROWS
# np.hstack        Stack HORIZONTALLY (↔)     H = Horizontal = adds COLS
# np.concatenate   General (specify axis)     axis=0 vertical, axis=1 horizontal

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# vstack: stacks arrays as NEW ROWS
print(np.vstack((a, b)))
# [[1 2 3]
#  [4 5 6]]

# hstack: extends the row by joining side-by-side
print(np.hstack((a, b)))
# [1 2 3 4 5 6]

# 2D example
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(np.vstack((A, B)))   # 4×2 matrix (more rows)
print(np.hstack((A, B)))   # 2×4 matrix (more cols)

# --- split — EXAM QUESTION (July 2021) ---
# Split = inverse of stack

arr = np.array([1, 2, 3, 4, 5, 6])

# Equal split into N parts
parts = np.split(arr, 3)
print(parts)        # [array([1,2]), array([3,4]), array([5,6])]

# Split at specific indices
parts2 = np.split(arr, [2, 4])
print(parts2)       # [array([1,2]), array([3,4]), array([5,6])]

# Unequal split (np.array_split allows uneven parts)
parts3 = np.array_split(arr, 4)  # 6 elements / 4 parts → sizes 2,2,1,1
print(parts3)

# 2D split
mat = np.arange(12).reshape(3, 4)
print(np.hsplit(mat, 2))    # split by COLUMNS (horizontal)
print(np.vsplit(mat, 3))    # split by ROWS (vertical)


# ──────────────────────────────────────────
# SECTION 6 — BROADCASTING — EXAM QUESTION (Feb 2025)
# ──────────────────────────────────────────

# Broadcasting: NumPy auto-stretches SMALLER arrays to match shapes.
# Avoids writing explicit loops for element-wise operations.
#
# 3 Broadcasting Rules:
#   1. If shapes differ, prepend 1s to the SMALLER shape
#   2. Two dimensions are compatible if equal OR one of them is 1
#   3. Size-1 dimensions are "stretched" to match the larger size

# --- Scalar + array (scalar broadcast to ALL elements) ---
a = np.array([1, 2, 3])
print(a + 10)         # [11 12 13]  — scalar 10 added to each element

# --- 1D + 2D (1D broadcasts across each ROW) ---
mat = np.array([[1, 2, 3], [4, 5, 6]])
row = np.array([10, 20, 30])
print(mat + row)
# [[11 22 33]
#  [14 25 36]]

# --- Column vector + row vector → creates a MATRIX ---
col = np.array([[1], [2], [3]])   # shape (3, 1)
row = np.array([10, 20])          # shape (2,) → treated as (1, 2)
print(col + row)
# [[11 21]
#  [12 22]
#  [13 23]]


# ──────────────────────────────────────────
# SECTION 7 — INDEXING & SLICING
# ──────────────────────────────────────────

arr = np.array([10, 20, 30, 40, 50])

# 1D slicing — same syntax as Python lists
print(arr[0])          # 10       (first element)
print(arr[-1])         # 50       (last element)
print(arr[1:4])        # [20 30 40]
print(arr[::2])        # [10 30 50]  (every 2nd)

# 2D slicing
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mat[0, 1])       # 2   (row 0, col 1)
print(mat[0])          # [1 2 3]  (entire row 0)
print(mat[:, 1])       # [2 5 8]  (entire column 1)
print(mat[0:2, 1:3])   # 2×2 top-right submatrix

# --- Boolean indexing (VERY powerful!) ---
arr = np.array([10, 25, 8, 42, 17])
mask = arr > 20              # [False  True False  True False]
print(arr[mask])             # [25 42]

print(arr[arr > 20])         # same, one-liner
print(arr[(arr > 10) & (arr < 40)])   # multiple conditions → [25 17]


# ──────────────────────────────────────────
# SECTION 8 — STATISTICAL FUNCTIONS
# ──────────────────────────────────────────

arr = np.array([3, 7, 1, 9, 5, 2])

print(arr.sum())              # 27      — total
print(arr.mean())             # 4.5     — average
print(arr.min(), arr.max())   # 1  9
print(arr.std())              # standard deviation
print(arr.var())              # variance
print(arr.argmin())           # 2       — INDEX of minimum value
print(arr.argmax())           # 3       — INDEX of maximum value
print(np.median(arr))         # 4.0     — median

# --- axis parameter for 2D arrays ---
# axis=0 → collapse ROWS    → result is per COLUMN (going DOWN)
# axis=1 → collapse COLUMNS → result is per ROW    (going ACROSS)
# Memory Aid: "axis=0 gives column results"
mat = np.array([[1, 2, 3], [4, 5, 6]])
print(mat.sum())           # 21       (all elements)
print(mat.sum(axis=0))     # [5 7 9]  (column-wise sum — collapse rows)
print(mat.sum(axis=1))     # [6 15]   (row-wise sum — collapse cols)

# --- any() and all() — EXAM QUESTION (Feb 2025) ---
# any() → True if AT LEAST ONE element is True
# all() → True if ALL elements are True
arr_bool = np.array([True, False, True, True])
print(arr_bool.any())      # True  (at least one True)
print(arr_bool.all())      # False (not ALL True)

nums = np.array([5, 10, 15])
print((nums > 0).all())    # True  — every element is positive
print((nums > 7).any())    # True  — at least one element > 7


# ╔══════════════════════════════════════════════════════════╗
# ║         DAY 8 — PANDAS BASICS                           ║
# ╚══════════════════════════════════════════════════════════╝

# ──────────────────────────────────────────
# SECTION 1 — INTRO TO PANDAS
# ──────────────────────────────────────────

# Two main data structures:
#   Series    — 1D labeled array (like a single column with named indices)
#   DataFrame — 2D labeled table  (like an Excel sheet or SQL table)
#
# Key Features (for theory questions):
#   DataFrame          — tabular structure with labeled rows + columns
#   Read/Write         — CSV, Excel, JSON, SQL
#   Missing data       — dropna(), fillna()
#   GroupBy            — split-apply-combine aggregations
#   Merge/Join         — SQL-style table combining
#   Time series        — date/time indexing
#   Built on NumPy     — fast vectorized operations

# --- Series ---
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)
# a    10
# b    20
# c    30

# --- DataFrame ---
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Carol'],
    'Age':  [25, 30, 35],
    'City': ['BLR', 'DEL', 'MUM']
})
print(df)


# ──────────────────────────────────────────
# SECTION 2 — READING DATA
# ──────────────────────────────────────────

# df = pd.read_csv("data.csv")                        # standard CSV read
# df = pd.read_csv("data.csv", index_col=0)           # first col as index
# df = pd.read_csv("data.csv", na_values=["?","NA"])  # custom NA markers
# df = pd.read_excel("data.xlsx")
# df = pd.read_json("data.json")


# ──────────────────────────────────────────
# SECTION 3 — EXPLORING DATA (use for EVERY dataset)
# ──────────────────────────────────────────

df = pd.DataFrame({
    'Name':   ['Alice', 'Bob', 'Carol', 'David', 'Eve'],
    'Age':    [25, 30, None, 22, 35],
    'City':   ['BLR', 'DEL', 'BLR', 'MUM', 'DEL'],
    'Salary': [50000, 70000, 60000, 45000, 80000]
})

print(df.shape)           # (5, 4)   — (rows, columns)
print(df.head())          # first 5 rows (default)
print(df.head(3))         # first 3 rows
print(df.tail())          # last 5 rows
print(df.columns)         # column names as Index
print(df.columns.tolist())# column names as Python list
print(df.dtypes)          # data type of each column
print(df.info())          # dtypes + non-null counts — shows missing data!
print(df.describe())      # stats: count, mean, std, min, max for numeric cols
print(df.describe(include='all'))  # include non-numeric (object) columns too
print(len(df))            # number of rows

# --- Numerical vs Categorical columns (July 2021) ---
numerical     = df.select_dtypes(include=['number']).columns.tolist()
non_numerical = df.select_dtypes(exclude=['number']).columns.tolist()
print("Numerical:", numerical)         # ['Age', 'Salary']
print("Non-numerical:", non_numerical) # ['Name', 'City']


# ──────────────────────────────────────────
# SECTION 4 — INDEXING: loc & iloc — EXAM QUESTION (Feb 2025)
# ──────────────────────────────────────────

# loc  — label-based indexing  — INCLUSIVE on both ends
# iloc — position-based indexing — EXCLUSIVE on stop (like Python lists)
#
# Feature      loc                     iloc
# Type         LABEL-based             POSITION-based (integer)
# Range end    Inclusive               Exclusive (like Python slices)
# Example      df.loc[0:2, 'Name']     df.iloc[0:2, 0]

df2 = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8]
}, index=['w', 'x', 'y', 'z'])

# --- loc: by LABEL ---
print(df2.loc['x'])            # entire row with label 'x'
print(df2.loc['x', 'A'])       # single cell: row 'x', column 'A'
print(df2.loc['w':'y'])         # rows w, x, y (INCLUSIVE — 'y' IS included)
print(df2.loc[:, 'A'])         # all rows, only column 'A'
print(df2.loc[df2['A'] > 2])   # boolean condition: rows where A > 2

# --- iloc: by POSITION (integer) ---
print(df2.iloc[0])             # first row (position 0)
print(df2.iloc[0, 1])          # row 0, column 1
print(df2.iloc[0:2])           # rows at position 0 and 1 (EXCLUSIVE — position 2 NOT included)
print(df2.iloc[:, 0])          # all rows, first column
print(df2.iloc[-1])            # last row

# --- Direct column access (no loc/iloc needed) ---
print(df2['A'])                 # single column → Series
print(df2[['A', 'B']])          # multiple columns → DataFrame


# ──────────────────────────────────────────
# SECTION 5 — FILTERING ROWS
# ──────────────────────────────────────────

df = pd.DataFrame({
    'Name':   ['Alice', 'Bob', 'Carol', 'David', 'Eve'],
    'Age':    [25, 30, 28, 22, 35],
    'City':   ['BLR', 'DEL', 'BLR', 'MUM', 'DEL'],
    'Salary': [50000, 70000, 60000, 45000, 80000]
})

# Single condition
print(df[df['Age'] > 25])

# Multiple conditions — MUST use & (AND) or | (OR), NOT 'and'/'or'
# ⚠️  Each condition MUST be in parentheses!
print(df[(df['Age'] > 25) & (df['City'] == 'DEL')])   # both conditions true
print(df[(df['Age'] < 25) | (df['Age'] > 30)])         # either condition true

# Membership filter — check if value is in a list
print(df[df['City'].isin(['BLR', 'DEL'])])

# NOT membership — use ~ (tilde) to negate
print(df[~df['City'].isin(['BLR'])])

# String-based filters (using .str accessor)
print(df[df['Name'].str.startswith('A')])
print(df[df['Name'].str.contains('li')])

# between (inclusive on both ends)
print(df[df['Age'].between(25, 30)])

# query() — readable alternative syntax
print(df.query("Age > 25 and City == 'DEL'"))


# ──────────────────────────────────────────
# SECTION 6 — MISSING VALUES — EXAM QUESTION (2 papers!)
# ──────────────────────────────────────────

# IDENTIFY missing values
df = pd.DataFrame({
    'Name':   ['Alice', 'Bob', None, 'David'],
    'Age':    [25, None, 28, 22],
    'Salary': [50000, 70000, None, 45000]
})

print(df.isnull())              # True where NaN
print(df.isnull().sum())        # count of NaN per column
print(df.isnull().sum().sum())  # total NaN in entire DataFrame
print(df.isnull().mean() * 100) # % missing per column
print(df.notna())               # True where NOT NaN (inverse of isnull)

# HANDLE missing values

# Drop rows that have ANY NaN
df.dropna()

# Drop only rows where a SPECIFIC column has NaN
df.dropna(subset=['Age'])

# Drop COLUMNS where ALL values are NaN
df.dropna(axis=1, how='all')

# Fill with a constant
df.fillna(0)
df.fillna("Unknown")

# Fill numeric column with its mean
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Forward fill: use the PREVIOUS valid value
df.fillna(method='ffill')

# Backward fill: use the NEXT valid value
df.fillna(method='bfill')

# Different fill value per column (dict)
df.fillna({'Age': 0, 'Name': 'Unknown'})

# --- EXAM QUESTION: dropna axis=0 vs axis=1 ---
# axis=0 (default) → drop ROWS  with NaN  (use when few rows are bad)
# axis=1           → drop COLUMNS with NaN (use when whole column is mostly empty)


# ──────────────────────────────────────────
# SECTION 7 — REMOVING DUPLICATES — EXAM QUESTION (Mar 2024)
# ──────────────────────────────────────────

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Alice', 'Carol', 'Bob'],
    'City': ['BLR', 'DEL', 'BLR', 'MUM', 'DEL']
})

print(df.duplicated())           # True for duplicate rows (keeps first as False)
print(df.duplicated().sum())     # count of duplicated rows

df.drop_duplicates()                     # keep FIRST occurrence of each duplicate
df.drop_duplicates(keep='last')          # keep LAST occurrence
df.drop_duplicates(keep=False)           # remove ALL copies (no survivors)
df.drop_duplicates(subset=['Name'])      # duplicate check only on 'Name' column
df.drop_duplicates(subset=['Name', 'City'], inplace=True)  # in-place


# ──────────────────────────────────────────
# SECTION 8 — DROPPING ROWS / COLUMNS — EXAM QUESTION (Model Set)
# ──────────────────────────────────────────

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Carol'],
    'Age':  [25, 30, 35],
    'City': ['BLR', 'DEL', 'MUM']
})

# Drop rows by index label
df.drop(0)                           # drop row with index 0
df.drop([0, 1])                      # drop multiple rows

# Drop columns (must specify axis=1)
df.drop('Age', axis=1)               # drop column 'Age'
df.drop(['Age', 'City'], axis=1)     # drop multiple columns

# Cleaner syntax using keyword arguments
df.drop(columns=['Age', 'City'])     # same as axis=1
df.drop(index=[0, 1])                # same as axis=0

# In-place (modifies df directly)
df.drop('Age', axis=1, inplace=True)


# ──────────────────────────────────────────
# SECTION 9 — ADDING COLUMNS
# ──────────────────────────────────────────

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Carol'],
    'Age':  [25, 30, 35],
})

df['Country']    = 'India'                     # constant value for all rows
df['AgePlusOne'] = df['Age'] + 1               # derived from existing column

# Row-wise mean of multiple columns
# df['avg_score'] = df[['Score1', 'Score2']].mean(axis=1).round(1)

# Conditional column using apply + lambda
df['Senior'] = df['Age'].apply(lambda x: 'Yes' if x >= 30 else 'No')

# assign() — chainable, returns new DataFrame (doesn't modify original)
df = df.assign(AgeSquared=df['Age'] ** 2)
print(df)


# ──────────────────────────────────────────
# SECTION 10 — value_counts & unique — EXAM QUESTION (Feb 2025)
# ──────────────────────────────────────────

# Method               What it does
# df['col'].count()    Count NON-NULL entries → single number
# df['col'].value_counts() Count each unique value → Series (sorted by freq)
# df['col'].unique()   Array of unique values
# df['col'].nunique()  COUNT of unique values → single number

df = pd.DataFrame({'City': ['BLR', 'DEL', 'BLR', 'MUM', 'BLR', None]})

print(df['City'].count())           # → 5  (excludes None)

print(df['City'].value_counts())
# BLR    3
# DEL    1
# MUM    1

print(df['City'].value_counts(normalize=True))   # proportions (sum = 1.0)
print(df['City'].unique())          # → ['BLR', 'DEL', 'MUM', None]
print(df['City'].nunique())         # → 3  (unique non-null count)


# ──────────────────────────────────────────
# SECTION 11 — CATEGORICAL DATA — EXAM QUESTION (Aug 2021, May 2025)
# ──────────────────────────────────────────

# Categorical data = fixed set of possible values (Gender: M/F, Grade: A/B/C)
# Storing as 'category' dtype SAVES MEMORY and enables ORDERING

df = pd.DataFrame({'Grade': ['A', 'B', 'C', 'A', 'B', 'F']})

# Convert to categorical
df['Grade'] = df['Grade'].astype('category')
print(df['Grade'].dtype)            # category
print(df['Grade'].cat.categories)   # Index(['A', 'B', 'C', 'F'], dtype='object')

# Set ORDERED categories (enables A > B > C comparisons)
from pandas.api.types import CategoricalDtype
ordered_grades = CategoricalDtype(['F', 'D', 'C', 'B', 'A'], ordered=True)
df['Grade'] = df['Grade'].astype(ordered_grades)
print(df['Grade'].cat.ordered)      # → True
# Now: A > B > C > D > F for comparisons and sorting


# ╔══════════════════════════════════════════════════════════╗
# ║         DAY 9 — PANDAS ADVANCED                         ║
# ╚══════════════════════════════════════════════════════════╝

# ──────────────────────────────────────────
# SECTION 1 — groupby() — THE MOST IMPORTANT PANDAS TOOL
# ──────────────────────────────────────────

# groupby = Split → Apply → Combine
# SQL equivalent of GROUP BY
# Used in EVERY Section C dataset question!

df = pd.DataFrame({
    'Dept':   ['IT', 'HR', 'IT', 'HR', 'Finance'],
    'Salary': [70000, 50000, 80000, 55000, 60000],
    'Age':    [28, 32, 45, 29, 38]
})

# Step 1: SPLIT by 'Dept'
# Step 2: APPLY mean() to 'Salary' within each group
# Step 3: COMBINE results
print(df.groupby('Dept')['Salary'].mean())
# Finance    60000.0
# HR         52500.0
# IT         75000.0

# Common aggregations
print(df.groupby('Dept')['Salary'].sum())    # total per group
print(df.groupby('Dept')['Salary'].count())  # count per group
print(df.groupby('Dept')['Salary'].max())    # maximum per group
print(df.groupby('Dept')['Salary'].min())    # minimum per group
print(df.groupby('Dept')['Salary'].median()) # median per group
print(df.groupby('Dept')['Salary'].std())    # standard deviation per group

# --- Generic reusable groupby helper ---
def group_summary(df, group_col, value_col, agg_func='mean'):
    """Average/sum/count of value_col split by group_col."""
    return df.groupby(group_col)[value_col].agg(agg_func)

# Use for any "average X per Y" question in Section C


# ──────────────────────────────────────────
# SECTION 2 — agg() — MULTIPLE AGGREGATIONS AT ONCE
# ──────────────────────────────────────────

# Method 1: same functions on ALL columns
print(df.groupby('Dept').agg(['mean', 'min', 'max']))

# Method 2: different functions per column (dict)
print(df.groupby('Dept').agg({
    'Salary': ['mean', 'max'],   # two stats for Salary
    'Age':    'mean'             # one stat for Age
}))

# Method 3: named aggregation — CLEANEST, recommended for exams
print(df.groupby('Dept').agg(
    Avg_Salary = ('Salary', 'mean'),
    Max_Salary = ('Salary', 'max'),
    Avg_Age    = ('Age',    'mean'),
    Count      = ('Age',    'count')
).round(2))


# ──────────────────────────────────────────
# SECTION 3 — concat / merge / join
# ──────────────────────────────────────────

# Method        What it does                When to use
# pd.concat()   Stack rows or columns       Same schema, different rows
# pd.merge()    SQL-style join on column    Tables sharing a common key
# df.join()     Join on index               Quick join when index is the key
#
# Memory Aid: concat = stack · merge = SQL JOIN on column · join = JOIN on index

df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['A', 'B', 'C']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Score': [88, 75, 92]})
df3 = pd.DataFrame({'ID': [4, 5],    'Name': ['D', 'E']})

# --- concat: stack ROWS (axis=0, default) ---
combined = pd.concat([df1, df3], ignore_index=True)  # reset index to 0,1,2...
print(combined)

# --- concat: stack COLUMNS (axis=1) ---
side_by_side = pd.concat([df1, df2], axis=1)
print(side_by_side)

# --- merge: INNER join — only rows with matching keys in BOTH DataFrames ---
inner = pd.merge(df1, df2, on='ID')        # only IDs 2,3 appear
print(inner)

# --- merge: LEFT join — keep ALL rows from left (df1), NaN for unmatched ---
left = pd.merge(df1, df2, on='ID', how='left')
print(left)       # ID 1 appears with NaN for Score

# --- merge: OUTER join — keep ALL keys from both DataFrames ---
outer = pd.merge(df1, df2, on='ID', how='outer')
print(outer)

# --- join: works on INDEX (must set index first) ---
df1_idx = df1.set_index('ID')
df2_idx = df2.set_index('ID')
print(df1_idx.join(df2_idx, how='inner'))


# ──────────────────────────────────────────
# SECTION 4 — pivot_table vs crosstab
# ──────────────────────────────────────────

# crosstab    → COUNT frequencies (how many in each category pair)
# pivot_table → AGGREGATE a numeric value column
#
# Memory Aid:
#   crosstab    = "COUNT pairs"
#   pivot_table = "AGGREGATE values"

df = pd.DataFrame({
    'Diabetes': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No'],
    'Survived': ['Y',   'Y',   'N',   'Y',  'N',   'N'],
    'Age':      [45,     50,    60,    35,   70,    55]
})

# crosstab: count how many times each combination appears
print(pd.crosstab(df['Diabetes'], df['Survived']))
# Survived   N   Y
# Diabetes
# No         1   2
# Yes        2   1

# crosstab with ROW percentages (normalize='index' → each row sums to 1.0)
print(pd.crosstab(df['Diabetes'], df['Survived'], normalize='index'))

# crosstab with TOTALS row and column (margins=True)
print(pd.crosstab(df['Diabetes'], df['Survived'], margins=True))

# pivot_table: AVERAGE age for each Diabetes × Survived combination
print(df.pivot_table(values='Age', index='Diabetes', columns='Survived', aggfunc='mean'))

# normalize options:
#   normalize='index'   → row percentages   (rows sum to 1)
#   normalize='columns' → column percentages (cols sum to 1)
#   margins=True        → adds 'All' row and column


# ──────────────────────────────────────────
# SECTION 5 — apply() with lambda (MOST-USED PATTERN)
# ──────────────────────────────────────────

# apply() on Series  → applies function to each VALUE in the column
# apply(axis=1) on DF → applies function to each ROW (uses multiple columns)
#
# Memory Aid: axis=1 = "across columns" = "row by row"
# ALWAYS use pd.notna(x) when source column can contain NaN

df = pd.DataFrame({
    'Name':  ['Alice', 'Bob', 'Carol'],
    'Age':   [25, 17, 35],
    'SibSp': [1, 0, 2],
    'Parch': [0, 1, 1]
})

# --- Single column apply: classify age ---
def age_category(age):
    if age >= 30:   return 'Senior'
    elif age >= 18: return 'Adult'
    else:           return 'Minor'

df['AgeGroup'] = df['Age'].apply(age_category)
print(df[['Name', 'Age', 'AgeGroup']])

# Same with lambda (short logic)
df['IsAdult'] = df['Age'].apply(lambda x: 'Yes' if x >= 18 else 'No')

# --- Multi-column apply (axis=1): family size needs SibSp AND Parch ---
df['FamilySize'] = df.apply(
    lambda row: row['SibSp'] + row['Parch'] + 1,  # +1 for the passenger
    axis=1   # ← this means "go row by row"
)
print(df[['Name', 'SibSp', 'Parch', 'FamilySize']])

# --- Handle NaN in apply ---
# df['Cabin_Type'] = df['Cabin'].apply(lambda x: x[0] if pd.notna(x) else 'Unknown')

# --- Reusable templates ---
def add_categorical_column(df, source_col, new_col, classify_fn):
    """Classify source_col values and store in new_col."""
    df[new_col] = df[source_col].apply(classify_fn)
    return df

def add_derived_column(df, new_col, derive_fn):
    """Compute new_col from multiple existing columns (row-wise)."""
    df[new_col] = df.apply(derive_fn, axis=1)
    return df


# ──────────────────────────────────────────
# SECTION 6 — rank() — 5 METHODS
# ──────────────────────────────────────────

# How ties are handled differs by method — exam-critical!
#
# Method   Behavior for ties          Memory Aid (AMFMD)
# average  Average of tied positions  DEFAULT
# min      Lowest tied rank           "minimum of tied group"
# max      Highest tied rank          "maximum of tied group"
# first    Order of first appearance  "first seen gets lower rank"
# dense    Like min but NO GAPS       "dense = no rank gaps"

s = pd.Series([30, 10, 30, 50, 10])
# Two ties: value 10 at positions 1,4  and  value 30 at positions 0,2

print(s.rank(method='average'))  # [3.5, 1.5, 3.5, 5.0, 1.5]  ← DEFAULT
print(s.rank(method='min'))      # [3.0, 1.0, 3.0, 5.0, 1.0]
print(s.rank(method='max'))      # [4.0, 2.0, 4.0, 5.0, 2.0]
print(s.rank(method='first'))    # [3.0, 1.0, 4.0, 5.0, 2.0]
print(s.rank(method='dense'))    # [2.0, 1.0, 2.0, 3.0, 1.0]  ← no gaps!

# Reverse ranking (largest = rank 1)
print(s.rank(ascending=False))


# ──────────────────────────────────────────
# SECTION 7 — sort_values vs sort_index
# ──────────────────────────────────────────

# sort_values → sort by DATA values in a column
# sort_index  → sort by ROW/COLUMN LABELS (index)

df = pd.DataFrame({
    'Dept':   ['IT', 'HR', 'Finance'],
    'Salary': [70000, 50000, 60000]
}, index=[2, 0, 1])

print(df.sort_values('Salary'))                          # ascending by Salary
print(df.sort_values('Salary', ascending=False))         # descending
print(df.sort_values(['Dept', 'Salary']))                # sort by Dept first, then Salary
print(df.sort_values(['Dept', 'Salary'],
                     ascending=[True, False]))           # Dept asc, Salary desc

print(df.sort_index())                                   # sort by row INDEX labels → 0,1,2
print(df.sort_index(axis=1))                             # sort COLUMN names alphabetically


# ──────────────────────────────────────────
# SECTION 8 — nlargest / nsmallest — TOP-N
# ──────────────────────────────────────────

# Faster and cleaner than sort_values().head(N)
# nlargest  = "give me TOP N rows"
# nsmallest = "give me BOTTOM N rows"

df = pd.DataFrame({
    'Country':    ['India', 'China', 'USA', 'Brazil', 'UK'],
    'Population': [1400, 1400, 330, 215, 67],
    'GDP':        [3200, 18000, 25000, 2000, 3100]
})

print(df.nlargest(3, 'Population'))    # top 3 most populous
print(df.nsmallest(2, 'GDP'))          # 2 lowest GDP

# With filtering first
big_countries = df[df['Population'] > 200]
print(big_countries.nsmallest(2, 'GDP'))


# ──────────────────────────────────────────
# SECTION 9 — isin() — FILTER BY MULTIPLE VALUES
# ──────────────────────────────────────────

# isin() = cleaner alternative to multiple OR conditions
# Memory Aid: "is value IN this list?"  ·  ~ = NOT

df = pd.DataFrame({
    'Name':      ['Alice', 'Bob', 'Carol', 'David'],
    'Education': ['Bachelors', 'HS-grad', 'Masters', 'Doctorate']
})

high_edu = ['Bachelors', 'Masters', 'Doctorate']

# Rows WHERE education IS in the list
print(df[df['Education'].isin(high_edu)])

# Rows where education is NOT in the list (~ = NOT operator)
print(df[~df['Education'].isin(high_edu)])

# Combine with other conditions
print(df[(df['Education'].isin(high_edu)) & (df['Name'].str.startswith('A'))])


# ──────────────────────────────────────────
# SECTION 10 — MULTI-LEVEL groupby + unstack()
# ──────────────────────────────────────────

# groupby([col1, col2]) → creates a HIERARCHICAL (multi-index) Series
# .unstack() → pivots the INNER index level into COLUMNS (wide format)
# Memory Aid: groupby two cols → multi-index · unstack → flatten to table

df = pd.DataFrame({
    'Country': ['USA', 'USA', 'UK', 'UK', 'India', 'India'],
    'Salary':  ['<=50K', '>50K', '<=50K', '>50K', '<=50K', '>50K'],
    'Hours':   [40, 50, 38, 45, 42, 48]
})

# Group by two columns
result = df.groupby(['Country', 'Salary'])['Hours'].mean()
print(result)
# Country  Salary
# India    <=50K     42.0
#           >50K     48.0
# UK       <=50K     38.0
#           >50K     45.0

# unstack: turn inner level ('Salary') into columns
table = result.unstack('Salary')
print(table)
#         <=50K   >50K
# Country
# India    42.0   48.0
# UK       38.0   45.0
# USA      40.0   50.0

# Top countries by hours for >50K earners
print(table['>50K'].nlargest(2))

# stack() = opposite of unstack (wide → long format)
# reset_index() = flatten multi-index to regular columns


# ──────────────────────────────────────────
# REUSABLE SECTION C PATTERNS
# ──────────────────────────────────────────

# --- Pattern 1: Filter then Aggregate ---
# "Among rows matching condition X, find avg/max/min of Y"
def filter_and_aggregate(df, condition, value_col, agg='mean'):
    filtered = df[condition]
    return filtered[value_col].agg(agg)

# --- Pattern 2: Categorize a Numeric Column ---
def categorise_numeric(df, source_col, new_col, bins, labels):
    """Classify numeric values into named categories.
    bins:   [upper_bound_cat1, upper_bound_cat2, ...] (ascending thresholds)
    labels: ['cat1', 'cat2', 'cat3_and_above']
    """
    def classify(val):
        for threshold, label in zip(bins, labels):
            if val < threshold:
                return label
        return labels[-1]
    df[new_col] = df[source_col].apply(classify)
    return df

# --- Pattern 3: Success/Survival Rate per Group ---
def success_rate_per_group(df, group_col, target_col, success_value):
    """Success rate for each group (e.g., survival per port)."""
    return df.groupby(group_col)[target_col].apply(
        lambda s: (s == success_value).mean()
    )

# Or simpler when target is already 0/1:
# df.groupby('Embarked')['Survived'].mean()

# --- Pattern 4: Multi-Stat Named Summary ---
def summary_table(df, group_by_col):
    return df.groupby(group_by_col).agg(
        Count    = ('Hours',   'count'),
        Avg_Hrs  = ('Hours',   'mean'),
        Max_Hrs  = ('Hours',   'max'),
    ).round(2)

# --- Pattern 5: 2-Way Cross with Row Percentages ---
# For "what % of X are Y" questions
# pct_table = pd.crosstab(df['gender'], df['survived'], normalize='index') * 100


# ╔══════════════════════════════════════════════════════════╗
# ║         DAY 10 — DATA VISUALIZATION                     ║
# ╚══════════════════════════════════════════════════════════╝

# ──────────────────────────────────────────
# PLOT DECISION MAP — keyword → plot type
# ──────────────────────────────────────────

# Keyword in question            Plot type              Method
# "distribution", "spread"    →  Histogram + KDE        sns.histplot(kde=True)
# "compare distributions"      →  Boxplot                sns.boxplot(x=cat, y=val)
# "relationship", "correlation"→  Scatter / regplot      sns.regplot()
# "correlation matrix"         →  Heatmap                sns.heatmap(df.corr())
# "count of", "frequency"      →  Countplot / bar        sns.countplot()
# "proportion", "percentage"   →  Pie chart              .plot(kind='pie')
# "over time", "trend"         →  Line plot              plt.plot() / kind='line'
# "distribution + shape"       →  Violin plot            sns.violinplot()

# Standard imports & defaults
sns.set_style('whitegrid')             # cleaner background
plt.rcParams['figure.figsize'] = (10, 6)


# ──────────────────────────────────────────
# 1. HISTOGRAM — distribution of ONE numeric column
# ──────────────────────────────────────────

# When to use: "distribution of age", "spread of salary", "histogram of X"
# bins=20–30 are standard   ·   kde=True adds a smooth curve

df_sample = pd.DataFrame({'Age': np.random.normal(35, 10, 200)})

# seaborn (BEST — includes KDE)
plt.figure(figsize=(9, 5))
sns.histplot(df_sample['Age'], bins=30, kde=True, color='steelblue')
plt.axvline(df_sample['Age'].mean(), color='red', linestyle='--',
            label=f"Mean={df_sample['Age'].mean():.1f}")   # mean reference line
plt.title('Age Distribution')
plt.xlabel('Age'); plt.ylabel('Frequency')
plt.legend(); plt.tight_layout(); plt.show()

# --- Reusable template ---
def plot_distribution(df, col, bins=30, title=None):
    """Histogram + KDE + mean line for any numeric column."""
    plt.figure(figsize=(9, 5))
    sns.histplot(df[col], bins=bins, kde=True, color='steelblue')
    plt.axvline(df[col].mean(), color='red', linestyle='--',
                label=f'Mean={df[col].mean():.2f}')
    plt.title(title or f'Distribution of {col}')
    plt.xlabel(col); plt.ylabel('Frequency')
    plt.legend(); plt.tight_layout(); plt.show()

# Usage: plot_distribution(titanic, 'Age')


# ──────────────────────────────────────────
# 2. BOXPLOT — compare distributions across categories
# ──────────────────────────────────────────

# When to use: "compare Age/Salary across departments/ports/classes"
# Boxplot anatomy:
#   Box     → middle 50% of data (Q1 to Q3, the interquartile range)
#   Line    → median (50th percentile)
#   Whiskers→ extend to non-outlier min/max
#   Dots    → outliers (beyond whiskers)

df_box = pd.DataFrame({
    'Dept':   ['IT', 'HR', 'IT', 'HR', 'Finance', 'Finance', 'IT'],
    'Salary': [70000, 50000, 80000, 55000, 60000, 65000, 75000]
})

# Two columns side-by-side (no category)
# df[['ColA', 'ColB']].boxplot()

# Numeric column grouped by category
plt.figure(figsize=(8, 5))
sns.boxplot(data=df_box, x='Dept', y='Salary', palette='Set2')
plt.xticks(rotation=30)   # rotate long labels
plt.title('Salary by Department'); plt.tight_layout(); plt.show()

# --- Reusable template ---
def plot_box_by_group(df, group_col, value_col, rotate=30):
    """Boxplot: value_col distribution split by group_col."""
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x=group_col, y=value_col, palette='Set2')
    plt.xticks(rotation=rotate)
    plt.title(f'{value_col} by {group_col}')
    plt.tight_layout(); plt.show()


# ──────────────────────────────────────────
# 3. SCATTER + REGPLOT — relationship between 2 numeric variables
# ──────────────────────────────────────────

# When to use: "relationship between Age and Fare", "correlation between X and Y"
# regplot adds a REGRESSION LINE (best-fit trend line)

df_scatter = pd.DataFrame({
    'Age':  np.random.randint(20, 70, 50),
    'Fare': np.random.randint(10, 500, 50)
})

# Scatter with trend line
plt.figure(figsize=(8, 5))
sns.regplot(data=df_scatter, x='Age', y='Fare', scatter_kws={'alpha': 0.5})
plt.title('Age vs Fare with Trendline'); plt.tight_layout(); plt.show()

# With category coloring (hue)
# sns.scatterplot(data=df, x='Age', y='Fare', hue='Survived')


# ──────────────────────────────────────────
# 4. BAR / COUNTPLOT — compare categories
# ──────────────────────────────────────────

# countplot = automatic counting (just give the column)
# bar       = you provide the numeric values yourself

df_count = pd.DataFrame({'City': ['BLR', 'DEL', 'BLR', 'MUM', 'BLR', 'DEL']})

# countplot
plt.figure(figsize=(7, 4))
sns.countplot(data=df_count, x='City', palette='viridis',
              order=sorted(df_count['City'].unique()))   # consistent ordering
plt.title('Count by City'); plt.tight_layout(); plt.show()

# Horizontal bar (better for LONG category names)
df_count['City'].value_counts().plot(kind='barh', color='#58a6ff')
plt.title('City Counts'); plt.tight_layout(); plt.show()


# ──────────────────────────────────────────
# 5. PIE CHART — proportions of few categories
# ──────────────────────────────────────────

# When to use: "proportion of X", "percentage breakdown" for ≤6 categories
# For more than 6 categories, use a bar plot instead (pie becomes unreadable)

counts = df_count['City'].value_counts()
plt.figure(figsize=(7, 7))
counts.plot(
    kind='pie',
    autopct='%1.1f%%',        # show "12.5%" labels on each slice
    startangle=90,             # start from top (12 o'clock)
    colors=sns.color_palette('Set2', len(counts))
)
plt.title('City Distribution')
plt.ylabel('')                 # hide default y-label
plt.tight_layout(); plt.show()


# ──────────────────────────────────────────
# 6. LINE PLOT — trend over time / ordered index
# ──────────────────────────────────────────

# When to use: "trend over time", "sales over years", "change in X"

years  = [2019, 2020, 2021, 2022, 2023]
sales  = [120,  95,   150,  170,  200]
sales2 = [80,   110,  130,  160,  190]

plt.figure(figsize=(9, 5))
plt.plot(years, sales,  marker='o', label='Product A', color='steelblue')
plt.plot(years, sales2, marker='s', label='Product B', color='orange')
plt.title('Annual Sales Trend')
plt.xlabel('Year'); plt.ylabel('Sales (units)')
plt.legend(); plt.grid(True, alpha=0.3); plt.tight_layout(); plt.show()


# ──────────────────────────────────────────
# 7. VIOLIN PLOT — box + distribution shape combined
# ──────────────────────────────────────────

# When to use: shows BOTH median/quartiles AND distribution shape
# "Show distribution shape and median of X by Y"

df_violin = pd.DataFrame({
    'Class': [1, 1, 2, 2, 3, 3, 1, 2, 3],
    'Age':   [22, 28, 35, 40, 18, 25, 30, 45, 20]
})

plt.figure(figsize=(8, 5))
sns.violinplot(data=df_violin, x='Class', y='Age', palette='Set3')
plt.title('Age Distribution by Class'); plt.tight_layout(); plt.show()


# ──────────────────────────────────────────
# 8. HEATMAP — correlation matrix — MEMORIZE THIS RECIPE!
# ──────────────────────────────────────────

# When to use: "correlation matrix", "which variables are related"
# Color interpretation:
#   +1 (dark red)   → perfect positive correlation
#    0 (white)      → no correlation
#   -1 (dark blue)  → perfect negative correlation
#
# HEATMAP RECIPE: corr() → heatmap(annot=True, cmap='coolwarm')
# Always use annot=True and cmap='coolwarm' — the gold standard

df_heat = pd.DataFrame(
    np.random.randn(50, 4),
    columns=['Age', 'Fare', 'SibSp', 'Survived']
)
corr_matrix = df_heat.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(
    corr_matrix,
    annot=True,        # show correlation number in each cell
    fmt=".2f",         # 2 decimal places
    cmap="coolwarm",   # red = positive, blue = negative
    vmin=-1, vmax=1,   # fix color scale to full range
    linewidths=0.5,    # thin lines between cells
    square=True        # force square cells
)
plt.title('Correlation Heatmap')
plt.tight_layout(); plt.show()

# --- Reusable template ---
def plot_corr_heatmap(df, cols=None, title='Correlation Heatmap'):
    """Correlation heatmap. If cols=None, uses all numeric columns."""
    if cols is None:
        cols = df.select_dtypes(include=['number']).columns.tolist()
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[cols].corr(), annot=True, fmt='.2f',
                cmap='coolwarm', vmin=-1, vmax=1, square=True, linewidths=0.5)
    plt.title(title); plt.tight_layout(); plt.show()


# ──────────────────────────────────────────
# 9. PLOT EXTRAS — reference lines, annotations, subplots, save
# ──────────────────────────────────────────

# Reference lines on any plot
plt.axhline(y=50, color='red',   linestyle='--', label='Threshold')
plt.axvline(x=35, color='green', linestyle='-.',  label='Mean Age')

# Annotation with arrow pointing to a specific point
plt.annotate('Outlier!',
             xy=(10, 95),           # coordinates of the point
             xytext=(12, 90),       # where to put the label
             arrowprops=dict(arrowstyle='->'))

# Save plot to file
# plt.savefig('plot.png', dpi=150, bbox_inches='tight')

# Multiple subplots side-by-side
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].hist(np.random.randn(100), bins=20)
axes[0].set_title('Plot A')
axes[1].hist(np.random.randn(100), bins=20, color='orange')
axes[1].set_title('Plot B')
plt.tight_layout(); plt.show()


# ──────────────────────────────────────────
# UNIVERSAL PLOT HELPER — copy-paste for any Section C question
# ──────────────────────────────────────────

def quick_plot(df, kind, x=None, y=None, hue=None, title=''):
    """One-call wrapper for the 6 most common plot types.
    kind: 'hist' | 'box' | 'scatter' | 'count' | 'bar' | 'violin'
    """
    plt.figure(figsize=(10, 6))
    if   kind == 'hist':    sns.histplot(df[x], bins=30, kde=True)
    elif kind == 'box':     sns.boxplot(data=df, x=x, y=y, hue=hue, palette='Set2')
    elif kind == 'scatter': sns.scatterplot(data=df, x=x, y=y, hue=hue)
    elif kind == 'count':   sns.countplot(data=df, x=x, hue=hue, palette='viridis')
    elif kind == 'bar':     sns.barplot(data=df, x=x, y=y, hue=hue)
    elif kind == 'violin':  sns.violinplot(data=df, x=x, y=y, hue=hue, palette='Set3')
    plt.title(title); plt.xticks(rotation=30)
    plt.tight_layout(); plt.show()

# Usage examples (uncomment and swap df/columns):
# quick_plot(df, 'hist',    x='Age',        title='Age Distribution')
# quick_plot(df, 'box',     x='Dept', y='Salary', title='Salary by Dept')
# quick_plot(df, 'count',   x='City', hue='Gender')
# quick_plot(df, 'scatter', x='Age',  y='Fare', hue='Survived')


# ──────────────────────────────────────────
# QUICK REFERENCE CHEATSHEET — VISUALIZATION
# ──────────────────────────────────────────

# ALWAYS ADD THESE LINES TO EVERY PLOT:
# plt.title('...')
# plt.xlabel('...'); plt.ylabel('...')
# plt.xticks(rotation=30)   ← for long category labels
# plt.legend()               ← when multiple series / hue
# plt.tight_layout()         ← prevents label clipping
# plt.show()

# COLOR PALETTES:
# sns.set_style('whitegrid')           → nicer default background
# cmap='coolwarm'                      → ALWAYS use for heatmaps
# palette='Set2'  / 'Set3' / 'viridis' → for categorical plots

# PLOT DECISION (one-line):
# 1 numeric          → histplot(kde=True)
# 1 numeric × 1 cat  → boxplot(x=cat, y=val)
# 2 numerics         → regplot(x, y)
# 2 categories       → crosstab → heatmap
# 1 cat counts       → countplot
# proportions ≤6     → pie chart
# correlation matrix → heatmap(df.corr(), annot=True, cmap='coolwarm')
# time series        → plt.plot() with markers

# ============================================================
# End of Days 7–10 Notes — Good luck!
# ============================================================
