from fastapi import FastAPI
from temporalio.client import Client
from workflow import orderWorkflow
import random

app = FastAPI()

@app.post("/jobs")
async def placeOrder(item: str):

    client = await Client.connect("localhost:7233") #refresh
    orderId = f"Order-{random.randint(1000, 9999)}"

    await client.start_workflow(
        orderWorkflow.run,
        item,
        id = orderId,
        task_queue = "task",
    )

    return {
        "job_id": orderId, 
        "status": "Running"
    }

@app.get("/jobs/{job_id}")
async def checkStatus(job_id: str):
    
    client = await Client.connect("localhost:7233") #refresh
    handle = client.get_workflow_handle(job_id)

    info = await handle.query(orderWorkflow.getStatus)
    return {
        "job_id": job_id, 
        **info
    }