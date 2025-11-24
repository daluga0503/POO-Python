from typing import Protocol
class Prestable(Protocol):
    def presta(self) -> None:
        ...
        
    def devuelve(self) -> None:
        ...

    def estaPrestado(self) -> bool:
        ...
