"""
GeoServer Helper Functions
"""

import time
import hashlib
import json


def now():

    return int(time.time())


def now_ms():

    return int(time.time() * 1000)


def md5(text):

    return hashlib.md5(

        str(text).encode()

    ).hexdigest()


def make_cache_key(mcc, mnc, lac, cid):

    return "%d-%d-%d-%d" % (

        mcc,

        mnc,

        lac,

        cid

    )


def json_dump(data):

    return json.dumps(

        data,

        ensure_ascii=False,

        indent=4

    )