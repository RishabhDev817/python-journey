# Python Journey 🐍

> A comprehensive, continuously evolving repository documenting my progression in Python — from foundational syntax and core logic to Data Structures & Algorithms (DSA), Object-Oriented Programming (OOP), and Machine Learning practicals.

---

## 📑 Table of Contents
1. [Data Structures & Algorithms (`DSA/`)](#-data-structures--algorithms-dsa)
2. [Machine Learning Practicals](#-machine-learning-practicals)
3. [Modular Projects & Package Architecture](#-modular-projects--package-architecture)
4. [Core Logic, Loops & Math](#-core-logic-loops--math)
5. [Data Collections (Lists, Tuples, Sets & Dictionaries)](#-data-collections-lists-tuples-sets--dictionaries)
6. [Conditionals, Strings & Utilities](#-conditionals-strings--utilities)
7. [Functions, Modules & OOP](#-functions-modules--oop)
8. [How to Run](#-how-to-run)
9. [Future Roadmap](#-future-roadmap)

---

## ⚡ Data Structures & Algorithms (`DSA/`)

This directory contains implementations of classic searching and sorting algorithms, including real-world applications of algorithmic techniques.

| File | Algorithm / Concept | Description |
| :--- | :--- | :--- |
| [`DSA/linear_search.py`](file:///Users/rishabh/Python/DSA/linear_search.py) | **Linear Search** | Iterates sequentially through an array to locate a target value and returns its index, or `-1` if absent ($O(n)$ time complexity). |
| [`DSA/binary_search.py`](file:///Users/rishabh/Python/DSA/binary_search.py) | **Binary Search (Descending)** | Implements binary search ($O(\log n)$) on a reverse-sorted list using two pointers (`left`, `right`) and midpoint checking. |
| [`DSA/Bubble_Sort.py`](file:///Users/rishabh/Python/DSA/Bubble_Sort.py) | **Bubble Sort** | Sorts an array in ascending order by repeatedly stepping through the list and swapping adjacent elements that are out of order ($O(n^2)$). |
| [`DSA/Selection_Sort.py`](file:///Users/rishabh/Python/DSA/Selection_Sort.py) | **Selection Sort** | In-place comparison sort that finds the minimum element from the unsorted part and places it at the beginning ($O(n^2)$). |
| [`DSA/Insertion_Sort.py`](file:///Users/rishabh/Python/DSA/Insertion_Sort.py) | **Insertion Sort** | Classic insertion sort that builds the final sorted array one item at a time by shifting larger elements to the right. |
| [`DSA/Insertion_Sort1.py`](file:///Users/rishabh/Python/DSA/Insertion_Sort1.py) | **Real-Time Leaderboard** | Advanced real-world application using Python's `@dataclass`. Implements live streaming score insertion into an ordered leaderboard and batch sorting using insertion sort. |
| [`DSA/Quick_Sort.py`](file:///Users/rishabh/Python/DSA/Quick_Sort.py) | **Quick Sort** | Divide-and-conquer sorting algorithm that partitions elements around a pivot into left, middle, and right sublists, achieving average $O(n \log n)$ time complexity. |

---

## 🧠 Machine Learning Practicals

End-to-end practical implementations of foundational machine learning workflows covering preprocessing, modeling, evaluation, and visualizations.

| File | Type | Description |
| :--- | :--- | :--- |
| [`machineLearning.py`](file:///Users/rishabh/Python/machineLearning.py) | **Supervised Learning** | Full **House Price Prediction** pipeline using **Linear Regression**. Includes synthetic dataset creation, Exploratory Data Analysis (EDA), feature correlation, train-test splitting, model fitting, metric evaluation (Mean Squared Error, $R^2$ score), and residual plotting. |
| [`UNSUPERVISED_LEARNING.py`](file:///Users/rishabh/Python/UNSUPERVISED_LEARNING.py) | **Unsupervised Learning** | Comprehensive practical on **K-Means Clustering**. Covers feature scaling with `StandardScaler`, finding the optimal number of clusters ($k$) via the **Elbow Method** (WCSS), fitting `KMeans`, evaluating with Silhouette Scores, and cluster visualization with centroids. |

---

## 🏗️ Modular Projects & Package Architecture

Structured, multi-file Python applications showcasing modular separation of concerns, clean code organization, and package imports.

### 📁 Text Cleaner Project (`myProject/`)
Demonstrates modular decomposition by separating utility logic into an independent module and consuming it via a main entry point.

| File | Component | Description |
| :--- | :--- | :--- |
| [`myProject/analyzer.py`](file:///Users/rishabh/Python/myProject/analyzer.py) | **Text Normalizer** | Defines `analyze_text(text)` which trims and normalizes multi-space strings into single spaces using `split()` and `join()`. |
| [`myProject/main.py`](file:///Users/rishabh/Python/myProject/main.py) | **Application Entry Point** | Imports `analyze_text` from the local `analyzer` module and executes the text-cleaning pipeline on input messages. |

### 📦 AI Text Processing Package (`ai_project/`)
Demonstrates package hierarchy with an internal `app/` subpackage containing specialized modules coordinated by a root orchestration script.

| File | Component | Description |
| :--- | :--- | :--- |
| [`ai_project/app/cleaner.py`](file:///Users/rishabh/Python/ai_project/app/cleaner.py) | **Cleaner Module** | Implements `normalize_text(text)` to sanitize irregular spacing and clean strings for downstream NLP tasks. |
| [`ai_project/app/analyzer.py`](file:///Users/rishabh/Python/ai_project/app/analyzer.py) | **Analyzer Module** | Implements `count_words(text)` to compute word counts and text statistics. |
| [`ai_project/app/init.py`](file:///Users/rishabh/Python/ai_project/app/init.py) | **Package Initialization** | Package marker for the `app` namespace. |
| [`ai_project/main.py`](file:///Users/rishabh/Python/ai_project/main.py) | **Project Pipeline** | Imports both `app.analyzer` and `app.cleaner` modules to run an end-to-end text preprocessing and word analysis pipeline. |

---

## 🔁 Core Logic, Loops & Math

Scripts focusing on fundamental control structures (`while`, `for`, `range`), arithmetic formulas, and iteration patterns.

| File | Focus | Description |
| :--- | :--- | :--- |
| [`count_up.py`](file:///Users/rishabh/Python/count_up.py) | While Loop | Prints numbers incrementally from 1 to 100 using a `while` counter. |
| [`count_down.py`](file:///Users/rishabh/Python/count_down.py) | While Loop | Decrements numbers from 100 down to 1 using a `while` loop. |
| [`range_up.py`](file:///Users/rishabh/Python/range_up.py) | `range()` Function | Generates and prints numbers from 1 to 100 using `range(1, 101)`. |
| [`range_down.py`](file:///Users/rishabh/Python/range_down.py) | Reverse `range()` | Counts backwards from 100 to 1 utilizing negative step indexing (`range(100, 0, -1)`). |
| [`factorial.py`](file:///Users/rishabh/Python/factorial.py) | Math / Loops | Computes the factorial ($n!$) of a user-supplied integer using a `for` loop accumulator. |
| [`sum_n.py`](file:///Users/rishabh/Python/sum_n.py) | Accumulator Pattern | Calculates the sum of the first $n$ natural numbers using a `while` loop. |
| [`table.py`](file:///Users/rishabh/Python/table.py) | Multiplication Table | Generates a 1-to-10 multiplication table for any input integer using a `while` loop. |
| [`range_table.py`](file:///Users/rishabh/Python/range_table.py) | Formatted Table | Generates an formatted multiplication table (`N x i = Result`) using a `for` loop and f-strings. |
| [`fibonacci.py`](file:///Users/rishabh/Python/fibonacci.py) | Fibonacci Series | Generates the Fibonacci sequence up to $n$ terms using a `for` loop with tuple swapping. |
| [`pattern_right_triangle.py`](file:///Users/rishabh/Python/pattern_right_triangle.py) | Star Pattern | Prints a left-aligned right-angled star triangle for $n$ rows using nested loops. |
| [`pattern_inverted_triangle.py`](file:///Users/rishabh/Python/pattern_inverted_triangle.py) | Star Pattern | Prints an inverted right-angled star triangle with decreasing stars per row. |
| [`pattern_pyramid.py`](file:///Users/rishabh/Python/pattern_pyramid.py) | Star Pattern | Prints a centered full pyramid star pattern using space offsetting and $(2i - 1)$ stars per row. |
| [`pattern_diamond.py`](file:///Users/rishabh/Python/pattern_diamond.py) | Star Pattern | Prints a symmetric diamond star pattern combining upper and lower triangular halves. |

---

## 📦 Data Collections (Lists, Tuples, Sets & Dictionaries)

Hands-on exercises exploring Python's built-in compound data types and their native methods.

| File | Data Structure | Description |
| :--- | :--- | :--- |
| [`list.py`](file:///Users/rishabh/Python/list.py) | List Manipulation | Prompts the user for favorite movie names and dynamically populates a list using `.append()`. |
| [`list_len.py`](file:///Users/rishabh/Python/list_len.py) | List Sizing | Defines a function to compute and display the total length of any passed list. |
| [`for_list.py`](file:///Users/rishabh/Python/for_list.py) | List Traversal | Demonstrates clean for-in iteration over a list of square numbers. |
| [`print_list.py`](file:///Users/rishabh/Python/print_list.py) | Index Traversal | Iterates through list indices manually using a `while` loop and boundary check. |
| [`print_elements.py`](file:///Users/rishabh/Python/print_elements.py) | Custom Traversal | Function that prints list elements inline separated by spaces using `print(element, end=' ')`. |
| [`sort.py`](file:///Users/rishabh/Python/sort.py) | List Sorting | Uses the in-place `.sort()` method to alphabetically organize a list of student letter grades. |
| [`palindrome.py`](file:///Users/rishabh/Python/palindrome.py) | List Reversal | Validates whether a list is a palindrome by comparing a cloned copy with its reversed version (`.copy()` and `.reverse()`). |
| [`tuple.py`](file:///Users/rishabh/Python/tuple.py) | Tuples & Counting | Counts occurrences of an element (e.g. grade "A") within an immutable tuple using `.count()`. |
| [`tuple_search.py`](file:///Users/rishabh/Python/tuple_search.py) | Tuple Search | Searches for a specific value in a tuple using index tracking in a `while` loop. |
| [`for_search.py`](file:///Users/rishabh/Python/for_search.py) | Search with Flag | Searches for a number in a tuple using a `for` loop with a boolean `found` flag. |
| [`set.py`](file:///Users/rishabh/Python/set.py) | Sets & Uniqueness | Eliminates duplicate subject entries by casting a list to a `set` to determine the unique number of classrooms needed. |
| [`unique.py`](file:///Users/rishabh/Python/unique.py) | Set Data Types | Highlights how sets preserve distinct values (such as `"9"` vs `"9.0"`). |
| [`unique_words.py`](file:///Users/rishabh/Python/unique_words.py) | Unique Words Finder | Extracts unique words from a string by normalizing casing, stripping punctuation, and leveraging set uniqueness. |
| [`set_operations.py`](file:///Users/rishabh/Python/set_operations.py) | Set Operations | Demonstrates union (`|`), intersection (`&`), difference (`-`), and symmetric difference (`^`) between sets. |
| [`anagram_check.py`](file:///Users/rishabh/Python/anagram_check.py) | Anagram & Set Analysis | Checks if two strings are anagrams using sorted character matching and compares unique character sets. |
| [`vowel_counter.py`](file:///Users/rishabh/Python/vowel_counter.py) | Vowels & Set Intersection | Identifies unique vowels in a sentence via set intersection with `{'a', 'e', 'i', 'o', 'u'}` and calculates vowel frequencies. |
| [`char_frequency.py`](file:///Users/rishabh/Python/char_frequency.py) | Character Frequency | Computes the occurrence frequency for each unique character extracted from a string using sets. |
| [`dictonary.py`](file:///Users/rishabh/Python/dictonary.py) | Dictionaries | Key-value store mapping words to their definitions and demonstrating dictionary lookups. |
| [`empty_dictonary.py`](file:///Users/rishabh/Python/empty_dictonary.py) | Dynamic Dictionary | Interactively builds a student grade-book dictionary by taking subject-score pairs from user input. |

---

## 🔤 Conditionals, Strings & Utilities

Entry-level exercises on basic arithmetic, conditional branches (`if`/`elif`/`else`), string operations, and conversions.

| File | Topic | Description |
| :--- | :--- | :--- |
| [`hello.py`](file:///Users/rishabh/Python/hello.py) | Hello World | Standard first program to verify Python runtime environment. |
| [`sum.py`](file:///Users/rishabh/Python/sum.py) | Addition | Takes two float inputs and calculates their sum. |
| [`avg.py`](file:///Users/rishabh/Python/avg.py) | Average | Takes two numbers and calculates their arithmetic mean. |
| [`sqArea.py`](file:///Users/rishabh/Python/sqArea.py) | Geometry Formula | Calculates the area of a square from a user-provided side length ($area = side^2$). |
| [`string.py`](file:///Users/rishabh/Python/string.py) | String Syntax | Demonstrates single, double, and triple-quoted multiline string literals in Python. |
| [`length.py`](file:///Users/rishabh/Python/length.py) | String Length | Computes and displays the length of a string using `len()`. |
| [`dollarCount.py`](file:///Users/rishabh/Python/dollarCount.py) | Substring Count | Counts total occurrences of the `$` symbol in an input string using `.count('$')`. |
| [`even_odd.py`](file:///Users/rishabh/Python/even_odd.py) | Modulo Operator | Determines whether an input integer is even or odd using the `% 2` condition. |
| [`multiple7.py`](file:///Users/rishabh/Python/multiple7.py) | Divisibility Test | Checks if a given number is divisible by 7 using the modulo operator. |
| [`greaterORequal.py`](file:///Users/rishabh/Python/greaterORequal.py) | Relational Logic | Compares two numbers to determine if the first is greater than or equal to the second. |
| [`greatest_num.py`](file:///Users/rishabh/Python/greatest_num.py) | Nested Conditionals | Evaluates three input numbers and determines the maximum among them. |
| [`usd_to_inr.py`](file:///Users/rishabh/Python/usd_to_inr.py) | Currency Converter | Function that converts United States Dollars (USD) to Indian Rupees (INR) based on a conversion multiplier. |

---

## 🏛️ Functions, Modules & OOP

| File | Topic | Description |
| :--- | :--- | :--- |
| [`arr.py`](file:///Users/rishabh/Python/arr.py) | Default Arguments | Demonstrates function definitions with default parameter values (`def fun(x, y=3):`). |
| [`abstract_class.py`](file:///Users/rishabh/Python/abstract_class.py) | Abstract Base Classes | Demonstrates Object-Oriented Programming (OOP) abstraction using Python's `abc` module (`ABC`, `@abstractmethod`). |
| [`Calculator.py`](file:///Users/rishabh/Python/Calculator.py) | Custom Module | Implements reusable arithmetic utility functions designed for modular import across scripts. |
| [`add.py`](file:///Users/rishabh/Python/add.py) | Module Imports | Demonstrates importing specific functions from a local module (`from Calculator import add`) and invoking them. |

---

## 🚀 How to Run

Ensure you have Python 3 installed. You can run any script directly from the root directory:

```bash
# Run basic scripts
python3 hello.py
python3 factorial.py
python3 fibonacci.py

# Run star pattern programs
python3 pattern_right_triangle.py
python3 pattern_inverted_triangle.py
python3 pattern_pyramid.py
python3 pattern_diamond.py

# Run set and string processing programs
python3 unique_words.py
python3 set_operations.py
python3 anagram_check.py
python3 vowel_counter.py
python3 char_frequency.py

# Run modular scripts & imports
python3 add.py

# Run Data Structures & Algorithms
python3 DSA/binary_search.py
python3 DSA/Insertion_Sort1.py
python3 DSA/Quick_Sort.py

# Run modular project pipelines
python3 myProject/main.py
python3 ai_project/main.py

# Run Machine Learning scripts (requires scikit-learn, pandas, matplotlib)
python3 machineLearning.py
python3 UNSUPERVISED_LEARNING.py
```

---

## 🗺️ Future Roadmap
- [ ] Recursion and Backtracking problems
- [ ] Stacks, Queues, and Linked Lists in Python
- [ ] Object-Oriented Design Patterns
- [ ] Deep Learning / Neural Network fundamentals
- [x] Modular project architecture & package structure (`ai_project/`, `myProject/`)
- [ ] Mini project integrations (CLI tools, APIs with FastAPI/Flask)
