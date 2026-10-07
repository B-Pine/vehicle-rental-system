import pytest

from vehicle_rental_system.vehicle import (
    Bike,
    Car,
    Truck,
)


def test_car_rental_cost() -> None:
    car = Car(
        "CAR001",
        "Toyota",
        "Corolla",
        40_000,
        seats=5,
    )

    assert (
        car.calculate_rental_cost(3)
        == 120_000
    )


def test_truck_has_surcharge() -> None:
    truck = Truck(
        "TRK001",
        "Isuzu",
        "NPR",
        80_000,
        load_capacity_tons=5,
    )

    assert (
        truck.calculate_rental_cost(2)
        == 192_000
    )


def test_bike_without_discount() -> None:
    bike = Bike(
        "BIK001",
        "Yamaha",
        "FZ",
        20_000,
        engine_cc=150,
    )

    assert (
        bike.calculate_rental_cost(3)
        == 60_000
    )


def test_bike_long_rental_discount() -> None:
    bike = Bike(
        "BIK001",
        "Yamaha",
        "FZ",
        20_000,
        engine_cc=150,
    )

    assert (
        bike.calculate_rental_cost(7)
        == 126_000
    )


def test_price_must_be_positive() -> None:
    with pytest.raises(ValueError):
        Car(
            "CAR001",
            "Toyota",
            "Corolla",
            0,
            seats=5,
        )


def test_car_seats_must_be_positive() -> None:
    with pytest.raises(ValueError):
        Car(
            "CAR001",
            "Toyota",
            "Corolla",
            40_000,
            seats=0,
        )


def test_truck_capacity_must_be_positive() -> None:
    with pytest.raises(ValueError):
        Truck(
            "TRK001",
            "Isuzu",
            "NPR",
            80_000,
            load_capacity_tons=0,
        )


def test_bike_engine_must_be_positive() -> None:
    with pytest.raises(ValueError):
        Bike(
            "BIK001",
            "Yamaha",
            "FZ",
            20_000,
            engine_cc=0,
        )


def test_vehicle_id_is_normalized() -> None:
    car = Car(
        "car001",
        "Toyota",
        "Corolla",
        40_000,
        seats=5,
    )

    assert car.vehicle_id == "CAR001"

