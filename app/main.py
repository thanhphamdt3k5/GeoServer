"""
GeoServer v1.0.0
Main Application
"""

import os
from datetime import datetime

from fastapi import FastAPI

from database import create_database

from api.health import router as health_router
from api.stats import router as stats_router
from api.upload import router as upload_router
from api.locate import router as locate_router
from api.cells import router as cells_router
from api.admin import router as admin_router
from api.system import router as system_router
from api.ping import router as ping_router

VERSION = "1.0.0"

app = FastAPI(
    title="GeoServer",
    description="Cell Tower Geo Location Server",
    version=VERSION,
    docs_url="/docs",
    redoc_url="/redoc"
)

#
# Register API
#

app.include_router(health_router)
app.include_router(stats_router)
app.include_router(upload_router)
app.include_router(locate_router)
app.include_router(cells_router)
app.include_router(admin_router)
app.include_router(system_router)
app.include_router(ping_router)


@app.on_event("startup")
async def startup():

    print("=" * 60)
    print(" GeoServer v%s" % VERSION)
    print("=" * 60)

    print("Database")

    print(" Host :", os.getenv("DB_HOST"))
    print(" Port :", os.getenv("DB_PORT"))
    print(" User :", os.getenv("DB_USER"))
    print(" Name :", os.getenv("DB_NAME"))

    print()

    print("Creating database tables...")

    create_database()

    print("Database OK")

    print("=" * 60)


@app.get("/")
def root():

    return {

        "project": "GeoServer",

        "version": VERSION,

        "status": "running",

        "time": datetime.utcnow().isoformat()

    }