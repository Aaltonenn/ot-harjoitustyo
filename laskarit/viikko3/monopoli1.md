## Monopoli

```mermaid
 classDiagram
      Pelaaja "1" --> "0" Pelilauta
      Peli "1" --> "2...8" Pelaaja
      Peli "1" --> "1" Pelilauta

      class Pelaaja{
          nappula
      }
      class Pelilauta{
          ruutu
      }
      class Peli{
      }
```
