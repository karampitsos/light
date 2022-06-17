# phos

Phos is a Python library for dealing with the parsing files from spectrometry
cameras. Currently support only raw8 files.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Phos.

```bash
pip install phos
```

## Basic Usage

```python
from phos import AvantesSpectra


spectra = AvantesSpectra('input.raw8')
print(f'integration time: {spectra.integration_time}')
print(f'integration delay: {spectra.integration_delay}')
plt.plot(spectra.wavelenghts, spectra.counts)
plt.show()
spectra.to_csv('test.csv')
spectra.to_json('test.json')
```
