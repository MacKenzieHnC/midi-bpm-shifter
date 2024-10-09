from mido import MidiFile

# Open for writing
mid = MidiFile("invent4.mid", clip=True)

ratio = 8
for i in range(0, len(mid.tracks)):
    for j in range(0, len(mid.tracks[i])):
        if not mid.tracks[i][j].is_meta:
            mid.tracks[i][j].time = round(mid.tracks[i][j].time * ratio)
        elif mid.tracks[i][j].type == "set_tempo":
            mid.tracks[i][j].tempo = round(mid.tracks[i][j].tempo / ratio)
            mid.tracks[i][j].time = round(mid.tracks[i][j].time * ratio)

# Save file
mid.save("edited.mid")
