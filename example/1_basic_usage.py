from datetime import datetime

from hydnam.chart import plot_q
from hydnam.dataset import Dataset
from hydnam.hydnam import HydNAM
from hydnam.parameters import Parameters

dataset = Dataset(
    timeseries=[
        datetime(2016, 10, 9),
        datetime(2016, 10, 10),
        datetime(2016, 10, 11),
    ],
    temperature=[15.4, 14.4, 14.9],
    precipitation=[0.0, 0.0, 0.0],
    evapotranspiration=[2.79, 3.46, 3.65],
    discharge=[0.25694, 0.25812, 0.30983]
)

params = Parameters(
    umax=0.01,
    lmax=0.01,
    cqof=0.01,
    ckif=200.0,
    ck12=10.0,
    tof=0.0,
    tif=0.0,
    tg=0.0,
    ckbf=500.0,
    csnow=0.0,
    snowtemp=0.0
)

nam = HydNAM(
    dataset=dataset,
    parameters=params,
    area=58.8,
    interval=24.0,
    start=None,
    end=None,
    spin_off=0.0,
    ignore_snow=False
)

nam.optimize()

print(f'Parameters: {nam.parameters}')
print(f'Statistics: {nam.statistics}')

plot_q(nam.simulation_result, only_obs_and_sim=True).show()