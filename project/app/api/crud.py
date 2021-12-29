from typing import Union

from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(url=payload.url, summary="dummy summary")
    await summary.save()
    return summary.id


async def get(_id: int) -> Union[dict, None]:
    summary = await TextSummary.filter(id=_id).first().values()
    if summary:
        return summary
    else:
        return None


async def get_all():
    summaries = await TextSummary.all().values()
    return summaries
