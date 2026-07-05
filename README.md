# GeoServer

GeoServer is a Home Assistant App providing Cell Tower Geolocation services.

## Features

- FastAPI REST API
- MariaDB
- Swagger UI
- Cell Database
- OpenCellID Provider
- UnwiredLabs Provider
- Local Cache
- GPS Measurement Upload

## API

GET /

GET /api/health

GET /api/version

POST /api/upload

POST /api/locate

## Swagger

http://HOME_ASSISTANT_IP:8099/docs

## Database

MariaDB

Tables

- system
- cells
- measurements
- devices

## Version

1.0.0
