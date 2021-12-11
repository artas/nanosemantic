import sys
import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from loguru import logger

from app.api.routes import router
from app.midleware import Logger
logger.remove()
logger.add(sys.stdout, colorize=True,
           format="<green>{time:HH:mm:ss}</green> | {level} | <level>{message}</level>")
logger.add('./logs/log.log', level="DEBUG")
app = FastAPI()

app.middleware('http')(Logger())
app.include_router(router)


@app.get("/", include_in_schema=False)
async def health() -> JSONResponse:
    return JSONResponse({"status": "ok"})


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)

