"""
GeoServer API
"""

from .health import router as health_router
from .stats import router as stats_router
from .upload import router as upload_router
from .locate import router as locate_router
from .cells import router as cells_router
from .admin import router as admin_router