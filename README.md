# AsyncMessageBroker

A simple asynchronous producer–consumer message broker built using Python's `asyncio`.  
It demonstrates how tasks are produced, queued, and processed by multiple workers concurrently.

---

## 🚀 Features
- Multiple async producers  
- Multiple async consumers  
- FIFO task queue using `asyncio.Queue()`  
- Automatic load balancing  
- Graceful shutdown  
- Fully non-blocking and concurrent  

---

## 📌 How It Works

Producers add messages → Queue stores them → Consumers process them.

