from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Base class for all rentable vehicles."""

    def __init__(
        self,
        vehicle_id: str,
        brand: str,
        model: str,
        price_per_day: float,
    ) -> None:
        vehicle_id = vehicle_id.strip().upper()
        brand = brand.strip()
        model = model.strip()

        if not vehicle_id:
            raise ValueError("Vehicle ID cannot be empty.")

        if not brand:
            raise ValueError("Brand cannot be empty.")

        if not model:
            raise ValueError("Model cannot be empty.")

        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model

        self.price_per_day = price_per_day
        self.available = True

    @property
    def price_per_day(self) -> float:
        """Return the vehicle's daily rental price."""
        return self._price_per_day

    @price_per_day.setter
    def price_per_day(self, value: float) -> None:
        """Validate and update daily rental price."""
        if value <= 0:
            raise ValueError(
                "Price per day must be greater than 0."
            )

        self._price_per_day = float(value)

    @property
    def available(self) -> bool:
        """Return whether the vehicle is available."""
        return self._available

    @available.setter
    def available(self, value: bool) -> None:
        """Validate and update availability."""
        if not isinstance(value, bool):
            raise ValueError(
                "Availability must be True or False."
            )

        self._available = value

    @abstractmethod
    def calculate_rental_cost(
        self,
        days: int,
    ) -> float:
        """Calculate rental cost for the vehicle."""
        raise NotImplementedError

    def __str__(self) -> str:
        """Return a user-friendly vehicle description."""

        status = (
            "Available"
            if self.available
            else "Rented"
        )

        return (
            f"{self.vehicle_id} - "
            f"{self.brand} {self.model} "
            f"({self.__class__.__name__}) - "
            f"{status}"
        )

    def __repr__(self) -> str:
        """Return a developer-friendly representation."""

        return (
            f"{self.__class__.__name__}("
            f"vehicle_id={self.vehicle_id!r}, "
            f"brand={self.brand!r}, "
            f"model={self.model!r}, "
            f"price_per_day={self.price_per_day}, "
            f"available={self.available})"
        )


class Car(Vehicle):
    """Standard passenger car."""

    def __init__(
        self,
        vehicle_id: str,
        brand: str,
        model: str,
        price_per_day: float,
        seats: int,
    ) -> None:
        super().__init__(
            vehicle_id,
            brand,
            model,
            price_per_day,
        )

        if seats <= 0:
            raise ValueError(
                "Number of seats must be greater than 0."
            )

        self.seats = seats

    def calculate_rental_cost(
        self,
        days: int,
    ) -> float:
        if days <= 0:
            raise ValueError(
                "Rental days must be greater than 0."
            )

        return self.price_per_day * days


class Truck(Vehicle):
    """Truck with additional heavy-vehicle surcharge."""

    def __init__(
        self,
        vehicle_id: str,
        brand: str,
        model: str,
        price_per_day: float,
        load_capacity_tons: float,
    ) -> None:
        super().__init__(
            vehicle_id,
            brand,
            model,
            price_per_day,
        )

        if load_capacity_tons <= 0:
            raise ValueError(
                "Load capacity must be greater than 0."
            )

        self.load_capacity_tons = float(load_capacity_tons)

    def calculate_rental_cost(
        self,
        days: int,
    ) -> float:
        if days <= 0:
            raise ValueError(
                "Rental days must be greater than 0."
            )

        base_cost = self.price_per_day * days

        surcharge = base_cost * 0.20

        return base_cost + surcharge


class Bike(Vehicle):
    """Bike with long-rental discount."""

    def __init__(
        self,
        vehicle_id: str,
        brand: str,
        model: str,
        price_per_day: float,
        engine_cc: int,
    ) -> None:
        super().__init__(
            vehicle_id,
            brand,
            model,
            price_per_day,
        )

        if engine_cc <= 0:
            raise ValueError(
                "Engine capacity must be greater than 0."
            )

        self.engine_cc = engine_cc

    def calculate_rental_cost(
        self,
        days: int,
    ) -> float:
        if days <= 0:
            raise ValueError(
                "Rental days must be greater than 0."
            )

        cost = self.price_per_day * days

        if days >= 7:
            discount = cost * 0.10
            cost -= discount

        return cost
    