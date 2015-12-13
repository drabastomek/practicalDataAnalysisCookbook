from scipy import signal
original = [0, 1, 0, 0, 1, 1, 0, 0]
impulse_response = [0,0,1,2,2,1,0,0]
recorded = signal.convolve(impulse_response, original)

print(recorded)

# recovered, remainder = signal.deconvolve(recorded, impulse_response)
# print(original, recovered)

print( 12 // 3)

import numpy as np
freq = 12
filt = np.array([.5] + [1] * (freq - 1) + [.5]) / freq

print(filt)

d = [1,2,3,4,5,6,7,8,9,10] 
print(d[1::2])