# 🧮 Assignment 3 - Understanding Algorithm Efficiency and Scalability

## 📘 Overview
This project explores and compares the efficiency and scalability of two core algorithmic techniques:

1. **Randomized Quicksort** – a divide-and-conquer sorting algorithm that uses random pivot selection to ensure stable average-case performance.  
2. **Hashing with Chaining** – a dynamic hash table implementation that supports efficient insert, search, and delete operations with collision handling.

Both algorithms were implemented in Python and tested empirically to compare their theoretical and observed performance.

---

## ⚙️ How to Run

### ▶️ Part 1: Randomized Quicksort
1. Open a terminal in the project directory.  
2. Run the script:
   ```bash
   python randomized_quicksort.py
   ```
3. Enter array sizes and input types when prompted.  
4. The script prints benchmark results and saves them to `results.csv`.

### ▶️ Part 2: Hashing with Chaining
1. Run the hash table script:
   ```bash
   python hashing_with_chaining.py
   ```
2. Use the interactive menu to:
   - Insert, search, and delete key-value pairs.
   - Display the current hash table structure and load factor.
3. The table automatically resizes when the load factor exceeds **0.75**.

---

## 📊 Summary of Findings
- **Randomized Quicksort** achieved stable **O(n log n)** performance across all input types.  
- **Deterministic Quicksort** performed similarly but is more sensitive to sorted inputs.  
- **Hashing with Chaining** maintained **O(1)** average performance for insert, search, and delete operations.  
- **Dynamic resizing** ensured low load factor and sustained efficiency even under heavy data loads.

---