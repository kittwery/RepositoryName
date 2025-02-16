if __name__ == "__main__":
    class Vehicle:
        def __init__(self, make: str, model: str, year: int) -> None:
            self.make = make
            self.model = model
            self.year = year

        def __str__(self) -> str:
            return f"{self.year} {self.make} {self.model}"

        def __repr__(self) -> str:
            return f"Vehicle(make='{self.make}', model='{self.model}', year={self.year})"


    class Car(Vehicle):
        def __init__(self, make: str, model: str, year: int, num_doors: int) -> None:
            super().__init__(make, model, year)
            self.num_doors = num_doors

        def __str__(self) -> str:
            return f"{super().__str__()} with {self.num_doors} doors"

        def __repr__(self) -> str:
            return f"Car(make='{self.make}', model='{self.model}', year={self.year}, num_doors={self.num_doors})"

        def drive(self) -> str:
            return f"{self.make} {self.model} is driving."


    class Truck(Vehicle):
        def __init__(self, make: str, model: str, year: int, load_capacity: float) -> None:
            super().__init__(make, model, year)
            self._load_capacity = load_capacity

        def __str__(self) -> str:
            return f"{super().__str__()} with a load capacity of {self._load_capacity} tons"

        def __repr__(self) -> str:
            return f"Truck(make='{self.make}', model='{self.model}', year={self.year}, load_capacity={self._load_capacity})"

        def load(self, weight: float) -> str:
            if weight > self._load_capacity:
                raise ValueError(f"Cannot load {weight} tons. Exceeds capacity of {self._load_capacity} tons.")
            return f"Loaded {weight} tons into the truck."


    if __name__ == "__main__":
        car = Car("Toyota", "Corolla", 2020, 4)
        print(car)
        print(car.drive())

        truck = Truck("Volvo", "FH", 2019, 18.0)
        print(truck)
        print(truck.load(15.0))

    pass
