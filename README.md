# Minimum Information Copula

https://github.com/stardust-coder/minimum-information-copula/assets/61531920/afc16224-a6e3-463c-b05f-a1556587b8be


### Setup

#### GitHub経由
```
pip install git+https://github.com/stardust-coder/minimum-information-copula
```

#### ローカルから
```
git clone https://github.com/stardust-coder/minimum-information-copula
pip install .
```


### Usage
```python
from MIC import *
import pandas as pd
import matplotlib.pyplot as plt

#Load dataset
df = dataloader.load_data_template("trading_jp", start=(2010,1,1),end=(2020,12,31),log_return=True) #currently only support 5 major Japanese trading firms.
df = df.iloc[:,[0,1]] #choose 2 columns.
###or
df = pd.read_csv("hoge.csv") #your own data

#Calculate statistics
tau,rho,_,_,_,_= stats.calc_bivar_stats(df)

#Fit 30x30 MICK/MICS to data. Other gridsizes will be coming soon...
#About 1min.
mick = copula.greedy_MICK(size=30,invariance=copula.plor(tau.statistic)) #need to convert tau into pseudo log odds ratio
mics = copula.greedy_MICS(size=30,invariance=copula.lor(rho.statistic)) #need to convert rho into log odds ratio

#Sample from copulas
samples = sampler.sample_from_ccopula(mick,sample_size=1000,save_csv=False)
plt.figure(figsize=(5,5))
plt.scatter(samples.values[:,0],samples.values[:,1])

#Visualize copula densities
visualize.three_dim_plot_flatten(mics, top=0.01) #top means the upper bound of the density
```

### Run on App
`streamlit run app.py`

### Document

#### Dataloader
Return Pandas DataFrame with 2 columns. `dataloader.load_data_template("trading_jp", start=(2010,1,1),end=(2020,12,31),log_return=True)`


#### Sampler
from Clayton copula `sampler.MOsamples_clayton(alpha=10,size=100)`     
from Gumbel-Hougaard copula `sampler.MOsamples_gh(gamma=5,size=100)`   
from Frank copula `sampler.Invsamples_frank(theta=20,size=100)`    

#### Copula

To be done.

#### Stats

To be done.