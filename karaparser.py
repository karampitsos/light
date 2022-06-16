from __future__ import annotations
import struct
from typing import List, Tuple, Dict, Optional
import csv
import os
import json
from datatypes import Identity, StrayLightconfig, ControlSettings, \
    DarkCorrection, NonlinConfig, Smoothing, TriggerType

from mapper import bytemapper, Data


class AvantesSpectra:
    def __init__(self, file_dir: str, mapper: Dict[str, Data] = bytemapper):
        
        with open(file_dir, 'rb') as file:
            self.content = file.read()

        self._start_byte_of_dynamic_arrays: int = 328
        self._pixels_of_dynamic_arrays: int = self.stop_pixel - self.start_pixel + 1
        self._offset: int = self._start_byte_of_dynamic_arrays + self._pixels_of_dynamic_arrays*12

    @property    
    def start_pixel(self) -> int:
        return bytemapper['m_StartPixel'].unpack(self.content)

    @property
    def stop_pixel(self) -> int:
        return bytemapper['m_StopPixel'].unpack(self.content)

    @property
    def marker(self) -> str:
        return bytemapper['marker'].unpack(self.content)
        
    @property
    def measmode(self) -> int:
        return bytemapper['measmode'].unpack(self.content)

    @property
    def numspectra(self) -> int:
        return bytemapper['numspectra'].unpack(self.content)

    @property
    def length(self) -> int:
        return bytemapper['length'].unpack(self.content)

    @property
    def seqnum(self) -> int:
        return bytemapper['seqnum'].unpack(self.content)

    @property
    def bitness(self) -> int:
        return bytemapper['bitness'].unpack(self.content)

    @property
    def sdmarker(self) -> int:
        return bytemapper['SDmarker'].unpack(self.content) 

    @property
    def identity(self) -> Identity:

        serial_number = bytemapper['serialNumber'].unpack(self.content)        
        user_friendly_name = bytemapper['UserFriendlyName'].unpack(self.content)
        status = bytemapper['status'].unpack(self.content)
        
        identity = Identity(
            serial_number=serial_number,
            user_friendly_name=user_friendly_name,
            status=status
        )

        return identity

    @property
    def detector_temp(self) -> float:
        return bytemapper['detectortemp'].unpack(self.content)
    
    @property
    def board_temp(self) -> float:
        return bytemapper['boardtemp'].unpack(self.content)
    
    @property
    def fit_data(self) -> List[float]:
        return bytemapper['fitdata'].unpack(self.content)

    @property
    def ntc2volt(self) -> float:
        return bytemapper['NTC2volt'].unpack(self.content)
    
    @property
    def colortemp(self) -> float:
        return bytemapper['ColorTemp'].unpack(self.content) 
    
    @property
    def calinttime(self) -> float:
        return bytemapper['CalIntTime'].unpack(self.content)

    @property
    def integration_time(self) -> float:
        time = bytemapper['m_IntegrationTime'].unpack(self.content)
        return round(time, 2)

    @property
    def integration_delay(self) -> int:
        return bytemapper['m_IntegrationDelay'].unpack(self.content) 

    @property
    def number_of_averages(self):
        return bytemapper['m_NrAverages'].unpack(self.content)
    
    @property
    def dark_correction(self) -> DarkCorrection:
        s = DarkCorrection(
            bytemapper['m_enable'].unpack(self.content),
            bytemapper['m_ForgetPercentage'].unpack(self.content)    
        )
        return s

    @property 
    def smoothing_type(self) -> Smoothing:
        s = Smoothing(
            bytemapper['m_SmoothPix'].unpack(self.content),
            bytemapper['m_SmoothModel'].unpack(self.content),
        )
        return s
    
    @property
    def saturation_detection(self) -> int:
        return bytemapper['m_SaturationDetection'].unpack(self.content)

    @property
    def trigger_type(self) -> TriggerType:
        s = TriggerType(
            bytemapper['m_Mode'].unpack(self.content),
            bytemapper['m_Source'].unpack(self.content),
            bytemapper['m_SourceType'].unpack(self.content)
        )

        return s

    @property
    def control_settings(self) -> ControlSettings:
        s = ControlSettings(
            bytemapper['m_StrobeControl'].unpack(self.content),
            bytemapper['m_LaserDelay'].unpack(self.content),
            bytemapper['m_LaserWidth'].unpack(self.content),
            bytemapper['m_LaserWaveLength'].unpack(self.content),
            bytemapper['m_StoreToRam'].unpack(self.content),
        )

        return s

    @property
    def straylightconfig(self) -> StrayLightconfig:
        
        s = StrayLightconfig(
            bytemapper['m_SLSSupported'].unpack(self.content, offset=self._offset),
            bytemapper['m_SLSEnabled'].unpack(self.content, offset=self._offset),
            bytemapper['m_SLSMultiFact'].unpack(self.content, offset=self._offset),
            bytemapper['m_SLSError'].unpack(self.content, offset=self._offset)
        )

        return s
    
    @property
    def nonlinconfig(self) -> NonlinConfig:

        s = NonlinConfig(
            bytemapper['m_NonlinSupported'].unpack(self.content, offset=self._offset),
            bytemapper['m_NonlinEnabled'].unpack(self.content, offset=self._offset),
            bytemapper['m_NonlinError'].unpack(self.content, offset=self._offset)
        )

        return s

    @property
    def wavelenghts(self) -> List[float]:
        type = 'f'*self._pixels_of_dynamic_arrays
        start = self._start_byte_of_dynamic_arrays
        end = self._pixels_of_dynamic_arrays*4 + self._start_byte_of_dynamic_arrays

        wave =  struct.unpack(type, self.content[start:end])
        return list(wave)
    
    @property
    def counts(self) -> List[float]:
        type = 'f'*self._pixels_of_dynamic_arrays        
        start = self._start_byte_of_dynamic_arrays + self._pixels_of_dynamic_arrays*4
        end = self._start_byte_of_dynamic_arrays + self._pixels_of_dynamic_arrays*8
        
        c = struct.unpack(type, self.content[start:end])
        return list(c)
    
    @property
    def dark(self) -> List[float]:
        type = 'f'*self._pixels_of_dynamic_arrays
        start = self._start_byte_of_dynamic_arrays + self._pixels_of_dynamic_arrays*8
        end = self._start_byte_of_dynamic_arrays + self._pixels_of_dynamic_arrays*12
    
        c = struct.unpack(type, self.content[start:end])
        return list(c)
     
    @property
    def reference(self) -> List[float]:
        type = 'f'*self._pixels_of_dynamic_arrays
        start = self._start_byte_of_dynamic_arrays + self._pixels_of_dynamic_arrays*12
        end = self._start_byte_of_dynamic_arrays + self._pixels_of_dynamic_arrays*16
        c = struct.unpack(type, self.content[start:end])
        return list(c)
    
    @property
    def custom_reflectance(self) -> bool:
        return bytemapper['CustomReflectance'].unpack(self.content, offset=self._offset)
    
    @property
    def custom_white_ref_value(self) -> List[float]:
        return bytemapper['CustomWhiteRefValue'].unpack(self.content, offset=self._offset)
    
    @property
    def custom_dark_ref_value(self) -> List[float]:
        return bytemapper['CustomDarkRefValue'].unpack(self.content, offset=self._offset)

    def to_csv(self, file_dir: str, delimiter: str = ',') -> None:
        with open(file_dir, 'w') as file:
            writer = csv.writer(file, delimiter=delimiter)
            header = ['wavelenght', 'counts']
            writer.writerow(header)
            data = [
                [wavelenght, self.counts[i], self.dark[i], self.reference[i]] 
                for i, wavelenght in enumerate(self.wavelenghts)
                ]
            writer.writerows(data)
    
    def to_json(self, file_dir: str) -> None:
        with open(file_dir, 'w') as file:
            dictionary = self.to_dict()
            file.write(json.dumps(dictionary, indent=2))

    def to_dict(self) -> Dict:
        dictionary = {
            'avs8header': {
                'marker': self.marker,
                'numspectra': self.numspectra,
                },
            'avs8spectrum': {
                'length': self.length,
                'seqnum': self.seqnum,
                'measmode': self.measmode,
                'bitness': self.bitness,
                'SDmarker': self.sdmarker,
                'identity': {
                    'SerialNumber': self.serial_number,
                    'UserFriendlyName': self.user_friendly_name,
                    'Status': self.status
                },
                'measconf': {
                    'm_StartPixel': self.start_pixel,
                    'm_StopPixel': self.stop_pixel,
                    'm_IntegrationTime': self.integration_time,
                    'm_IntegrationDelay': self.integration_delay,
                    'm_NrAverages': self.number_of_averages,
                    'm_CorDynDark': {
                        'm_Enable': '',
                        'm_ForgetPercentage':''
                    },
                    'm_Smoothing': '',
                    'm_SaturationDetection': '',
                    'm_Trigger': '',
                    'm_Control': '' 
                },
                'timestamp': '',
                'SPCfiledate': '',
                'detectortemp': self.detector_temp,
                'boardtemp': self.board_temp,
                'NTC2volt': self.ntc2volt,
                'ColorTemp': self.colortemp,
                'CalIntTime': self.calinttime,
                'fitdata': self.fit_data,
                'comment': '',
                'xcoord': self.wavelenghts,
                'scope': self.counts,
                'dark': self.dark,
                'reference': self.reference,
                'mergegroup': [],
                'straylighconf': {},
                'nonlinconf': {},
                'CustomReflectance': '',
                'CutomWhiteRefValue': {},
                'CustomDarkRefValue': {}
                }
            }
        return dictionary


    @classmethod
    def from_folder(cls, folder_dir: str) -> List[AvantesSpectra]:
        files = os.listdir(folder_dir)
        spectrums: List[AvantesSpectra] = []
        for file_dir in files:
            spectra = cls(file_dir)
            spectrums.append(spectra)
        
        return spectrums