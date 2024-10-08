from mido import MidiFile

# Open for writing
mid = MidiFile("invent4.mid", clip=True)


# Save file
mid.save("edited.mid")
