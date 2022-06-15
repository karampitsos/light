from __future__ import annotations
import struct
from typing import List, Tuple, Dict
import csv
import os
import json
from utils import tuple_of_bytes_to_string
from datatypes import Identity, StrayLightconfig, ControlSettings, \
    DarkCorrection, NonlinConfig, Smoothing


class AvantesSpectra:
    def __init__(self, file_dir: str):
        
        with open(file_dir, 'rb') as file:
            self.content = file.read()

        self._current: int = 328

    @property    
    def start_pixel(self) -> int:
        pixel = struct.unpack('H', self.content[89:91])
        return pixel[0]

    @property
    def stop_pixel(self) -> int:
        pixel = struct.unpack('H', self.content[91:93])
        return pixel[0]

    @property
    def marker(self) -> str:
        data: Tuple[bytes] = struct.unpack('ccccc', self.content[:5])
        marker = tuple_of_bytes_to_string(data)
        return marker

    @property
    def measmode(self) -> int:
        data = struct.unpack('B', self.content[11:12])
        return data[0]

    @property
    def numspectra(self) -> int:
        numspectra = struct.unpack('B', self.content[5:6])
        return numspectra[0]

    @property
    def length(self) -> int:
        length = struct.unpack('I', self.content[6:10])
        return length[0]

    @property
    def seqnum(self) -> int:
        seqnum = struct.unpack('B', self.content[10:11])
        return seqnum[0]

    @property
    def bitness(self) -> int:
        bitness = struct.unpack('B', self.content[12:13])
        return bitness[0]

    @property
    def sdmarker(self) -> int:
        
        SDmarker = struct.unpack('B', self.content[13:14])
        return SDmarker[0]

    @property
    def identity(self) -> Identity:

        type = 'c'*10
        data: Tuple[bytes] = struct.unpack(type, self.content[14:24])
        
        serial_number = tuple_of_bytes_to_string(data)
        
        type = 'c'*64
        data: Tuple[bytes] = struct.unpack(type, self.content[24:88])
        
        user_friendly_name = tuple_of_bytes_to_string(data)
        
        status = struct.unpack('B', self.content[88:89])
        
        identity = Identity(
            serial_number=serial_number,
            user_friendly_name=user_friendly_name,
            status=status
        )

        return identity

    @property
    def detector_temp(self) -> float:
        temp = struct.unpack('f', self.content[138:142])
        return temp[0]
    
    @property
    def board_temp(self) -> float:
        temp = struct.unpack('f', self.content[142:146])
        return temp[0]
    
    @property
    def fit_data(self) -> List[float]:
        data = struct.unpack('ddddd', self.content[158:198])
        return list(data)

    @property
    def ntc2volt(self) -> float:
        data = struct.unpack('f', self.content[146:150])
        return data[0]
    
    @property
    def colortemp(self) -> float:
        data = struct.unpack('f', self.content[150:154])
        return data[0]
    
    @property
    def calinttime(self) -> float:
        data = struct.unpack('f', self.content[154:158])
        return data[0]

    @property
    def integration_time(self) -> float:
        time = struct.unpack('f', self.content[93:97])
        return round(time[0], 2)

    @property
    def integration_delay(self) -> int:
        delay = struct.unpack('I', self.content[97:101])
        return delay[0]

    @property
    def number_of_averages(self):
        number = struct.unpack('I', self.content[101:105])
        return number[0]

    @property
    def wavelenghts(self) -> List[float]:
        
        pixel_numbers = self.stop_pixel - self.start_pixel + 1
        type = 'f'*pixel_numbers
        number = pixel_numbers*4 + self._current

        wave =  struct.unpack(type, self.content[self._current:number])
        return list(wave)
    
    @property
    def counts(self) -> List[float]:
        pixel_numbers = self.stop_pixel - self.start_pixel + 1
        type = 'f'*pixel_numbers
        start = self._current + pixel_numbers*4
        end = self._current + pixel_numbers*8
        c = struct.unpack(type, self.content[start:end])
        return list(c)
    
    @property
    def dark(self) -> List[float]:
        pixel_numbers = self.stop_pixel - self.start_pixel + 1
        type = 'f'*pixel_numbers
        start = self._current + pixel_numbers*8
        end = self._current + pixel_numbers*12
        c = struct.unpack(type, self.content[start:end])
        return c
     
    @property
    def reference(self) -> List[float]:
        pixel_numbers = self.stop_pixel - self.start_pixel + 1
        type = 'f'*pixel_numbers
        start = self._current + pixel_numbers*12
        end = self._current + pixel_numbers*16
        c = struct.unpack(type, self.content[start:end])
        return c
    
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