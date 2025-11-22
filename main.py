import asyncio
import random


async def consumer(queue, name):
    while True:
        item = await queue.get()
        print(f"{name} processing {item}")
        await asyncio.sleep(random.uniform(0.3, 0.6))
        queue.task_done()


async def producer(queue, name, num_items=5):
    for i in range(num_items):
        await asyncio.sleep(random.uniform(0.1, 0.5))
        item = f"image_{i} from {name}"
        await queue.put(item)
        print(f"{name} added {item}")
    print(f"{name} finished producing")


async def main():
    q = asyncio.Queue()


    producer_tasks = [
        asyncio.create_task(producer(q, f"Producer-{i}")) for i in range(2)
    ]


    consumer_tasks = [
        asyncio.create_task(consumer(q, f"Consumer-{i}")) for i in range(3)
    ]

    await asyncio.gather(*producer_tasks)


    await q.join()


    for c in consumer_tasks:
        c.cancel()

    print("All tasks completed!")

asyncio.run(main())
