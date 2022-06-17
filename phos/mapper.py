from dataclasses import dataclass
import struct
from typing import List, Any
from phos.utils import tuple_of_bytes_to_string

@dataclass
class Data:
    start: int
    stop: int
    type: str

    def unpack(self, content: List[bytes], offset: int = 0) -> Any:
        unpacked = struct.unpack(self.type ,content[offset+self.start:offset+self.stop])        
        if len(unpacked) == 1:
            return unpacked[0]
        else:
            if type(unpacked[0]) == bytes:
                return tuple_of_bytes_to_string(unpacked)
            else:
                return list(unpacked)

bytemapper = {
    'marker': Data(0, 5, 'c'*5),
    'numspectra': Data(5, 6, 'B'),
    'length': Data(6, 10, 'I'),
    'seqnum': Data(10, 11, 'B'),
    'measmode': Data(11, 12, 'B'),
    'bitness': Data(12, 13, 'B'),
    'SDmarker': Data(13, 14, 'B'),
    #AvsIdentity
    'serialNumber': Data(14, 24, 'c'*10),
    'UserFriendlyName': Data(24, 88, 'c'*64),
    'status': Data(88, 89, 'B'),
    #MeasConfig
    'm_StartPixel': Data(89, 91, 'H'),
    'm_StopPixel': Data(91, 93, 'H'),
    'm_IntegrationTime': Data(93, 97, 'f'),
    'm_IntegrationDelay': Data(97, 101, 'I'),
    'm_NrAverages': Data(101, 105, 'I'),
        #darkCorrection
    'm_enable': Data(105, 106, 'B'),
    'm_ForgetPercentage': Data(106,107, 'B'),
        #smoothing type
    'm_SmoothPix': Data(107, 109,'H'),
    'm_SmoothModel': Data(109, 110, 'B'),
        #
    'm_SaturationDetection': Data(110, 111, 'B'),
        #trigger type
    'm_Mode': Data(111, 112, 'B'),
    'm_Source': Data(112, 113, 'B'),
    'm_SourceType': Data(113, 114, 'B'),
        #control settings
    'm_StrobeControl': Data(114, 116, 'H'),
    'm_LaserDelay': Data(116, 120, 'I'),
    'm_LaserWidth': Data(120, 124, 'I'),
    'm_LaserWaveLength': Data(124, 128, 'f'),
    'm_StoreToRam': Data(128, 130, 'H'),
        #
    'timestamp': Data(130, 134, 'c'*4),
    'SPCfiledate': Data(134, 138, 'c'*4),
    'detectortemp': Data(138, 142, 'f'),
    'boardtemp': Data(142, 146, 'f'),
    'NTC2volt': Data(146, 150, 'f'),
    'ColorTemp': Data(150, 154, 'f'),
    'CalIntTime': Data(154, 158, 'f'),
    'fitdata': Data(158, 198, 'd'*5),
    'comment': Data(198, 328, 'c'*130),
    #xcoord: array of single;
    #scope: array of single;
    #dark: array of single;
    #reference: array of single;
    'mergegroup': Data(0, 10, 'c'*10),
    #straigth light config
    'm_SLSSupported': Data(10, 11, '?'),
    'm_SLSEnabled': Data(11, 12, '?'),
    'm_SLSMultiFact': Data(12, 16, 'f'),
    'm_SLSError': Data(16, 17, 'B'),
    #Nonlinconfig
    'm_NonlinSupported': Data(17, 18, '?'),
    'm_NonlinEnabled': Data(18, 19, '?'),
    'm_NonlinError': Data(19, 20, 'B'),
    #
    'CustomReflectance': Data(20, 21, '?'),
    'CustomWhiteRefValue': Data(21, 1901, 'f'*470),
    'CustomDarkRefValue': Data(1901, 3781, 'f'*470)
}