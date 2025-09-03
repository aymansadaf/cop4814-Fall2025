"""
Basic Python Syntax
----------------------------
This file is a guided template for learning Python basics.
Students should fork and clone this repository from Greg's repo.
Explanations and examples will be added by Greg.
"""

# ==========================================================
# 1. PRINTING AND COMMENTS
# ----------------------------------------------------------
# - Print statements
# - Single-line comments
# - Multi-line comments (docstrings)
# ==========================================================

print("Sadaf",3.14,18)

# ==========================================================
# 2. VARIABLES AND DATA TYPES
# ----------------------------------------------------------
# - Strings
# - Integers, floats
# - Booleans
# - Type checking with type()
# ==========================================================

message = "Welcome to FIU"

print(type(message))

a= 10
b= 2
print(type(a),type(b))

isOpen = True
print(type(isOpen))

print(message[0])

# ==========================================================
# 3. BASIC OPERATORS
# ----------------------------------------------------------
# - Arithmetic (+, -, *, /, //, %, **)
# - Comparison (==, !=, >, <, >=, <=)
# - Logical (and, or, not)
# ==========================================================

print(a+b)
print(a*b)
print(7/2)
print(7//2)
print(7%2)

# ==========================================================
# 4. STRING OPERATIONS
# ----------------------------------------------------------
# - Concatenation
# - f-strings
# - Common methods (.upper(), .lower(), .strip(), etc.)
# ==========================================================

first_name = "ayman"
last_name = "sadaf"

print(first_name+" "+last_name)
print(f"My name is {first_name.upper()} {last_name.title()}.")
print("***Welcome to Software Dev***".strip('*'))

# ==========================================================
# 5. LISTS
# ----------------------------------------------------------
# - Creating lists
# - Indexing and slicing
# - Adding/removing elements
# - Useful methods (.append(), .remove(), .sort(), etc.)
# ==========================================================

professors = ["greg","joe", "richard","johnson","jason","leo","heather"]
print(type(professors))
print(professors)
print(professors[2:4]) #accessing indices 2,3. Upper bound never included
print(professors[:5]) #accessing till place 5
print(professors[2:])
print(professors[:]) #better way to access and edit list becs original is copied and not affected.

professors.append("todd")
professors.extend(["robinson","Stockholm","mustafa"])
professors.insert(2,"vyoma")
print(professors)
x=professors.pop(2)
print(x)
professors.reverse()
print(professors)
professors.sort()
print(professors)
professors.sort(reverse=True)
print(professors)
# ==========================================================
# 6. TUPLES AND SETS
# ----------------------------------------------------------
# - Tuples: immutable sequences
# - Sets: unique collections
# ==========================================================

grades =(88.3,78.6,99.5)
print(type(grades))
# grades [0]= 91.3

members = {"greg","richard","greg"}
print(members)

# ==========================================================
# 7. DICTIONARIES
# ----------------------------------------------------------
# - Key-value pairs
# - Accessing and modifying values
# - Common methods (.keys(), .values(), .items())
# ==========================================================



# ==========================================================
# 8. CONDITIONALS
# ----------------------------------------------------------
# - if, elif, else
# - Nested conditionals
# ==========================================================



# ==========================================================
# 9. LOOPS
# ----------------------------------------------------------
# - for loops
# - while loops
# - break and continue
# ==========================================================



# ==========================================================
# 10. FUNCTIONS
# ----------------------------------------------------------
# - Defining functions
# - Parameters and return values
# - Default arguments
# ==========================================================



# ==========================================================
# 11. IMPORTING MODULES
# ----------------------------------------------------------
# - Importing built-in modules (e.g., math, random)
# - Using functions from modules
# ==========================================================



# ==========================================================
# 12. ERROR HANDLING (OPTIONAL)
# ----------------------------------------------------------
# - try, except
# - Handling different exception types
# ==========================================================



