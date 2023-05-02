# Arkkitehtuurikuvaus
 
![kaavio](https://user-images.githubusercontent.com/127753914/235747248-47dabe51-ad5b-4e09-a7b4-9e81343953ee.png)
 
 


```mermaid
 classDiagram
      GUI --> gui_main_menu
      gui_main_menu --> note_giver
      gui_main_menu --> determine_chord
      gui_main_menu --> search_chord
      gui_main_menu --> create_song

      note_giver --> serviceGiveNotes
      determine_chord --> serviceChordDetermination
      
      class serviceChordDetermination{
      chord_determination()
      is_major_chord()
      is_minor_chord()
      }
      class serviceGiveNotes{
      give_notes()
      }
      class note_giver{
      give_note()
      }
      class determine_chord{
      determine_chord()
      }
      class gui_main_menu{
      }
      
      
```
