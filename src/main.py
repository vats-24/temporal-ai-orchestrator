from fastapi import FastAPI

app = FastAPI(
    title="AI Workflow Orchestrator"  
)


@app.get("/")
async def root():
    return {
        "status": "running"           
    }