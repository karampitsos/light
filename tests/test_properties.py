import pytest
from karaparser import AvantesSpectra
from typing import List
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

@pytest.fixture
def dark() -> List[float]:
    with open('output/test.csv', 'r') as file:
        reader = csv.reader(file, delimiter=',')
        c = [float(row[2]) for i, row in enumerate(reader) if i != 0]
    return c

@pytest.fixture
def reference() -> List[float]:
    with open('output/test.csv', 'r') as file:
        reader = csv.reader(file, delimiter=',')
        c = [float(row[3]) for i, row in enumerate(reader) if i != 0]
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

def test_identity(spectra: AvantesSpectra):
    assert spectra.identity.user_friendly_name == ''
    assert spectra.identity.serial_number == ''
    assert spectra.identity.status == ''

def test_detector_temp(spectra: AvantesSpectra):
    assert spectra.detector_temp == 0

def test_board_temp(spectra: AvantesSpectra):
    assert spectra.board_temp == 30.5

def test_fit_data(spectra: AvantesSpectra):
    assert len(spectra.fit_data) == 5

def test_ntc2volt(spectra: AvantesSpectra):
    assert spectra.ntc2volt == 0

def test_colortemp(spectra: AvantesSpectra):
    assert spectra.color_temp == 2850

def test_calinttime(spectra: AvantesSpectra):
    assert spectra.cal_int_time == 0

def test_integration_time(spectra: AvantesSpectra):
    assert spectra.integration_time == 1.05

def test_integration_delay(spectra: AvantesSpectra):
    assert spectra.integration_delay == 1

def test_number_of_averages(spectra: AvantesSpectra):
    assert spectra.number_of_averages == 1

def test_dark_correction(spectra: AvantesSpectra):    
    assert spectra.dark_correction.m_Enable == 1
    assert spectra.dark_correction.m_ForgetPercentage == 100

def test_smoothing(spectra: AvantesSpectra):    
    assert spectra.smoothing.m_SmoothModel == 0
    assert spectra.smoothing.m_SmoothPix == 0

def test_control_settings(spectra: AvantesSpectra):
    assert spectra.control_settings.m_LaserDelay == 0
    assert spectra.control_settings.m_StrobeControl == 0
    assert spectra.control_settings.m_LaserWaveLength == 0
    assert spectra.control_settings.m_StoreToRam == 0
    assert spectra.control_settings.m_LaserWidth == 0

def test_saturation_detection(spectra: AvantesSpectra):
    assert spectra.saturation_detection == 1

def test_trigger(spectra: AvantesSpectra):
    assert spectra.trigger.m_Mode == 0
    assert spectra.trigger.m_Source == 0
    assert spectra.trigger.m_SourceType == 0

def test_stray_light_config(spectra: AvantesSpectra):
    assert spectra.stray_light_config.m_SLSEnabled == True
    assert spectra.stray_light_config.m_SLSError == 133
    assert spectra.stray_light_config.m_SLSMultiFact == 35.19161605834961
    assert spectra.stray_light_config.m_SLSSupported == True

def test_non_lin_config(spectra: AvantesSpectra):
    assert spectra.non_lin_config.m_NonlinSupported == True
    assert spectra.non_lin_config.m_NonlinEnabled == True
    assert spectra.non_lin_config.m_NonlinError == 67

def test_wavelenghts(spectra: AvantesSpectra, wavelengths: List[float]):
    assert spectra.wavelenghts == wavelengths

def test_counts(spectra: AvantesSpectra, counts: List[float]):
    assert spectra.counts == counts

def test_dark(spectra: AvantesSpectra, dark: List[float]):
    assert spectra.dark == dark

def test_reference(spectra: AvantesSpectra, reference: List[float]):
    assert spectra.reference == reference