from dataclasses import dataclass


@dataclass(frozen=True)
class Outcome:
    name: str
    odds: int

    def winAmount(self, amount: float) -> float:
        return self.odds * amount
    
    def __str__(self):
        return f'{self.name} {self.odds}:1'
