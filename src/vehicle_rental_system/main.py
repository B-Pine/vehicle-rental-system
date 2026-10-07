from .rental import (
    find_vehicle,
    get_available_vehicles,
    rent_vehicle,
    return_vehicle,
)

from .utils import (
    format_currency,
    print_rental_record,
    read_non_empty,
    read_positive_int,
)

from .vehicle import (
    Bike,
    Car,
    Truck,
    Vehicle,
)


def create_sample_vehicles() -> list[Vehicle]:
    """Create sample vehicle inventory."""

    return [
        Car(
            "CAR001",
            "Toyota",
            "Corolla",
            40_000,
            seats=5,
        ),
        Car(
            "CAR002",
            "Hyundai",
            "Elantra",
            45_000,
            seats=5,
        ),
        Truck(
            "TRK001",
            "Isuzu",
            "NPR",
            80_000,
            load_capacity_tons=5,
        ),
        Bike(
            "BIK001",
            "Yamaha",
            "FZ",
            20_000,
            engine_cc=150,
        ),
        Bike(
            "BIK002",
            "Honda",
            "CBR",
            25_000,
            engine_cc=250,
        ),
    ]


def display_vehicles(
    vehicles: list[Vehicle],
) -> None:
    """Display all vehicles."""

    if not vehicles:
        print(
            "\nNo vehicles found."
        )
        return

    print("\nVEHICLE INVENTORY")
    print("-" * 80)

    print(
        f"{'ID':<10}"
        f"{'Type':<12}"
        f"{'Vehicle':<25}"
        f"{'Price/Day':>15}"
        f"{'Status':>15}"
    )

    print("-" * 80)

    for vehicle in vehicles:
        status = (
            "Available"
            if vehicle.available
            else "Rented"
        )

        vehicle_name = (
            f"{vehicle.brand} "
            f"{vehicle.model}"
        )

        print(
            f"{vehicle.vehicle_id:<10}"
            f"{vehicle.__class__.__name__:<12}"
            f"{vehicle_name:<25}"
            f"{format_currency(vehicle.price_per_day):>15}"
            f"{status:>15}"
        )


def display_available(
    vehicles: list[Vehicle],
) -> None:
    """Display only available vehicles."""

    available = get_available_vehicles(
        vehicles
    )

    if not available:
        print(
            "\nNo vehicles are currently available."
        )
        return

    display_vehicles(available)


def handle_rental(
    vehicles: list[Vehicle],
    rental_records: dict[
        str,
        dict[str, object],
    ],
) -> None:
    """Rent a vehicle."""

    display_available(vehicles)

    vehicle_id = read_non_empty(
        "\nEnter vehicle ID to rent: "
    )

    vehicle = find_vehicle(
        vehicles,
        vehicle_id,
    )

    if vehicle is None:
        print(
            "Vehicle not found."
        )
        return

    if not vehicle.available:
        print(
            "Vehicle is already rented."
        )
        return

    days = read_positive_int(
        "Number of rental days: "
    )

    try:
        record = rent_vehicle(
            vehicle,
            days,
        )

        rental_records[
            vehicle.vehicle_id
        ] = record

        print_rental_record(record)

    except ValueError as error:
        print(
            f"Rental failed: {error}"
        )


def handle_return(
    vehicles: list[Vehicle],
    rental_records: dict[
        str,
        dict[str, object],
    ],
) -> None:
    """Return a rented vehicle."""

    vehicle_id = read_non_empty(
        "Enter vehicle ID to return: "
    )

    vehicle = find_vehicle(
        vehicles,
        vehicle_id,
    )

    if vehicle is None:
        print(
            "Vehicle not found."
        )
        return

    try:
        return_vehicle(vehicle)

        if vehicle.vehicle_id in rental_records:
            rental_records[
                vehicle.vehicle_id
            ]["status"] = "Returned"

        print(
            f"{vehicle.brand} "
            f"{vehicle.model} "
            f"returned successfully."
        )

    except ValueError as error:
        print(
            f"Return failed: {error}"
        )


def display_rental_records(
    rental_records: dict[
        str,
        dict[str, object],
    ],
) -> None:
    """Display rental records."""

    if not rental_records:
        print(
            "\nNo rental records available."
        )
        return

    print("\nRENTAL RECORDS")
    print("-" * 90)

    print(
        f"{'ID':<10}"
        f"{'Type':<12}"
        f"{'Vehicle':<25}"
        f"{'Days':>8}"
        f"{'Cost':>18}"
        f"{'Status':>15}"
    )

    print("-" * 90)

    for record in rental_records.values():
        vehicle_name = (
            f"{record['brand']} "
            f"{record['model']}"
        )

        print(
            f"{str(record['vehicle_id']):<10}"
            f"{str(record['vehicle_type']):<12}"
            f"{vehicle_name:<25}"
            f"{str(record['days']):>8}"
            f"{format_currency(float(record['total_cost'])):>18}"
            f"{str(record['status']):>15}"
        )


def print_menu() -> None:
    """Display main application menu."""

    print("\n" + "=" * 45)
    print("VEHICLE RENTAL SYSTEM")
    print("=" * 45)

    print("1. View all vehicles")
    print("2. View available vehicles")
    print("3. Rent vehicle")
    print("4. Return vehicle")
    print("5. View rental records")
    print("6. Exit")


def main() -> None:
    """Run the Vehicle Rental System."""

    vehicles = create_sample_vehicles()

    rental_records: dict[
        str,
        dict[str, object],
    ] = {}

    while True:
        print_menu()

        choice = input(
            "Choose an option: "
        ).strip()

        if choice == "1":
            display_vehicles(
                vehicles
            )

        elif choice == "2":
            display_available(
                vehicles
            )

        elif choice == "3":
            handle_rental(
                vehicles,
                rental_records,
            )

        elif choice == "4":
            handle_return(
                vehicles,
                rental_records,
            )

        elif choice == "5":
            display_rental_records(
                rental_records
            )

        elif choice == "6":
            print(
                "Thank you for using "
                "Vehicle Rental System."
            )
            break

        else:
            print(
                "Invalid option. "
                "Choose between 1 and 6."
            )


if __name__ == "__main__":
    main()
    