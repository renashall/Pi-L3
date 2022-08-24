import pyaudio, wave

chunk = 2**12

def playSong(file_name):
    audio_file = wave.open(file_name, 'rb')
    audio = pyaudio.PyAudio()

    
    print("Now playing", file_name)


    stream.stop_stream()
    stream.close()
    audio.terminate()
    audio_file.close()

    print(file_name, "has been closed")

if __name__ == '__main__':
    song = input("What file do you want to play? ") + ".wav"
    playSong(song)
