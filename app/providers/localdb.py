"""
Local Database Provider
"""

from database import SessionLocal
from models import Cell


class LocalDBProvider:

    def __init__(self):

        self.db = SessionLocal()

    def close(self):

        self.db.close()

    def locate(self, mcc, mnc, lac, cid):

        cell = (
            self.db.query(Cell)
            .filter(Cell.mcc == mcc)
            .filter(Cell.mnc == mnc)
            .filter(Cell.lac == lac)
            .filter(Cell.cid == cid)
            .first()
        )

        if not cell:

            return None

        return {

            "provider": "LocalDB",

            "lat": cell.lat,

            "lon": cell.lon,

            "accuracy": cell.accuracy

        }

    def insert(self, data):

        cell = Cell(**data)

        self.db.add(cell)

        self.db.commit()

        self.db.refresh(cell)

        return cell

    def update(self, cell, **kwargs):

        for k, v in kwargs.items():

            setattr(cell, k, v)

        self.db.commit()

        return cell