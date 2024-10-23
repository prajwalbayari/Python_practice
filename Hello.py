import win32com.client
l=['Jack Sparrow','William Butcher','Peter Parker']

speaker1=win32com.client.Dispatch("SAPI.SpVoice")
speaker2=win32com.client.Dispatch("SAPI.SpVoice")
voices=speaker1.GetVoices()

speaker1.Voice=voices[0]
speaker2.Voice=voices[1]

for L in l:
    speaker1.Speak(f"Hello {L}")
    speaker2.Speak(f"Hello {L}")