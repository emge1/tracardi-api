from typing import Optional

from fastapi import APIRouter
from fastapi import HTTPException, Depends
from tracardi.service.storage.factory import storage_manager

from .auth.authentication import get_current_user
from tracardi.domain.enum.indexes_histogram import IndexesHistogram
from tracardi.domain.enum.indexes_search import IndexesSearch
from tracardi.service.storage.helpers.index import Index
from tracardi.domain.sql_query import SqlQuery
from tracardi.domain.time_range_query import DatetimeRangePayload

router = APIRouter(
    dependencies=[Depends(get_current_user)]
)


@router.post("/{index}/select", tags=["generic", "event", "profile", "resource", "rule", "session", "flow", "segment"])
async def select_by_sql(index: IndexesSearch, query: Optional[SqlQuery] = None):
    try:
        elastic_index = Index(storage_manager(index.value))
        if query is None:
            query = SqlQuery()
        return await elastic_index.search(query.where, query.limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/{index}/select/range/page/{page}",
             tags=["generic", "event", "profile", "resource", "rule", "session", "flow", "segment"])
@router.post("/{index}/select/range",
             tags=["generic", "event", "profile", "resource", "rule", "session", "flow", "segment"])
async def time_range_with_sql(index: IndexesHistogram, query: DatetimeRangePayload, page: Optional[int] = None):
    try:
        if page is not None:
            page_size = 25
            query.start = page_size * page
            query.limit = page
        elastic_index = Index(storage_manager(index.value))
        return await elastic_index.time_range(query)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/{index}/select/histogram",
             tags=["generic", "event", "profile", "resource", "rule", "session", "flow", "segment"])
async def histogram_with_sql(index: IndexesHistogram, query: DatetimeRangePayload):
    try:
        elastic_index = Index(storage_manager(index.value))
        return await elastic_index.histogram(query)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
