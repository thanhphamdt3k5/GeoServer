# GeoServer Documentation

## Overview

GeoServer is a Home Assistant App that provides Cell Tower Geolocation services.

The server stores GSM/LTE/NR cell information in MariaDB and exposes REST APIs for uploading measurements and locating devices.

---

## Architecture

```
GPS Tracker
      │
      │ HTTP / TCP
      ▼
 GeoServer
      │
      ├── FastAPI
      ├── SQLAlchemy
      ├── MariaDB
      ├── Local Cell Database
      ├── OpenCellID
      └── UnwiredLabs
```

---

## REST API

### Health

GET

```
/api/health
```

Response

```json
{
    "status":"ok"
}
```

---

### Version

GET

```
/api/version
```

---

### Upload

POST

```
/api/upload
```

Upload GPS + Cell measurements.

---

### Locate

POST

```
/api/locate
```

Return latitude, longitude and accuracy.

---

## Database

Tables

```
system

devices

cells

measurements

cache
```

---

## Swagger

```
http://HOME_ASSISTANT_IP:8099/docs
```

---

## Version

Current Version

```
1.0.0
```