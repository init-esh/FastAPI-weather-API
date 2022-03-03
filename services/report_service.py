import uuid
from typing import Optional,Callable, List, Union, Any
import datetime
from models.location import Location
from models.reports import Report

__reports: List[Report] = []
# fake db


async def get_reports() -> List[Report]:
    return list(__reports)


async def add_report(description: str, location: Location) -> Report:
    now = datetime.datetime.now()
    report = Report(id=str(uuid.uuid4()),
                    location=location,
                    description=description,
                    created_date=now)
    # if using real db use async calls

    __reports.append(report)
    func: Callable[[Report], Optional[Any]]=lambda r: r.created_date
    __reports.sort(key=func, reverse=True)
    return report
