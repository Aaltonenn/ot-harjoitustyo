## Machine
```mermaid
 sequenceDiagram
     main->>machine: Machine() 
     machine-)tank: FuelTank()
     machine-)tank: self._tank.fill(40)
     machine-)engine: Engine(self._tank)
     machine-)engine: self._engine.start()
     engine-)machine: self._fuel.tank.consume(5)
     machine-)tank: if running
     tank-)machine: true
     engine-)tank use.energy()
     machine-)tank: if running
     tank-)machine: true
     engine-)tank use.energy()
     machine-)tank: if running
     tank-)machine: true
     engine-)tank use.energy()     
     machine-)tank: if running
     tank-)machine: false
```
