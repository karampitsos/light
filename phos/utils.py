from typing import Tuple

def tuple_of_bytes_to_string(data: Tuple[bytes]) -> str:
    s = ''
    for d in data:
        s += d.decode('cp1252')
    
    return s