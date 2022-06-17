# phos

This is a library to read raw8 files


```
from phos import AvantesSpectra


spectra = AvantesSpectra('input.raw8')
print(f'integration time: {spectra.integration_time}')
print(f'integration delay: {spectra.integration_delay}')
plt.plot(spectra.wavelenghts, spectra.counts)
plt.show()
spectra.to_csv('test.csv')
spectra.to_json('test.json')
```