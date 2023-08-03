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
import maplotlib.pyplot as plt

#Load dataset
df = dataloader.load_data(...) #or
df = pd.read_csv("hoge.csv")

#Calculate statistics
tau, rho, = stats.calc_bivar_statistics(df)

#Fit MICK/MICS to data
mick = copula.calc_greedy("mick",tau)
mics = copula.calc_greedy("mics",rho)

#Sample from copulas
samples = sampler.sample_from_ccopula(mick,sample_size=1000,save_csv=False)
plt.scatter(samples[:,0],samples[:,1])

#Visualize copula densities
visualize.three_dim_flatten(mick)
```

### Run on App
`streamlit run app.py`


