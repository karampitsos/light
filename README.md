# phos

Phos is a user-friendly Python library for dealing with the parsing of spectrometry data
and retrieve the spectral data and the metadata. Currently support only raw8 files.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Phos.

```bash
pip install phos
```

## Basic Usage

To parse a raw8 file, initialize a Raw8Spectra instance
passing the file directory. 

```python
from phos import Raw8Spectra

spectra = Raw8Spectra('input.raw8')
```

The Raw8Spectra instance has all the attributes of the raw8 file.

```python
print(f'integration time: {spectra.integration_time}')
print(f'integration delay: {spectra.integration_delay}')
print(f'number of averages: {spectra.number_of_averages}')
print(f'start pixel: {spectra.start_pixel}')
print(f'stop pixel: {spectra.stop_pixel}')
```

You can plot the spectra using the list of wavelenghts and counts.

```python
plt.plot(spectra.wavelenghts, spectra.counts)
plt.show()
```

You can get the spectra scan on a csv file or all the parameters of the experiment
in a json file.

```python
spectra.to_csv('test.csv')
spectra.to_json('test.json')
```