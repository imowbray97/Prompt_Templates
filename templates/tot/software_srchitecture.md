### 🏗️ **Software Architecture ToT Prompt Template**

**Role:**
You are a senior software architect tasked with designing or improving a system. Use the Tree-of-Thought (ToT) approach to reason through multiple architectural strategies before selecting the most effective one.

---

#### 🧠 **Prompt Template**

```plaintext
You are a seasoned software architect applying the Tree-of-Thought (ToT) framework to evaluate architectural options.

Objective:  
{Briefly describe the software architecture goal or challenge.}  
(e.g., Design a scalable order management system for an e-commerce platform.)

Step 1: Thought Branch Generation  
Propose at least **3 distinct architectural strategies or patterns** to address this objective.  
These may include different architectural styles (e.g., microservices, monolith, event-driven, serverless), data storage patterns, integration approaches, etc.

Step 2: Thought Evaluation  
For each strategy, walk through its design step-by-step.  
Evaluate the following dimensions (as applicable):
- **Scalability**
- **Maintainability**
- **Performance**
- **Fault tolerance**
- **Complexity**
- **Cost implications**
- **Team experience or feasibility**

Step 3: Thought Selection  
Compare the strategies. Justify which one is the most appropriate, given the business and technical context.

Step 4: Final Architecture Output  
Present the selected architecture with:
- A high-level diagram description (if relevant)
- Key components and their responsibilities
- Technologies/tools you'd recommend
- Justification based on trade-offs
```

---

#### 📌 **Example Use Case**

**Objective:**
Design a backend architecture for a real-time chat application with millions of users.

---

**Step 1: Thought Branches**

1. **Monolithic Node.js app with WebSockets and Redis Pub/Sub**
2. **Microservices with Kafka and horizontal scaling**
3. **Serverless Functions (e.g., AWS Lambda) with DynamoDB + WebSocket API Gateway**

---

**Step 2: Evaluation**
\[Each branch walks through design, pros/cons, scalability, etc.]

---

**Step 3: Selection**
Microservices with Kafka is most aligned due to horizontal scalability, fault tolerance, and real-time event propagation.

---

**Step 4: Final Output**
Describe microservices architecture with user-service, chat-service, notification-service, Kafka event bus, Redis cache, and MongoDB storage.