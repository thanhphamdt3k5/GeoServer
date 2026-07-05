"""
Quectel AT Command Parser

Supported

EC200
EC600
EG91
EG95
BG95
BG96
RM500
RM502

AT+QENG="servingcell"
AT+QENG="neighbourcell"
"""

import re

from parser.atparser_v3 import ATParser


class QuectelParser:

    @staticmethod
    def parseServing(line):

        if "+QENG:" not in line:
            return False

        #
        # LTE
        #

        if '"LTE"' not in line:
            return False

        line = line.replace('"', "")

        item = [i.strip() for i in line.split(",")]

        try:

            serving = {

                "rat": item[2],

                "duplex": item[3],

                "mcc": int(item[4]),

                "mnc": int(item[5]),

                "eci": int(item[6], 16),

                "pci": int(item[7]),

                "earfcn": int(item[8]),

                "band": item[9],

                "tac": int(item[10], 16),

                "rsrp": int(item[11]),

                "rsrq": int(item[12]),

            }

            ATParser._serving = serving

            return True

        except Exception:

            return False

    @staticmethod
    def parseNeighbour(line):

        if "+QENG:" not in line:

            return False

        if "neighbourcell" not in line:

            return False

        line = line.replace('"', "")

        item = [i.strip() for i in line.split(",")]

        try:

            cell = {

                "type": item[1],

                "earfcn": int(item[2]),

                "pci": int(item[3]),

                "rsrp": int(item[4]),

                "rsrq": int(item[5])

            }

            ATParser._neighbour.append(cell)

            return True

        except Exception:

            return False

    @staticmethod
    def parse(lines):

        if isinstance(lines, str):

            lines = lines.splitlines()

        ATParser.clear()

        for line in lines:

            QuectelParser.parseServing(line)

            QuectelParser.parseNeighbour(line)

        return True