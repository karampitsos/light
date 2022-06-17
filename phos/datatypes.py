from dataclasses import dataclass
from typing import List

@dataclass
class Identity:
    serial_number: str
    user_friendly_name: str
    status: int


@dataclass
class StrayLightconfig:
    m_SLSSupported: bool
    m_SLSEnabled: bool
    m_SLSMultiFact: float
    m_SLSError: int


@dataclass
class ControlSettings:
    m_StrobeControl: int
    m_LaserDelay: int
    m_LaserWidth: int
    m_LaserWaveLength: float
    m_StoreToRam: int


@dataclass 
class Trigger:
    m_Mode: int
    m_Source: int
    m_SourceType: int


@dataclass
class NonlinConfig:
    m_NonlinSupported: bool
    m_NonlinEnabled: bool
    m_NonlinError: int


@dataclass
class DarkCorrection:
    m_Enable: int
    m_ForgetPercentage: int


@dataclass
class Smoothing:
    m_SmoothPix: int
    m_SmoothModel: int


@dataclass
class Spectra:
    marker: str
    numspectra: int
    length: int
    seqnum: int
    measmode: int
    bitness: int
    SDmarker: int
    Indentity: Identity
    m_StartPixel: int
    m_StopPixel: int
    m_IntegrationTime: float
    m_IntegrationDelay: int
    m_NrAverages: int
    DarkCorrection: DarkCorrection
    Smoothing: Smoothing
    m_SaturationDetection: int
    Trigger: Trigger
    ControlSettings: ControlSettings
    timestamp: str
    SPCfiledate: str 
    detectortemp: float 
    boardtemp: float 
    NTC2volt: float 
    ColorTemp: float 
    CalIntTime: float 
    fitdata: float 
    comment: str 
    xcoord: List[float]
    scope: List[float]
    dark: List[float]
    reference: List[float]
    mergegroup: str
    StrayLightconfig: StrayLightconfig
    NonlinConfig: NonlinConfig
    CustomReflectance: bool
    CustomWhiteRefValue: float
    CustomDarkValue: float