### 🧠 **Generalized ToT Prompt Template**

#### 🔧 **\[Template]**

**Task Description**
You are a thoughtful and strategic problem solver. Your goal is to solve the following problem by reasoning through multiple possible approaches before choosing the most effective one.

**Problem Statement:**
`{Insert the task, problem, or question here}`

**Approach (Tree-of-Thought):**

1. **Generate Multiple Thought Branches**
   Break the problem into **at least 3 different reasoning paths or strategies**. Clearly outline each path.

2. **Evaluate Each Path**
   For each path, reason step-by-step through its logic. Identify the pros, cons, and risks.

3. **Choose the Most Promising Path**
   Compare the paths and explain which one is the most effective or optimal for solving the problem.

4. **Finalize the Answer**
   Based on the selected path, synthesize a final solution, answer, or output.

---

#### 📦 **Example (Programming Context)**

**Problem Statement:**
How can I implement a rate limiter for an API in Node.js?

**Thought Branches:**

1. **Token Bucket Algorithm using Redis**
2. **Leaky Bucket Algorithm using in-memory cache**
3. **Fixed Window Counter using middleware**

**Evaluation:**

* *Token Bucket with Redis*: Scalable, resilient to restarts, good for distributed systems, but adds latency and external dependency.
* *Leaky Bucket in-memory*: Low-latency, simple, but doesn't persist across servers or restarts.
* *Fixed Window Counter*: Easy to implement, but causes spikes at window edges.

**Selected Path:**
Token Bucket using Redis is most reliable for production systems needing distributed rate limiting.

**Final Implementation Recommendation:**
Use `rate-limiter-flexible` with Redis backend in your Express middleware setup.

---

### 🧱 Prompt Template (for Copy-Paste)

```plaintext
You are a thoughtful problem-solver using the Tree-of-Thought (ToT) approach. Break the following task into multiple solution paths, evaluate them, and choose the best one.

Task:
{Insert your task/problem/question here}

Step 1: Generate 3 or more distinct solution paths or thought branches.

Step 2: For each path, reason through it step-by-step. Discuss benefits and drawbacks.

Step 3: Compare and select the most effective solution path. Explain why.

Step 4: Provide the final answer or implementation based on that path.
```
