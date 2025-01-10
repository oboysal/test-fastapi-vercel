from fastapi import FastAPI
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/api/health")
async def health_check():
    logger.info("Health check endpoint called")
    return {"status": "healthy"}

@app.get("/api/test")
async def test():
    logger.info("Test endpoint called")
    return {"message": "Hello from FastAPI"}

# Export the FastAPI app as handler
handler = app

# Log when the module is loaded
logger.info("FastAPI application initialized")
