### 💻 Programming-Centric CoT Prompt Template

> **🧩 Task:** {Clearly state the programming challenge or request}
>
> **📂 Context:**
> {Insert relevant information such as language, code snippet, expected output, constraints, or observed behavior}
>
> **🧠 Let’s think step by step.**
>
> **Step 1:** Understand the problem or expected behavior.
> **Step 2:** Analyze the provided code or logic line by line.
> **Step 3:** Identify any issues, inefficiencies, or logic gaps.
> **Step 4:** Propose a fix, refactor, or better solution.
>
> **✅ Final Answer:**
> \[Present the corrected or optimized code, explanation, or output]

---

### 🧪 Example: Debugging a Python Function

> **🧩 Task:** Fix the `calculate_total` function so it correctly sums a list of prices, ignoring any `None` values.
>
> **📂 Context:**
>
> ```python
> def calculate_total(prices):
>     total = 0
>     for price in prices:
>         total += price
>     return total
>
> print(calculate_total([10.5, None, 8.0]))
> ```
>
> It throws a `TypeError`.
>
> **🧠 Let’s think step by step.**
>
> **Step 1:** The function is trying to add `None` to a number, which causes the error.
> **Step 2:** We need to filter out `None` values during iteration.
> **Step 3:** We can use a condition: `if price is not None:`
> **Step 4:** Modify the loop to skip invalid values.
>
> **✅ Final Answer:**
>
> ```python
> def calculate_total(prices):
>     total = 0
>     for price in prices:
>         if price is not None:
>             total += price
>     return total
>
> print(calculate_total([10.5, None, 8.0]))  # Output: 18.5
> ```

---

### 🛠 Use Cases You Can Plug Into This Template

| Use Case                         | How to Use the Template                                                        |
| -------------------------------- | ------------------------------------------------------------------------------ |
| **Debugging Code**               | Provide faulty code, describe the error, and apply step-by-step analysis.      |
| **Explaining Code**              | Ask the model to walk through the logic and explain what each line/block does. |
| **Optimizing Code**              | Supply working code and ask for performance or readability improvements.       |
| **Converting Between Languages** | Provide source code and request a translation, step by step.                   |
| **Writing from Scratch**         | Describe the problem to solve, ask for pseudocode and final implementation.    |
