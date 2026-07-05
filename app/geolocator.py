"""
GeoLocator Engine
Priority

1. Local Database
2. OpenCellID
3. UnwiredLabs
"""

from providers.localdb import LocalDBProvider
from providers.opencellid import OpenCellIDProvider
from providers.unwired import UnwiredProvider

from cache import cache


class GeoLocator:

    def __init__(
        self,
        opencell_key=None,
        unwired_token=None,
    ):

        self.local = LocalDBProvider()

        self.opencell = OpenCellIDProvider(opencell_key)

        self.unwired = UnwiredProvider(unwired_token)

    def locate(self, body):

        cell = body["cells"][0]

        mcc = body["mcc"]
        mnc = body["mnc"]

        lac = cell.get("lac", 0)
        cid = cell.get("cid", 0)

        cache_key = "%d-%d-%d-%d" % (
            mcc,
            mnc,
            lac,
            cid,
        )

        result = cache.get(cache_key)

        if result:

            result["provider"] = "Cache"

            return result

        #
        # Local Database
        #

        result = self.local.locate(
            mcc,
            mnc,
            lac,
            cid,
        )

        if result:

            cache.set(cache_key, result)

            return result

        #
        # OpenCellID
        #

        if self.opencell.api_key:

            result = self.opencell.locate(
                mcc,
                mnc,
                lac,
                cid,
            )

            if result.get("lat"):

                location = {

                    "provider": "OpenCellID",

                    "lat": result["lat"],

                    "lon": result["lon"],

                    "accuracy": result.get(
                        "range",
                        result.get("accuracy", 0),
                    ),
                }

                cache.set(cache_key, location)

                return location

        #
        # Unwired
        #

        if self.unwired.token:

            result = self.unwired.locate(body)

            if result.get("status") == "ok":

                location = {

                    "provider": "UnwiredLabs",

                    "lat": result["lat"],

                    "lon": result["lon"],

                    "accuracy": result.get(
                        "accuracy",
                        0,
                    ),
                }

                cache.set(cache_key, location)

                return location

        return {

            "provider": None,

            "lat": 0,

            "lon": 0,

            "accuracy": 0,

        }