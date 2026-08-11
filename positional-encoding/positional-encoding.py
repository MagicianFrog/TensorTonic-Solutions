import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    pe = np.zeros((seq_len, d_model), dtype=float)
    positions = np.arange(seq_len)
    
    for col in range(d_model):
        i = col // 2
        divisor = base ** (2 * i / d_model)
        angles = positions / divisor
        
        if col % 2 == 0:
            pe[:, col] = np.sin(angles)
        else:
            pe[:, col] = np.cos(angles)
            
    return pe