import time

from fastapi import FastAPI, Request

from database.db import Base, engine
from models.employee import Employee
from routers.employees import router as employee_router

from utils.logger import logger


# =========================================================
# DATABASE TABLE CREATION
# =========================================================

Base.metadata.create_all(
    bind=engine
)


# =========================================================
# FASTAPI APP
# =========================================================

app = FastAPI(
    title="Employee Management API",
    version="1.0.0"
)


# =========================================================
# REQUEST LOGGING MIDDLEWARE
# =========================================================

@app.middleware("http")
async def logging_middleware(
    request: Request,
    call_next
):

    start_time = time.time()

    logger.info(
        "Request started | %s %s",
        request.method,
        request.url.path
    )

    try:

        response = await call_next(request)

        process_time = (
            time.time() - start_time
        )

        logger.info(
            "Request completed | %s %s | "
            "status=%s | time=%.4fs",
            request.method,
            request.url.path,
            response.status_code,
            process_time
        )

        return response

    except Exception:

        process_time = (
            time.time() - start_time
        )

        logger.exception(
            "Request failed | %s %s | "
            "time=%.4fs",
            request.method,
            request.url.path,
            process_time
        )

        raise


# =========================================================
# ROUTER
# =========================================================

app.include_router(
    employee_router
)


# =========================================================
# ROOT
# =========================================================

@app.get("/")
def root():

    logger.info(
        "Root endpoint called"
    )

    return {
        "message": "Employee Management API is running"
    }