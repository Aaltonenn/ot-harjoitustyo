sequenceDiagram
    main->>machine: Machine() 
    machine-)tank: FuelTank()
    machine-)tank: self._tank.fill(40)
    machine-)engine: Engine(self._tank)
    machine-)engine: self._engine.start()
     
    
