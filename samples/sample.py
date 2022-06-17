from phos import AvantesSpectra
import matplotlib.pyplot as plt


spectra = AvantesSpectra('../input/1904175U1_0001.raw8')
print(f'integration time: {spectra.integration_time}')
print(f'integration delay: {spectra.integration_delay}')
plt.plot(spectra.wavelenghts, spectra.counts)
plt.show()
spectra.to_csv('./output/test.csv')
spectra.to_json('./output/file.json')