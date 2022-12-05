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

import numpy as np
import pandas as pd
from typing import Optional
from models.Visit import Visit
from datetime import datetime as dtm
from models.Patient import Patient, PatientValidator

from lib.utils import convert_id


class State:
    def __init__(self) -> None:
        self.patients = []

    def new(self, file: str) -> None:
        df = pd.read_excel(file, sheet_name=0)

        # Identify Patients by unique Subject ID ACA, if we find different DOBs for the same Subject ID ACA
        # we consider the patient to be invalid
        for id in df["Subject ID ACA"].unique():
            pv = PatientValidator(df.loc[df["Subject ID ACA"] == id])
            if not pv.check_unique(var="DOB"):
                print(
                    f"Inconsistency in variable 'DOB' found for patient '{id}', skipping patient"
                )
                continue

            date_str = df.loc[df["Subject ID ACA"] == id]["DOB"].iloc[0]
            date = (
                dtm.strptime(date_str, "%d/%b/%Y") if not pd.isna(date_str) else np.NaN
            )

            attr = {
                "kc_id": convert_id(df.loc[df["Subject ID ACA"] == id]["kc_id"].iloc[0]),
                "aca_id": convert_id(df.loc[df["Subject ID ACA"] == id]["aca_id"].iloc[0]),
                "id": convert_id(id),
                "consent": 0,  # TODO
                "dob": date,
            }
            p = Patient(**attr)
            self.patients.append(p)

        # After patients have been added, each row of the df is added as a visit
        for i in range(len(df)):
            date_str = df.iloc[i]["Medical consultation date"]
            attr = {
                "date": dtm.strptime(date_str, "%d/%b/%Y")
                if not pd.isna(date_str)
                else np.NaN,
            }
            idx = self.get_patient_idx(df.iloc[i]["Subject ID ACA"])
            
            self.patients[idx].add_visit(visit = Visit(**attr))

    def patients_df(self):
        dicts = [p.get_dict() for p in self.patients]
        dicts_combine = {k: [d[k] for d in dicts] for k in dicts[0]}
        return pd.DataFrame(dicts_combine, columns=dicts[0].keys())

    def get_patient_idx(self, id: str) -> int:
        for i, p in enumerate(self.patients):
            if p.id == id:
                return i
        return None
