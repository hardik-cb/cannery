from fastapi import FastAPI

# Create the FastAPI instance with metadata
app = FastAPI(
    title="Hello API",
    version="5.0.0",
    description="A simple FastAPI project that says Hello and shows API version"
)

# API endpoint: /gen
@app.get("/gen")
def say_hello():
    return {
        "message": "Hello",
        "api_version": app.version
    }
