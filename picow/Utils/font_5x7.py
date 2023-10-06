# https://www.engineersgarage.com/dot-matrix-display-using-arduino/
font_5x7 = {
    ' ': [0x00,0x00,0x00,0x00,0x00],  
    '!': [0x00,0x00,0x7d,0x00,0x00],  
    '"': [0x00,0x70,0x00,0x70,0x00],  
    '#': [0x14,0x7f,0x14,0x7f,0x14],  
    '$': [0x12,0x2a,0x6b,0x2a,0x24],  
    '%': [0x32,0x34,0x08,0x16,0x26],  
    '&': [0x36,0x49,0x4d,0x52,0x25],  
    "'": [0x00,0x00,0x70,0x00,0x00],  
    '(': [0x00,0x3e,0x41,0x00,0x00],  
    ')': [0x00,0x0,0x41,0x3e,0x00],  
    '*': [0x2a,0x1c,0x08,0x1c,0x2a],  
    '+': [0x08,0x08,0x3e,0x08,0x08],  
    ',': [0x00,0x01,0x06,0x04,0x00],  
    '-': [0x08,0x08,0x08,0x08,0x00],  
    '.': [0x00,0x00,0x03,0x03,0x00],  
    '/': [0x02,0x04,0x08,0x10,0x20],  
    '0': [0x3e,0x41,0x41,0x3e,0x00],  
    '1': [0x11,0x21,0x7f,0x01,0x01],  
    '2': [0x21,0x43,0x45,0x49,0x31],  
    '3': [0x22,0x49,0x49,0x49,0x36],  
    '4': [0x0c,0x14,0x24,0x7f,0x04],  
    '5': [0x72,0x51,0x51,0x51,0x4e],  
    '6': [0x3e,0x49,0x49,0x49,0x26],  
    '7': [0x60,0x40,0x43,0x4c,0x70],  
    '8': [0x36,0x49,0x49,0x49,0x36],  
    '9': [0x32,0x49,0x49,0x49,0x3e],  
    ':': [0x00,0x36,0x36,0x00,0x00],  
    ';': [0x01,0x36,0x34,0x00,0x00],  
    '<': [0x08,0x14,0x22,0x41,0x00],  
    '=': [0x14,0x14,0x14,0x14,0x00],  
    '>': [0x00,0x41,0x22,0x14,0x08],  
    '?': [0x30,0x40,0x45,0x48,0x30],  
    '@': [0x3e,0x41,0x59,0x55,0x3c],  
    'A': [0x3f,0X44,0x44,0x44,0x3f],  
    'B': [0x7f,0x49,0x49,0x49,0x36],  
    'C': [0x3e,0x41,0x41,0x41,0x22],  
    'D': [0x41,0x7f,0x41,0x41,0x3e],  
    'E': [0x7f,0x49,0x49,0x49,0x41],  
    'F': [0x7f,0x48,0x48,0x48,0x40],  
    'G': [0x3e,0x41,0x45,0x45,0x26],  
    'H': [0x7f,0x08,0x08,0x08,0x7f],  
    'I': [0x41,0x41,0x7f,0x41,0x41],  
    'J': [0x42,0x41,0x41,0x7e,0x40],  
    'K': [0x7f,0x08,0x14,0x22,0x41],  
    'L': [0x7f,0x01,0x01,0x01,0x01],  
    'M': [0x7f,0x20,0x18,0x20,0x7f],  
    'N': [0x7f,0x20,0x18,0x06,0x7f],  
    'O': [0x3e,0x41,0x41,0x41,0x3e],  
    'P': [0x7f,0x48,0x48,0x48,0x30],  
    'Q': [0x3c,0x42,0x46,0x42,0x3d],  
    'R': [0x7f,0x48,0x4c,0x4a,0x31],  
    'S': [0x32,0x49,0x49,0x49,0x26],  
    'T': [0x40,0x40,0x7f,0x40,0x40],  
    'U': [0x7e,0x01,0x01,0x01,0x7e],  
    'V': [0x7c,0x02,0x01,0x02,0x7c],  
    'W': [0x7e,0x01,0x06,0x01,0x7e],  
    'X': [0x41,0x22,0x1c,0x22,0x41],  
    'Y': [0x70,0x08,0x0F,0x08,0x70],  
    'Z': [0x43,0x45,0x49,0x51,0x61],  
    '[': [0x00,0x7f,0x41,0x00,0x00],  
    '"': [0x20,0x10,0x08,0x04,0x02],  
    ']': [0x00,0x00,0x41,0x7f,0x00],  
    '^': [0x00,0x20,0x40,0x20,0x00],  
    '_': [0x01,0x01,0x01,0x01,0x01],  
    '`': [0x00,0x40,0x20,0x00,0x00],  
    'a': [0x0c,0x12,0x14,0x0e,0x01],  
    'b': [0x7e,0x11,0x11,0x0e,0x00],  
    'c': [0x0e,0x11,0x11,0x11,0x00],  
    'd': [0x0e,0x11,0x11,0x7e,0x00],  
    'e': [0x0e,0x15,0x15,0x0d,0x00],  
    'f': [0x08,0x3f,0x48,0x20,0x00],  
    'g': [0x12,0x29,0x29,0x1e,0x00],  
    'h': [0x7f,0x08,0x08,0x07,0x00],  
    'i': [0x00,0x11,0x5f,0x01,0x00],  
    'j': [0x00,0x12,0x11,0x5e,0x00],  
    's': [0x7f,0x04,0x0a,0x11,0x00],  
    'l': [0x00,0x41,0x7f,0x01,0x00],  
    'm': [0x3f,0x10,0x0f,0x10,0x0f],  
    'n': [0x20,0x1f,0x10,0x10,0x0f],  
    'o': [0x0e,0x11,0x11,0x0e,0x00],  
    'p': [0x1f,0x14,0x14,0x08,0x00],  
    'q': [0x08,0x14,0x14,0x1f,0x02],  
    'r': [0x1f,0x08,0x10,0x00,0x00],  
    's': [0x09,0x15,0x15,0x12,0x00],  
    't': [0x10,0x7e,0x11,0x02,0x00],  
    'u': [0x1e,0x01,0x01,0x1e,0x01],  
    'v': [0x1e,0x01,0x1e,0x00,0x00],  
    'w': [0x1e,0x01,0x06,0x01,0x1],  
    'x': [0x11,0x0a,0x04,0x0a,0x11],  
    'y': [0x19,0x05,0x06,0x18,0x00],  
    'z': [0x13,0x15,0x19,0x11,0x00],  
    '{': [0x00,0x08,0x36,0x41,0x00],  
    '|': [0x00,0x00,0x7f,0x00,0x00],  
    '}': [0x00,0x41,0x36,0x08,0x00],  
    '~': [0x08,0x10,0x08,0x10,0x00],  
}

morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.'
}

font_3x5 = {
    
    '0': [0x1F, 0x11, 0x1F],
    '1': [0x09, 0x3F, 0x01],
    '2': [0x13, 0x15, 0x19],
    '3': [0x11, 0x15, 0x1F],
    '4': [0x1C, 0x04, 0x1F],
    '5': [0x1D, 0x15, 0x17],
    '6': [0x1F, 0x15, 0x17],
    '7': [0x10, 0x17, 0x18],
    '8': [0x1F, 0x15, 0x1F],
    '9': [0x1D, 0x15, 0x1F],
    'A': [0x1F, 0x24, 0x1F],
    'B': [0x1F, 0x15, 0x0A],
    'C': [0x0E, 0x11, 0x11],
    'D': [0x1F, 0x11, 0x0E],
    'E': [0x1F, 0x15, 0x11],
    'F': [0x1F, 0x14, 0x10],
    'G': [0x1F, 0x11, 0x17],
    'H': [0x0F, 0x04, 0x1F],
    'I': [0x11, 0x1F, 0x11],
    'J': [0x03, 0x01, 0x1F],
    'K': [0x1F, 0x04, 0x1B],
    'L': [0x1F, 0x01, 0x01],
    'M': [0x1F, 0x08, 0x1F],
    'N': [0x1F, 0x02, 0x1E],
    'O': [0x1F, 0x11, 0x1F],
    'P': [0x1F, 0x14, 0x1C],
    'Q': [0x1E, 0x12, 0x1F],
    'R': [0x1F, 0x14, 0x0B],
    'S': [0x1D, 0x15, 0x17],
    'T': [0x10, 0x1F, 0x10],
    'U': [0x1F, 0x01, 0x1F],
    'V': [0x1E, 0x01, 0x1E],
    'W': [0x1F, 0x02, 0x1F],
    'X': [0x1B, 0x04, 0x1B],
    'Y': [0x18, 0x07, 0x18],
    'Z': [0x13, 0x15, 0x19],
    # 'a': [0x1C, 0x14, 0x1E],
    # 'b': [0x1F, 0x14, 0x08],
    # 'c': [0x0C, 0x12, 0x12],
    # 'd': [0x08, 0x14, 0x1F],
    # 'e': [0x1C, 0x16, 0x16],
    # 'f': [0x08, 0x3E, 0x09],
    # 'g': [0x19, 0x25, 0x1E],
    # 'h': [0x1F, 0x04, 0x1C],
    # 'i': [0x00, 0x1D, 0x00],
    # 'j': [0x02, 0x01, 0x1E],
    # 'k': [0x1F, 0x04, 0x1A],
    # 'l': [0x00, 0x1F, 0x00],
    # 'm': [0x1E, 0x0C, 0x1E],
    # 'n': [0x1E, 0x04, 0x1C],
    # 'o': [0x0C, 0x12, 0x0C],
    # 'p': [0x3F, 0x12, 0x0C],
    # 'q': [0x0C, 0x12, 0x3F],
    # 'r': [0x1E, 0x04, 0x02],
    # 's': [0x14, 0x16, 0x0A],
    # 't': [0x02, 0x1F, 0x12],
    # 'u': [0x1E, 0x10, 0x1E],
    # 'v': [0x1C, 0x10, 0x1C],
    # 'w': [0x1E, 0x18, 0x1E],
    # 'x': [0x1A, 0x04, 0x1A],
    # 'y': [0x39, 0x05, 0x03],
    # 'z': [0x12, 0x16, 0x1A],
    chr(31): [0x00],
    ' ': [0x00, 0x00, 0x00],
    '.': [0x01],
    ',': [0x01, 0x03, 0x00],
    ':': [0x0A],
    ';': [0x01, 0x0B, 0x00],
    '!': [0x00, 0x1D, 0x00],
    '?': [0x10, 0x15, 0x0C],
    '-': [0x04, 0x04, 0x04],
    '_': [0x01, 0x01, 0x01],
    '/': [0x18, 0x04, 0x03],
    '\\': [0x03, 0x04, 0x18],
    '@': [0x1E, 0x15, 0x1D],
    # '#': [0x0A, 0x1F, 0x0A],
    # '$': [0x12, 0x1F, 0x09],
    '%': [0x13, 0x04, 0x19],
    '^': [0x08, 0x10, 0x08],
    # '&': [0x0A, 0x15, 0x1A],
    '*': [0x0A, 0x04, 0x0A],
    '(': [0x0E, 0x11, 0x00],
    ')': [0x00, 0x11, 0x0E],
    '[': [0x1F, 0x11, 0x00],
    ']': [0x00, 0x11, 0x1F],
    '{': [0x04, 0x1F, 0x11],
    '}': [0x11, 0x1F, 0x04],
    '<': [0x04, 0x0A, 0x11],
    '>': [0x11, 0x0A, 0x04],
    '=': [0x0A, 0x0A, 0x0A],
    '+': [0x04, 0x0E, 0x04],
    '|': [0x00, 0x1F, 0x00],
    '"': [0x10, 0x00, 0x10],
    "'": [0x00, 0x10, 0x00],
    '`': [0x10, 0x00, 0x00],
    # '~': [0x04, 0x0A, 0x04],
}