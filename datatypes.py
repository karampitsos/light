from dataclasses import dataclass


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
class TriggerType:
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