## Monopoli

```mermaid
 classDiagram
      Pelaaja "1" --> "40" Pelilauta
      Peli --> "2...8" Pelaaja
      Peli --> "1" Pelilauta
      Peli --> "2" Noppa
      Pelaaja "1" --> "1" Nappula

      class Pelaaja{
      }
      class Pelilauta{
      }
      class Peli{
      }
      class Nappula{
      }
```
