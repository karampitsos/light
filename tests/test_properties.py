import pytest
from light.karaparser import AvantesSpectra
from typing import List, Dict
import csv


@pytest.fixture
def spectra() -> AvantesSpectra:
    s = AvantesSpectra('input/1904175U1_0001.raw8') 
    return s

@pytest.fixture
def wavelengths() -> List[float]:
    with open('output/spectra.csv', 'r') as file:
        reader = csv.reader(file, delimiter=',')
        wave = [float(row[0]) for i, row in enumerate(reader) if i != 0]
    return wave

@pytest.fixture
def counts() -> List[float]:
    with open('output/spectra.csv', 'r') as file:
        reader = csv.reader(file, delimiter=',')
        c = [float(row[1]) for i, row in enumerate(reader) if i != 0]
    return c

def test_start_pixel(spectra: AvantesSpectra):
    assert spectra.start_pixel == 48

def test_stop_pixel(spectra: AvantesSpectra):
    assert spectra.stop_pixel == 2799

def test_marker(spectra: AvantesSpectra):
    assert spectra.marker == 'AVS84'

def test_measmode(spectra: AvantesSpectra):
    assert spectra.measmode == 0

def test_numspectra(spectra: AvantesSpectra):
    assert spectra.numspectra == 1

def test_length(spectra: AvantesSpectra):
    assert spectra.length == 48133

def test_seqnum(spectra: AvantesSpectra):
    assert spectra.seqnum == 0

def test_bitness(spectra: AvantesSpectra):
    assert spectra.bitness == 0

def test_sdmaker(spectra: AvantesSpectra):
    assert spectra.sdmarker == 0

def test_serial_number(spectra: AvantesSpectra):
    assert spectra.serial_number == '1904175U1\x00'

def test_status(spectra: AvantesSpectra):
    assert spectra.status == 2

def test_user_friendly_name(spectra: AvantesSpectra):
    assert spectra.user_friendly_name == ''

def test_detector_temp(spectra: AvantesSpectra):
    assert spectra.detector_temp == 0

def test_board_temp(spectra: AvantesSpectra):
    assert spectra.board_temp == 30.5

def test_fit_data(spectra: AvantesSpectra):
    assert len(spectra.fit_data) == 5

def test_ntc2volt(spectra: AvantesSpectra):
    assert spectra.ntc2volt == 0

def test_colortemp(spectra: AvantesSpectra):
    assert spectra.colortemp == 2850

def test_calinttime(spectra: AvantesSpectra):
    assert spectra.calinttime == 0

def test_integration_time(spectra: AvantesSpectra):
    assert spectra.integration_time == 1.05

def test_integration_delay(spectra: AvantesSpectra):
    assert spectra.integration_delay == 1

def test_number_of_averages(spectra: AvantesSpectra):
    assert spectra.number_of_averages == 1

def test_wavelenghts(spectra: AvantesSpectra, wavelengths: List[float]):
    assert spectra.wavelenghts == wavelengths

def test_counts(spectra: AvantesSpectra, counts: List[float]):
    assert spectra.counts == counts