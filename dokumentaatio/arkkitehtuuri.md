## Sointuohjelma

```mermaid
 classDiagram
      UI --> determine_chord (ui)
      UI --> note_giver (ui)
      determine_chord (ui) --> services.service
      note_giver (ui) --> services.service
      services.service --> ChordDetermination
      services.service --> GiveNotes
      
      class note_giver (ui){
      NoteGiver
      }
      class determine_chord (ui){
      }
      class services.service{
      }
      class ChordDetermination{
      }
      class ChordDetermination{
      }
      
```
