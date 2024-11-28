from datetime import datetime

import pandas as pd

from hydnam.chart import plot_q
from hydnam.columns_constants import TIMESERIES, TEMPERATURE, PRECIPITATION, EVAPOTRANSPIRATION, DISCHARGE
from hydnam.dataset import Dataset
from hydnam.hydnam import HydNAM
from hydnam.parameters import Parameters

df = pd.read_csv('data.csv')

dataset = Dataset(
    timeseries=df[TIMESERIES].tolist(),
    temperature=df[TEMPERATURE].tolist(),
    precipitation=df[PRECIPITATION].tolist(),
    evapotranspiration=df[EVAPOTRANSPIRATION].tolist(),
    discharge=df[DISCHARGE].tolist(),
)

params = Parameters()
params.from_params(
    [0.97, 721.56, 0.18, 495.91, 25.16, 0.97, 0.11, 0.19, 1121.74, 2.31, 3.51]
)

nam = HydNAM(
    dataset=dataset,
    parameters=params,
    area=58.8,
    interval=24.0,
    start=datetime(2017, 12, 1),
    end=datetime(2017, 12, 30),
    spin_off=0.0,
    ignore_snow=False
)

print(f'Parameters: {nam.parameters}')
print(f'Statistics: {nam.statistics}')

plot_q(nam.simulation_result).show()
