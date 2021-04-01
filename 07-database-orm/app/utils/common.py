from fastapi import Depends, Query
from typing import Optional, List

from ..database.database import SessionLocal


def common_params(fields: Optional[List[str]] = Query(None, description='Include only these fields.'), credits: Optional[int] = None):
    return {'fields': fields, 'credits': credits}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
