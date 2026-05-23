from fastapi import FastAPI
import time

app = FastAPI()
request_count = 0

@app.get("/time")
def get_time():
    global request_count
    request_count += 1
    return {"time": int(time.time())}

@app.get("/metrics")
def get_metrics():
    return {"count": request_count}
