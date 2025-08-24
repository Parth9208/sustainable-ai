import time

def retry_action(action_func, max_retries=3, delay=2, *args, **kwargs):
   
    for attempt in range(1, max_retries + 1):
        try:
            result = action_func(*args, **kwargs)
            return result
        except Exception as e:
            print(f"[RETRY] Attempt {attempt} failed: {e}")
            if attempt < max_retries:
                time.sleep(delay)
            else:
                print("[RETRY] All attempts failed.")
                raise
