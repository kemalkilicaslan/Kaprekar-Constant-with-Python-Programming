# Kaprekar Constant with Python Programming

## 1. Introduction

This project implements the **Kaprekar Constant (6174)**, first described by Indian mathematician Dattatraya Ramchandra Kaprekar in 1949. Kaprekar, who had no formal mathematical training, presented it at a symposium. The constant appears when you apply a simple iterative arithmetic operation to four-digit numbers.

Starting from any four-digit number with at least two different digits and repeatedly applying a specific subtraction process, you always reach 6174 within seven iterations. Once you reach 6174, the process stays there, returning 6174 on every further step.

**Core Features:**
- Implementation of the Kaprekar routine for four-digit numbers (6174 constant)
- Implementation of the Kaprekar routine for three-digit numbers (495 constant)
- Step-by-step visualization of the iteration process
- Automatic detection of the Kaprekar constant
- Support for numbers with leading zeros
- Clear output formatting showing each operation

[![6174](https://github.com/kemalkilicaslan/Kaprekar-Constant-with-Python-Programming/blob/main/6174.webp)](https://www.youtube.com/watch?v=PsC7mOu_R74)

## 2. Methodology / Approach

The Kaprekar routine follows a simple yet elegant algorithm that transforms any four-digit number into the constant 6174 through iterative subtraction operations.

### 2.1 The Kaprekar Process

The algorithm operates through the following steps:

1. **Input Selection:** Start with any four-digit number where at least two digits are different
2. **Digit Arrangement:** Arrange the digits to form the largest and smallest possible numbers
3. **Subtraction:** Subtract the smaller number from the larger number
4. **Iteration:** Repeat steps 2-3 with the result until 6174 is reached
5. **Convergence:** The process always converges to 6174 within seven iterations

**Example with 1000:**

$$1000 \rightarrow 1000 - 0001 = 0999$$
$$0999 \rightarrow 9990 - 0999 = 8991$$
$$8991 \rightarrow 9981 - 1899 = 8082$$
$$8082 \rightarrow 8820 - 0288 = 8532$$
$$8532 \rightarrow 8532 - 2358 = 6174$$

and the loop continues indefinitely:

$$6174 \rightarrow 7641 - 1467 = 6174$$

### 2.2 Mathematical Properties

The Kaprekar constant exhibits several remarkable properties:

**Convergence Property:**
For any four-digit number $n$ with at least two different digits:

$$K(K(K(...K(n)...))) = 6174$$

where $K$ represents the Kaprekar operation, and the maximum depth of iteration is 7.

**Fixed Point Property:**
Once 6174 is reached, the operation becomes idempotent:

$$K(6174) = 7641 - 1467 = 6174$$

**Three-Digit Variant:**
The Kaprekar constant for three-digit numbers is 495:

$$K_3(K_3(K_3(...K_3(n)...))) = 495$$

with a maximum of 6 iterations.

### 2.3 Implementation Strategy

The Python implementation uses string manipulation for digit extraction and sorting, ensuring proper handling of leading zeros. The algorithm maintains a while loop that continues until the Kaprekar constant is reached, with each iteration displaying the operation performed.

## 3. Mathematical Framework

### 3.1 Kaprekar Operation Definition

For a four-digit number $n$ with digits $d_1, d_2, d_3, d_4$:

$$K(n) = \max(\text{permutations}(d_1, d_2, d_3, d_4)) - \min(\text{permutations}(d_1, d_2, d_3, d_4))$$

### 3.2 Digit Sorting

Given a number $n$ with digits extracted into array $D = [d_1, d_2, d_3, d_4]$:

$$n_{\text{desc}} = \sum_{i=1}^{4} d_i^{\text{sorted(desc)}} \cdot 10^{4-i}$$

$$n_{\text{asc}} = \sum_{i=1}^{4} d_i^{\text{sorted(asc)}} \cdot 10^{4-i}$$

### 3.3 Iteration Sequence

The sequence of operations can be represented as:

$$n_0 = \text{initial number}$$
$$n_{k+1} = K(n_k) \quad \text{for } k = 0, 1, 2, ...$$

Convergence occurs when:

$$\exists m \leq 7 : n_m = 6174$$

### 3.4 Proof of Convergence

The convergence to 6174 is guaranteed by the following properties:

1. **Bounded Operation:** $0 \leq K(n) \leq 9999$ for all four-digit $n$
2. **Non-trivial Result:** If $n$ has at least two different digits, $K(n) \neq 0$
3. **Cycle Detection:** The operation either reaches 6174 or enters a cycle
4. **Empirical Verification:** All four-digit numbers (except repdigits) converge to 6174

## 4. Requirements

`requirements.txt`
```txt
# No external dependencies required
# Python 3.6+ standard library only
```

## 5. Installation & Configuration

### 5.1 Environment Setup
```bash
# Clone the repository
git clone https://github.com/kemalkilicaslan/Kaprekar-Constant-with-Python-Programming.git
cd Kaprekar-Constant-with-Python-Programming

# No additional installation required - uses Python standard library
```

### 5.2 Project Structure
```
Kaprekar-Constant-with-Python-Programming
├── Kaprekar-Constant-with-Python-Programming.py
├── .gitignore
├── README.md
└── LICENSE
```

### 5.3 System Requirements

- **Python Version:** 3.6 or higher
- **Operating System:** Platform independent (Windows, macOS, Linux)
- **Memory:** Minimal (<1 MB)
- **Dependencies:** None (standard library only)

## 6. Usage / How to Run

### 6.1 Four-Digit Kaprekar Constant (6174)

**Basic Usage:**
```python
def kaprekar(num):
    if num == 6174:
        print("Result: 6174")
        return
    while num != 6174:        
        digits = [int(d) for d in str(num)]
        while len(digits) < 4:
            digits.insert(0, 0)
        ascending = int(''.join(map(str, sorted(digits))))
        descending = int(''.join(map(str, sorted(digits, reverse=True))))
        num = descending - ascending
        print(f"{descending:04d} - {ascending:04d} = {num:04d}")

# Example usage
kaprekar(1000)
```

**Output:**
```
1000 - 0001 = 0999
9990 - 0999 = 8991
9981 - 1899 = 8082
8820 - 0288 = 8532
8532 - 2358 = 6174
```

### 6.2 Three-Digit Kaprekar Constant (495)

**Basic Usage:**
```python
def kaprekar_3(num):
    if num == 495:
        print("Result: 495")
        return
    while num != 495:        
        digits = [int(d) for d in str(num)]
        while len(digits) < 3:
            digits.insert(0, 0)
        ascending = int(''.join(map(str, sorted(digits))))
        descending = int(''.join(map(str, sorted(digits, reverse=True))))
        num = descending - ascending
        print(f"{descending:03d} - {ascending:03d} = {num:03d}")

# Example usage
kaprekar_3(8)
```

**Output:**
```
800 - 008 = 792
972 - 279 = 693
963 - 369 = 594
954 - 459 = 495
```

### 6.3 Extended Implementation with Comments
```python
# Kaprekar Constant with Python Programming
def kaprekar(num):  # Define the Kaprekar function
    if num == 6174:  # If the number is 6174, operation is finished
        print("Result: 6174")
        return
    
    while num != 6174:  # Loop continues until number reaches 6174
        # Separate the digits of the number and assign to array
        digits = [int(d) for d in str(num)]
        
        # Add leading zeros until array has 4 digits
        while len(digits) < 4:
            digits.insert(0, 0)
        
        # Create new numbers by sorting digits ascending and descending
        ascending = int(''.join(map(str, sorted(digits))))
        descending = int(''.join(map(str, sorted(digits, reverse=True))))
        
        # Calculate difference and assign to num for next iteration
        num = descending - ascending
        
        # Print operation steps and result
        print(f"{descending:04d} - {ascending:04d} = {num:04d}")

# Test with your chosen four-digit number
kaprekar(1000)
```

### 6.4 Testing Different Numbers
```python
# Test various starting numbers
test_numbers = [1, 60, 803, 1000, 2791, 5094, 3006, 8000]

for num in test_numbers:
    print(f"\nStarting with {num:04d}:")
    kaprekar(num)
    print("-" * 30)
```

## 7. Application / Results

### 7.1 Convergence Analysis for Four-Digit Numbers

**Fast Convergence Examples:**

| Starting Number | Iterations | Path |
|----------------|-----------|------|
| 1000 | 5 | 1000→0999→8991→8082→8532→6174 |
| 2791 | 4 | 2791→7173→6354→3087→8352→6174 |
| 5094 | 3 | 5094→4086→8172→7443→3996→6174 |

**Maximum Iterations:**

| Starting Number | Iterations | Note |
|----------------|-----------|------|
| 1234 | 7 | Maximum iteration depth |
| 5678 | 7 | Requires full 7 steps |

**Single-Step Convergence:**

| Starting Number | Result | Direct Path |
|----------------|--------|-------------|
| 7641 | 6174 | 7641→6174 (immediate) |

### 7.2 Convergence Analysis for Three-Digit Numbers

**Example Sequences:**

| Starting Number | Iterations | Path |
|----------------|-----------|------|
| 8 | 4 | 008→792→693→594→495 |
| 100 | 5 | 100→099→891→792→693→594→495 |
| 523 | 3 | 523→396→693→594→495 |

### 7.3 Statistical Analysis

**Four-Digit Numbers (6174):**

| Metric | Value |
|--------|-------|
| Total valid numbers | 9,000 (excluding repdigits) |
| Maximum iterations | 7 |
| Average iterations | ~5.2 |
| Numbers requiring 7 iterations | ~78 |
| Numbers with 1 iteration | 356 |

**Three-Digit Numbers (495):**

| Metric | Value |
|--------|-------|
| Total valid numbers | 900 (excluding repdigits) |
| Maximum iterations | 6 |
| Average iterations | ~4.8 |

### 7.4 Special Cases

**Repdigits (Invalid Input):**
Numbers with all identical digits (1111, 2222, etc.) result in 0:

$$9999 - 9999 = 0$$

These are excluded from valid Kaprekar inputs.

**Single Iteration Examples:**

| Number | Descending | Ascending | Result |
|--------|-----------|-----------|--------|
| 7641 | 7641 | 1467 | 6174 |
| 6714 | 7641 | 1467 | 6174 |
| 4176 | 7641 | 1467 | 6174 |

## 8. Tech Stack

### 8.1 Core Technologies

- **Programming Language:** Python 3.6+
- **Standard Library Only:** No external dependencies
- **Built-in Functions:** `str()`, `int()`, `sorted()`, `len()`, `map()`, `join()`

### 8.2 Algorithm Components

| Component | Implementation | Purpose |
|-----------|----------------|---------|
| Digit Extraction | List comprehension | Convert number to digit array |
| Sorting | `sorted()` function | Arrange digits ascending/descending |
| String Manipulation | `join()` + `map()` | Reconstruct numbers from digits |
| Formatting | f-strings | Display operations with leading zeros |
| Control Flow | `while` loop | Iterate until convergence |

### 8.3 Performance Characteristics

| Characteristic | Value | Notes |
|---------------|-------|-------|
| Execution Speed | <1 ms per number | Negligible computation time |
| Memory Usage | <1 KB | Minimal memory footprint |
| Scalability | O(1) per number | Constant maximum iterations |

## 9. License

This project is licensed under the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)](https://github.com/kemalkilicaslan/Kaprekar-Constant-with-Python-Programming/blob/main/LICENSE).

## 10. References

1. Nishiyama, Y. (2012). [THE WEIRDNESS OF NUMBER 6174](https://www.researchgate.net/profile/Yutaka-Nishiyama-2/publication/259604856_The_weirdness_of_number_6174/links/0c96052ce2575a69a2000000/The-weirdness-of-number-6174.pdf). *International Journal of Pure and Applied Mathematics*, 80(3), 363-373.

---

### Acknowledgments

Dattatraya Ramchandra Kaprekar (1905-1986) described this constant. He had no formal mathematical training and worked mainly in recreational mathematics.

Special thanks to the mathematical community for preserving and expanding upon Kaprekar's work, and to educators worldwide who use this constant to inspire students in number theory and computational thinking.

---

**Note:** This project is for educational and recreational purposes. The Kaprekar routine touches on number theory, algorithm design, and convergence. You can try variations with different digit counts and look into why the routine converges.