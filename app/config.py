"""
GeoServer Configuration
"""

import os


class Config:

    VERSION = "1.0.0"

    APP_NAME = "GeoServer"

    DB_HOST = os.getenv("DB_HOST", "core-mariadb")

    DB_PORT = int(os.getenv("DB_PORT", "3306"))

    DB_USER = os.getenv("DB_USER", "geoserver")

    DB_PASSWORD = os.getenv("DB_PASSWORD", "geoserver")

    DB_NAME = os.getenv("DB_NAME", "geoserver")

    LOG_LEVEL = os.getenv("LOG_LEVEL", "info")

    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://%s:%s@%s:%d/%s"
        % (
            DB_USER,
            DB_PASSWORD,
            DB_HOST,
            DB_PORT,
            DB_NAME,
        )
    )