from fastapi import Query
from typing import Optional, List


def common_params(fields: Optional[List[str]] = Query(None, description='Include only these fields.'), credits: Optional[int] = None):
    return {'fields': fields, 'credits': credits}
