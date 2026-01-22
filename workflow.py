# as blueprint that handles the logic like sequence of activity

from datetime import timedelta
from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from activities import cookActivity

@workflow.defn
class orderWorkflow:
    def __init__(self):
        self._status = "Running"
        self._result = None

    @workflow.run
    async def run(self, item: str) -> str:
        self._status = "Preparing Order"

        self._result = await workflow.execute_activity(
            cookActivity,
            item,
            start_to_close_timeout=timedelta(seconds = 10)
        )

        self._status = "Order Completed"
        return self._result
    
    @workflow.query
    def getStatus(self):
        return {
            "status": self._status,
            "progress": {
                "stage": "kitchen", 
                "attempt": 3 #just to check
                },
            "result": self._result,
            "error": None
        }