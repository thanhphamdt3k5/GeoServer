"""
System API
"""

import os

from fastapi import APIRouter

router = APIRouter()


@router.get("/api/system")
def system():

    return {

        "name": "GeoServer",

        "version": "1.0.0",

        "python": os.sys.version,

        "database": os.getenv("DB_HOST"),

        "status": "running"

    }