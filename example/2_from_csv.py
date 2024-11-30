from datetime import datetime

from hydutils.hyd_constants import (
    TIMESERIES,
    TEMPERATURE,
    PRECIPITATION,
    EVAPOTRANSPIRATION,
    DISCHARGE,
)
import pandas as pd

from hydnam.chart import plot_q
from hydnam.dataset import Dataset
from hydnam.hydnam import HydNAM
from hydnam.parameters import Parameters

df = pd.read_csv("example/data.csv")

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
    area=24.56,
    interval=24.0,
    start=datetime(2019, 6, 1),
    end=datetime(2019, 9, 1),
    spin_off=0.0,
)

# nam.optimize()

print(f"Parameters: {nam.parameters}")
print(f"Statistics: {nam.statistics}")

plot_q(nam.simulation_result).show()

nam.simulation_result.to_dataframe().to_csv('result.csv', index=False)
