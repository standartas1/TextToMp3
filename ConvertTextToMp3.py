import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties for slower speech rate and default volume
engine.setProperty('rate', 125)   # Lower value makes speech slower (default is around 200)
engine.setProperty('volume', 1)   # Volume level (0.0 to 1.0)

# List all available voices
voices = engine.getProperty('voices')

# Find and set Microsoft David (US Male Voice)
for voice in voices:
  if "David" in voice.name:
    engine.setProperty('voice', voice.id)
    break

# Read the text from a file
input_file = r"C:\Python apps\Convert Text to Mp3\text.txt"
with open(input_file, 'r', encoding='utf-8') as file:
    text = file.read()  

# Save the speech to a file
output_file = r"C:\Python apps\Convert Text to Mp3\PragmaticProgrammerSummary.mp3"
engine.save_to_file(text, output_file)

# Stop the engine
engine.runAndWait()

# Provide the file path for download
output_file