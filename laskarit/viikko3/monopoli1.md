## Monopoli

```mermaid
 classDiagram
      Pelaaja "1" --> "40" Pelilauta
      Peli --> "2...8" Pelaaja
      Peli --> "1" Pelilauta
      Peli --> "2" Noppa
      Pelaaja "1" --> "1" Nappula
      Pelilauta --> "40" Ruutu
      Pelaaja --> "1" Nappula
      Nappula "1" --> "1" Ruutu
      
      class Pelaaja{
      }
      class Pelilauta{
      }
      class Peli{
      }
      class Nappula{
      }
      class Ruutu{
      }
      
```
