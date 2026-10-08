from .vehicle import Vehicle
from .utils import normalize_phone_number


def rent_vehicle(
    vehicle: Vehicle,
    days: int,
    customer_name: str,
    customer_phone: str,
) -> dict[str, object]:
    """Rent an available vehicle to a customer."""

    if not vehicle.available:
        raise ValueError(
            "Vehicle is already rented."
        )

    if days <= 0:
        raise ValueError(
            "Rental days must be greater than 0."
        )

    customer_name = customer_name.strip()

    if not customer_name:
        raise ValueError(
            "Customer name cannot be empty."
        )

    customer_phone = normalize_phone_number(
        customer_phone
    )

    total_cost = vehicle.calculate_rental_cost(
        days
    )

    vehicle.available = False

    return {
        "vehicle_id": vehicle.vehicle_id,
        "vehicle_type": vehicle.__class__.__name__,
        "brand": vehicle.brand,
        "model": vehicle.model,
        "customer_name": customer_name,
        "customer_phone": customer_phone,
        "days": days,
        "total_cost": total_cost,
        "status": "Rented",
    }

def return_vehicle(
    vehicle: Vehicle,
) -> None:
    """Return a rented vehicle."""

    if vehicle.available:
        raise ValueError(
            "Vehicle is not currently rented."
        )

    vehicle.available = True


def get_available_vehicles(
    vehicles: list[Vehicle],
) -> list[Vehicle]:
    """Return all currently available vehicles."""

    return [
        vehicle
        for vehicle in vehicles
        if vehicle.available
    ]


def find_vehicle(
    vehicles: list[Vehicle],
    vehicle_id: str,
) -> Vehicle | None:
    """Find a vehicle using its ID."""

    vehicle_id = vehicle_id.strip().upper()

    for vehicle in vehicles:
        if vehicle.vehicle_id == vehicle_id:
            return vehicle

    return None
