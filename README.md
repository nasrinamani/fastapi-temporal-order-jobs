# First Temporal Project: The Self-Healing Job System
I built this project to learn how to make a backend that is reliable. I used **FastAPI** for the API and **Temporal** to handle the background work. The main goal of this project is to show how a system can "heal itself" if a task fails. I'm using **Docker Compose** to run the Temporal server as recommended.

Activities are hard-coded to fail on the first two attempts to prove Temporal's built-in retry and state persistence capabilities.

## Getting Started
1. Start Temporal
2. Run worker
    ```python worker.py```
3. Start API 
    ```uvicorn main:app --reload```

## Verification of Requirements
1. Submit Job: Call POST /jobs to receive a job_id.
2. Check Status: Call GET /jobs/{job_id} to see current state.
3. Automatic Retries: The worker is programmed to fail twice. Temporal will automatically retry the task.
4. Completion: Continued polling of the GET endpoint will show the status transition from `Running` to `Order Completed` after the successful third attempt.

## AI Usage Disclosure
I used Gemini to assist with:
- Understanding what Temporal is and how the workflow/worker architecture operates.
- Understanding how to use Temporal's decorators like @workflow.defn, @workflow.run, and @workflow.query to structure the execution and state-access logic.
- Organizing the logic into separate Python modules.
- Learning how to use the `imports_passed_through` function to fix import errors within the Temporal sandbox.
- Troubleshooting workflow import requirements.
- Getting guidance on generating unique random order IDs for each job.
- Structuring documentation to ensure all requirements were addressed.
