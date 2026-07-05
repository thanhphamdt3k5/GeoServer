"""
ATParser v3.0

Supported Modules

- EC200
- EC600
- EG91
- EG95
- BG95
- BG96
- RM500
- RM502
"""

import json
import re


class ATParser:

    _serving = {}

    _neighbour = []

    @classmethod
    def clear(cls):

        cls._serving = {}

        cls._neighbour = []

    @classmethod
    def load(cls, data):

        """
        data = dict()
        """

        cls.clear()

        cls._serving = data.get("serving", {})

        cls._neighbour = data.get("neighbour", [])

    @classmethod
    def fromJSON(cls, text):

        cls.load(json.loads(text))

    @classmethod
    def toJSON(cls):

        return json.dumps(

            {

                "serving": cls._serving,

                "neighbour": cls._neighbour

            }

        )

    @classmethod
    def serving(cls):

        return cls._serving

    @classmethod
    def neighbour(cls):

        return cls._neighbour

    @classmethod
    def getQuality(cls):

        rsrp = cls._serving.get("rsrp", -150)

        if rsrp >= -80:

            return {

                "excellent": True,

                "good": False,

                "weak": False

            }

        if rsrp >= -100:

            return {

                "excellent": False,

                "good": True,

                "weak": False

            }

        return {

            "excellent": False,

            "good": False,

            "weak": True

        }

    @classmethod
    def getNeighbourCells(cls, top=10):

        return sorted(

            cls._neighbour,

            key=lambda x: x.get("rsrp", -150),

            reverse=True

        )[:top]

    @classmethod
    def toUnwired(cls):

        s = cls._serving

        return {

            "radio": "lte",

            "mcc": s["mcc"],

            "mnc": s["mnc"],

            "cells": [

                {

                    "cid": s["eci"],

                    "lac": s["tac"],

                    "psc": s["pci"],

                    "signal": s["rsrp"]

                }

            ]

        }

    @classmethod
    def toOpenCellID(cls):

        s = cls._serving

        return {

            "radio": "LTE",

            "mcc": s["mcc"],

            "mnc": s["mnc"],

            "lac": s["tac"],

            "cellid": s["eci"]

        }

    @classmethod
    def dump(cls):

        print("=" * 40)

        for k in sorted(cls._serving.keys()):

            print("%-10s : %s" % (

                k,

                cls._serving[k]

            ))

        print("=" * 40)