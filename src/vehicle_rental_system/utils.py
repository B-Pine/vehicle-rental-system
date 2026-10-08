def format_currency(
    amount: float,
) -> str:
    """Format money as Rwandan francs."""

    return f"{amount:,.0f} RWF"


def read_non_empty(
    prompt: str,
) -> str:
    """Read non-empty text."""

    while True:
        value = input(prompt).strip()

        if value:
            return value

        print(
            "Input cannot be empty."
        )


def read_positive_float(
    prompt: str,
) -> float:
    """Read a positive decimal number."""

    while True:
        try:
            value = float(
                input(prompt)
            )

            if value > 0:
                return value

            print(
                "Value must be greater than 0."
            )

        except ValueError:
            print(
                "Please enter a valid number."
            )


def read_positive_int(
    prompt: str,
) -> int:
    """Read a positive whole number."""

    while True:
        try:
            value = int(
                input(prompt)
            )

            if value > 0:
                return value

            print(
                "Value must be greater than 0."
            )

        except ValueError:
            print(
                "Please enter a valid whole number."
            )


def print_rental_record(
    record: dict[str, object],
) -> None:
    """Display rental details."""

    print("\n" + "=" * 40)
    print("RENTAL RECEIPT")
    print("=" * 40)

    print(
        f"Vehicle ID   : "
        f"{record['vehicle_id']}"
    )

    print(
        f"Vehicle Type : "
        f"{record['vehicle_type']}"
    )

    print(
        f"Vehicle      : "
        f"{record['brand']} "
        f"{record['model']}"
    )
    print(
    f"Customer     : "
    f"{record['customer_name']}"
    )

    print(
        f"Phone        : "
        f"{record['customer_phone']}"
    )

    print(
        f"Rental Days  : "
        f"{record['days']}"
    )

    print(
        "Total Cost   : "
        f"{format_currency(float(record['total_cost']))}"
    )

    print(
        f"Status       : "
        f"{record['status']}"
    )

    print("=" * 40)


def normalize_phone_number(phone: str) -> str:
    """Validate and normalize a customer phone number."""

    phone = phone.strip()
    normalized = phone.replace(" ", "").replace("-", "")

    if normalized.startswith("+"):
        digits = normalized[1:]
    else:
        digits = normalized

    if not digits.isdigit():
        raise ValueError(
            "Phone number must contain only digits."
        )

    if not 10 <= len(digits) <= 15:
        raise ValueError(
            "Phone number must contain between 10 and 15 digits."
        )

    return normalized


def read_phone(prompt: str) -> str:
    """Read and validate a customer phone number."""

    while True:
        phone = input(prompt)

        try:
            return normalize_phone_number(phone)

        except ValueError as error:
            print(error)
            
              