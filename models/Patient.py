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


class Patient:
    def __init__(self, kc_id: str, aca_id: str, id: str, consent: int) -> None:

        self.kc_id = kc_id
        self.aca_id = aca_id
        self.id = id
        self.consent = consent
