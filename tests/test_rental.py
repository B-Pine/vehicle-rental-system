import pytest

from vehicle_rental_system.rental import (
    get_available_vehicles,
    rent_vehicle,
    return_vehicle,
)

from vehicle_rental_system.vehicle import (
    Bike,
    Car,
)


def test_rent_vehicle_changes_availability() -> None:
    car = Car(
        "CAR001",
        "Toyota",
        "Corolla",
        40_000,
        seats=5,
    )

    rent_vehicle(
        car,
        3,
        "Alice",
        "+250788123456",
    )

    assert car.available is False

def test_rental_record_contains_cost() -> None:
    car = Car(
        "CAR001",
        "Toyota",
        "Corolla",
        40_000,
        seats=5,
    )

    record = rent_vehicle(
        car,
        3,
        "Alice",
        "+250788123456",
    )

    assert (
        record["total_cost"]
        == 120_000
    )


def test_cannot_rent_same_vehicle_twice() -> None:
    car = Car(
        "CAR001",
        "Toyota",
        "Corolla",
        40_000,
        seats=5,
    )

    rent_vehicle(
        car,
        2,
        "Alice",
        "+250788123456",
    )

    with pytest.raises(ValueError):
        rent_vehicle(
            car,
            2,
            "Alice",
            "+250788123456",
        )


def test_return_vehicle() -> None:
    car = Car(
        "CAR001",
        "Toyota",
        "Corolla",
        40_000,
        seats=5,
    )

    rent_vehicle(
        car,
        2,
        "Alice",
        "+250788123456",
        
    )

    return_vehicle(car)

    assert car.available is True


def test_cannot_return_available_vehicle() -> None:
    car = Car(
        "CAR001",
        "Toyota",
        "Corolla",
        40_000,
        seats=5,
    )

    with pytest.raises(ValueError):
        return_vehicle(car)


def test_get_available_vehicles() -> None:
    car = Car(
        "CAR001",
        "Toyota",
        "Corolla",
        40_000,
        seats=5,
    )

    bike = Bike(
        "BIK001",
        "Yamaha",
        "FZ",
        20_000,
        engine_cc=150,
    )

    rent_vehicle(
        car,
        2,
        "Alice",
        "+250788123456",

    )

    available = get_available_vehicles(
        [car, bike]
    )

    assert bike in available
    assert car not in available

def test_rental_record_contains_customer() -> None:
    car = Car(
        "CAR001",
        "Toyota",
        "Corolla",
        40_000,
        seats=5,
    )

    record = rent_vehicle(
        car,
        3,
        "Alice",
        "+250788123456",
    )

    assert record["customer_name"] == "Alice"
    assert record["customer_phone"] == "+250788123456"


def test_invalid_customer_phone_is_rejected() -> None:
    car = Car(
        "CAR001",
        "Toyota",
        "Corolla",
        40_000,
        seats=5,
    )

    with pytest.raises(ValueError):
        rent_vehicle(
            car,
            3,
            "Alice",
            "not-a-phone",
        )

