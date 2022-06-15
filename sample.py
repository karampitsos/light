from light.karaparser import AvantesSpectra
import matplotlib.pyplot as plt

spectra = AvantesSpectra('1904175U1_0001.raw8')
print(f'integration time: {spectra.integration_time}')
print(f'integration delay: {spectra.integration_delay}')
plt.plot(spectra.wavelenghts, spectra.counts)
plt.show()
spectra.to_csv('test.csv')