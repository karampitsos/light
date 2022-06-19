# phos

Phos is a user-friendly Python library for dealing with the parsing of spectrometry data from spectrometry devices.
Currently support only raw8 files.
In order to analyze source data from a spectrometry device
utilizing powerful python libraries such as pandas, numpy, scipy, scikit-learn
you have to export the data in a csv format and afterwords analyze it with this format.
This library offers the ability to use the source files directly
and save a great amount of time and resources
especially if there is a big number of spectras waiting for analysis.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Phos.

```bash
pip install phos
```

## Basic Usage

In order to parse a raw8 file, you have to initialize a Raw8Spectra instance
passing the file directory.

```python
from phos import Raw8Spectra

spectra = Raw8Spectra('input.raw8')
```

The attributes of a raw8 files is accessed by properties of the instance of`Raw8spectra` class.

```python
integration_time = spectra.integration_time
integration_delay = spectra.integration_delay
number_of_averages = spectra.number_of_averages
start_pixel = spectra.start_pixel
stop_pixel = spectra.stop_pixel

print(f'integration time: {integration_time}')
print(f'integration delay: {integration_delay}')
print(f'number of averages: {number_of_averages}')
print(f'start pixel: {start_pixel}')
print(f'stop pixel: {stop_pixel}')
```

The spectra can be plotted using the lists of wavelenghts and counts.

```python
plt.plot(spectra.wavelenghts, spectra.counts)
plt.show()
```

The spectra scan can be exported as a csv file or as json file which contains all the corresponding metadata.

```python
spectra.to_csv('test.csv')
spectra.to_json('test.json')
```

## Advanced Usage
### Manage multiple files

In order to parse multiple files you can use the from_folder function.

```python
from phos import Raw8Spectra

spectras: List[Raw8Spectra] = Raw8Spectra.from_folder(folder_dir)
```

In order to export the data to csv or json format files you can use.

```python

spectras.many_to_csv()

spectras.many_to_json()

```

### Dark and reference

In order to access the dark and reference of a measurement.

```python
dark = spectra.dark
reference = spectra.reference

```

Export csv with dark and reference

```python
spectra.to_csv(file.csv, details=True)
```
