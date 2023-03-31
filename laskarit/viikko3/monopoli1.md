## Monopoli

```mermaid
 classDiagram
      Pelaaja "1" --> "40" Pelilauta
      Peli "1" --> "2...8" Pelaaja
      Peli "1" --> "1" Pelilauta
      Peli "1" --> "2" Noppa

      class Pelaaja{
      }
      class Pelilauta{
      }
      class Peli{
      }
```
