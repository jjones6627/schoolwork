# music note player

import winsound
import time

def main():
    note_letter = ['A ', 'A#', 'B ', 'C ', 'C#', 'D ', 'D#', 'E ', 'F ', 'F#', 'G ', 'G#']
    note_octave = []
    for octave in range (0,9):
        for n in range (len(note_letter)):
            if note_letter[n] == 'C ':
                octave += 1
            note_octave.append(note_letter[n]+str(octave))

    note_octave_letter_frequency = []
    start_frequency = 55
    note_counter  = 0

    for octave in range (0,9):
        for n in range (len(note_letter)):
            if note_letter[n] == 'C ':
                octave += 1
            note_frequency = (start_frequency*(2**(note_counter/12)))
            note_counter +=1
            note_octave_letter_frequency.append([note_letter[n]+str(octave),\
                                                 note_frequency])

    note_type = ['8TH', 'QTR', 'HALF', 'WHL']
    note_duration = [250, 500, 1000, 2000]

    song = [["D 4", "8TH"], ["D 4", "8TH"], ["E 4", "QTR"], ["D 4", "QTR"],\
            ["G 4", "QTR"], ["F#4", "HALF"], ["D 4", "8TH"], ["D 4", "8TH"],\
            ["E 4", "QTR"], ["D 4", "QTR"], ["A 4", "QTR"], ["G 4", "HALF"],\
            ["D 4", "8TH"], ["D 4", "8TH"],\
            ["D 5", "QTR"], ["B 4", "QTR"], ["G 4", "QTR"], ["F#4", "QTR"],\
            ["E 4", "QTR"], ["C 5", "8TH"], ["C 5", "8TH"], ["B 4", "QTR"],\
            ["G 4", "QTR"], ["A 4", "QTR"], ["G 4", "WHL"]] 

    for note in song:
        note_duration_index = note_type.index((str(note[1:2])[2:-2]))
        note_octave_str = str(note[0:1])[2:-2]
        note_octave_index = \
                note_octave.index(note_octave_str)                
        winsound.Beep(int(note_octave_letter_frequency[note_octave_index][1])\
            , note_duration[note_duration_index])
        time.sleep(note_duration[note_duration_index]/3000)
main()
                
                

      
