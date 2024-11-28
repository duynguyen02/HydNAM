from datetime import datetime
from typing import List

import pandas as pd

from hydnam.columns_constants import TIMESERIES, TEMPERATURE, PRECIPITATION, EVAPOTRANSPIRATION, DISCHARGE


class Dataset:
    def __init__(self, time_series: List[datetime], temperatures: List[float],
                 precipitations: List[float], evapotranspirations: List[float],
                 discharges: List[float]):
        self._time_series = time_series
        self._temperatures = temperatures
        self._precipitations = precipitations
        self._evapotranspirations = evapotranspirations
        self._discharges = discharges

    def to_dataframe(self):
        dataset_dict = {
            TIMESERIES: self._time_series,
            TEMPERATURE: self._temperatures,
            PRECIPITATION: self._precipitations,
            EVAPOTRANSPIRATION: self._evapotranspirations,
            DISCHARGE: self._discharges
        }

        df = pd.DataFrame(dataset_dict)
        df[TIMESERIES] = pd.to_datetime(df[TIMESERIES])
        return df
