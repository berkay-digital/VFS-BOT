from pydub import AudioSegment
from pydub.playback import play

# Replace "Alarm.mp4" with the path to your file
file_path = "Start.mp4"

# Load the audio file
audio = AudioSegment.from_file(file_path)

# Play the audio file
play(audio)