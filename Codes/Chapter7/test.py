from scipy import signal
original = [0, 1, 0, 0, 1, 1, 0, 0]
impulse_response = [0,0,1,2,2,1,0,0]
recorded = signal.convolve(impulse_response, original)

print(recorded)

# recovered, remainder = signal.deconvolve(recorded, impulse_response)
# print(original, recovered)

print( 12 // 3)