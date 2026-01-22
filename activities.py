#to do specific tasks

from temporalio import activity

@activity.defn
async def cookActivity(item: str) -> str:

    attempt = activity.info().attempt #track retries
    print(f"\nPreparing {item} attempt {attempt}")

    # Simulate a temporary system glitch
    if attempt < 3:

        print("-"*40)
        print(f"\n[Attempt {attempt}] Kitchen has issue. Retry...\n")
        raise RuntimeError(" Kitchen error")
    
    return f"[Attempt {attempt}] {item} is ready!"