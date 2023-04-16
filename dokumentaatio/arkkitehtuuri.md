## Sointuohjelma

```mermaid
 classDiagram
      UI --> note_giver
      UI --> determine_chord
      note_giver --> service
      determine_chord --> service
      service --> ChordDetermination
      service --> GiveNotes
      
      class ChordDetermination{
      chord_determination()
      is_major_chord()
      is_minor_chord()
      }
      class GiveNotes{
      give_notes()
      }
      class note_giver{
      give_note()
      }
      class determine_chord{
      determine_chord()
      }
      
```
