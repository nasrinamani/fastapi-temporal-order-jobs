# as engine like the background process that actually runs the code

import asyncio
from temporalio.client import Client
from temporalio.worker import Worker
from workflow import orderWorkflow
from activities import cookActivity

async def main():

    client = await Client.connect("localhost:7233") # temporal server

    worker = Worker(
        client,
        task_queue = "task",
        workflows = [orderWorkflow],
        activities = [cookActivity],
    )

    print("\nWaiting for order...\n")
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())