"""
Health API
"""

from datetime import datetime
from fastapi import APIRouter

from config import Config

router = APIRouter()


@router.get("/api/health")
def health():

    return {

        "status": "ok",

        "version": Config.VERSION,

        "time": datetime.utcnow().isoformat(),

        "database": {

            "host": Config.DB_HOST,

            "port": Config.DB_PORT,

            "name": Config.DB_NAME

        }

    }


@router.get("/api/version")
def version():

    return {

        "version": Config.VERSION

    }


@router.get("/api/info")
def info():

    return {

        "project": "GeoServer",

        "framework": "FastAPI",

        "database": "MariaDB",

        "providers": [

            "Local",

            "OpenCellID",

            "UnwiredLabs"

        ]

    }