from phos import Raw8Spectra
import matplotlib.pyplot as plt


spectra = Raw8Spectra('../input/example.raw8')
print(f'integration time: {spectra.integration_time}')
print(f'integration delay: {spectra.integration_delay}')
plt.plot(spectra.wavelenghts, spectra.counts)
plt.show()
spectra.to_csv('file.csv')
spectra.to_json('file.json')