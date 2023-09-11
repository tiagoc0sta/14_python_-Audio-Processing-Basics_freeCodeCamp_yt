import wave

obj = wave.open("tiago.wav", "rb")

print("Number of channels", obj.getnchannels())
print("Sample width", obj.getsampwidth())
print("Frame rate.", obj.getframerate())
print("Number of frames", obj.getnframes())
print("parameters:", obj.getparams())
frames = obj.readframes(obj.getnframes())

print(len(frames) / obj.getsampwidth(), frames[0], type(frames[0]))
obj.close()

# write wave file
sample_rate = 16000.0 # hertz
obj = wave.open("tiago.wav",'wb')

obj.setnchannels(1) # mono
obj.setsampwidth(2)
obj.setframerate(sample_rate)

obj.writeframes(frames)

obj.close()