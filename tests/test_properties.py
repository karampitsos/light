import pytest
from phos.parser import Raw8Spectra
from typing import List
import csv


@pytest.fixture
def spectra() -> Raw8Spectra:
    s = Raw8Spectra('input/example.raw8') 
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

def test_start_pixel(spectra: Raw8Spectra):
    assert spectra.start_pixel == 48

def test_stop_pixel(spectra: Raw8Spectra):
    assert spectra.stop_pixel == 2799

def test_marker(spectra: Raw8Spectra):
    assert spectra.marker == 'AVS84'

def test_measmode(spectra: Raw8Spectra):
    assert spectra.measmode == 0

def test_numspectra(spectra: Raw8Spectra):
    assert spectra.numspectra == 1

def test_length(spectra: Raw8Spectra):
    assert spectra.length == 48133

def test_seqnum(spectra: Raw8Spectra):
    assert spectra.seqnum == 0

def test_bitness(spectra: Raw8Spectra):
    assert spectra.bitness == 0

def test_sdmaker(spectra: Raw8Spectra):
    assert spectra.sdmarker == 0

def test_identity(spectra: Raw8Spectra):
    assert spectra.identity.user_friendly_name == ''
    assert spectra.identity.serial_number == ''
    assert spectra.identity.status == ''

def test_detector_temp(spectra: Raw8Spectra):
    assert spectra.detector_temp == 0

def test_board_temp(spectra: Raw8Spectra):
    assert spectra.board_temp == 30.5

def test_fit_data(spectra: Raw8Spectra):
    assert len(spectra.fit_data) == 5

def test_ntc2volt(spectra: Raw8Spectra):
    assert spectra.ntc2volt == 0

def test_colortemp(spectra: Raw8Spectra):
    assert spectra.color_temp == 2850

def test_calinttime(spectra: Raw8Spectra):
    assert spectra.cal_int_time == 0

def test_integration_time(spectra: Raw8Spectra):
    assert spectra.integration_time == 1.05

def test_integration_delay(spectra: Raw8Spectra):
    assert spectra.integration_delay == 1

def test_number_of_averages(spectra: Raw8Spectra):
    assert spectra.number_of_averages == 1

def test_dark_correction(spectra: Raw8Spectra):    
    assert spectra.dark_correction.m_Enable == 1
    assert spectra.dark_correction.m_ForgetPercentage == 100

def test_smoothing(spectra: Raw8Spectra):    
    assert spectra.smoothing.m_SmoothModel == 0
    assert spectra.smoothing.m_SmoothPix == 0

def test_control_settings(spectra: Raw8Spectra):
    assert spectra.control_settings.m_LaserDelay == 0
    assert spectra.control_settings.m_StrobeControl == 0
    assert spectra.control_settings.m_LaserWaveLength == 0
    assert spectra.control_settings.m_StoreToRam == 0
    assert spectra.control_settings.m_LaserWidth == 0

def test_saturation_detection(spectra: Raw8Spectra):
    assert spectra.saturation_detection == 1

def test_trigger(spectra: Raw8Spectra):
    assert spectra.trigger.m_Mode == 0
    assert spectra.trigger.m_Source == 0
    assert spectra.trigger.m_SourceType == 0

def test_stray_light_config(spectra: Raw8Spectra):
    assert spectra.stray_light_config.m_SLSEnabled == True
    assert spectra.stray_light_config.m_SLSError == 133
    assert spectra.stray_light_config.m_SLSMultiFact == 35.19161605834961
    assert spectra.stray_light_config.m_SLSSupported == True

def test_non_lin_config(spectra: Raw8Spectra):
    assert spectra.non_lin_config.m_NonlinSupported == True
    assert spectra.non_lin_config.m_NonlinEnabled == True
    assert spectra.non_lin_config.m_NonlinError == 67

def test_wavelenghts(spectra: Raw8Spectra, wavelengths: List[float]):
    assert spectra.wavelenghts == wavelengths

def test_counts(spectra: Raw8Spectra, counts: List[float]):
    assert spectra.counts == counts

def test_dark(spectra: Raw8Spectra, dark: List[float]):
    assert spectra.dark == dark

def test_reference(spectra: Raw8Spectra, reference: List[float]):
    assert spectra.reference == reference