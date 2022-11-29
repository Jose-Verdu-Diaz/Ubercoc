"""
Copyright (C) 2022 José Verdú-Díaz

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see https://www.gnu.org/licenses/
"""

from datetime import date
from typing import Tuple, Optional


class Treatment:
    def __init__(
        self,
        name: str,
        date_first: Optional[date] = None,
        date_last: Optional[date] = None,
        date_stop: Optional[date] = None,
        ongoing: Optional[bool] = None,
        stop_reason: Optional[str] = None,
        used_before: Optional[bool] = None,
        stop_before_reason: str = None,
        adverse: Optional[bool] = None,
        adverse_which: list = [],
        reported_change: Optional[str] = None,
    ) -> None:

        self.name = name
        self.date_first = date_first
        self.date_last = date_last
        self.date_stop = date_stop
        self.ongoing = ongoing
        self.stop_reason = stop_reason
        self.used_before = used_before
        self.stop_before_reason = stop_before_reason
        self.adverse = adverse
        self.adverse_which = adverse_which
        self.reported_change = reported_change

    def validate(self) -> Tuple[dict, str]:
        unconsistent = {
            "name": False,
            "date_first": False,
            "date_last": False,
            "date_stop": False,
            "ongoing": False,
            "stop_reason": False,
            "used_before": False,
            "stop_before_reason": False,
            "adverse": False,
            "adverse_which": False,
            "reported_change": False,
        }

        # Dates
        if self.date_last < self.date_first:
            unconsistent["date_last"] = True
            unconsistent["date_first"] = True
            return (
                unconsistent,
                "Date of last treatment must be higher or equal than date of first treatment",
            )

        if self.date_stop < self.date_first:
            unconsistent["date_stop"] = True
            unconsistent["date_first"] = True
            return (
                unconsistent,
                "Date of stop treatment must be higher or equal than date of first treatment",
            )

        if self.date_stop < self.date_last:
            unconsistent["date_stop"] = True
            unconsistent["date_last"] = True
            return (
                unconsistent,
                "Date of stop treatment must be higher or equal than date of last treatment",
            )

        # Ongoing
        if self.ongoing and (
            not self.stop_reason == None or not self.date_stop == None
        ):
            unconsistent["ongoing"] = True
            unconsistent["stop_reason"] = True
            unconsistent["date_stop"] = True
            return (
                unconsistent,
                "If treatment is ongoing, there must be no stop date and stop reason",
            )
