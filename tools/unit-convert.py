#!/usr/bin/env python3
"""Convert energy or mass units using only the Python standard library."""

import argparse
from decimal import Decimal, InvalidOperation
import sys


UNITS = {
    "kWh": ("energy", Decimal("1")),
    "MWh": ("energy", Decimal("1000")),
    "GWh": ("energy", Decimal("1000000")),
    "g": ("mass", Decimal("1")),
    "kg": ("mass", Decimal("1000")),
    "t": ("mass", Decimal("1000000")),
}


def format_decimal(value: Decimal) -> str:
    return format(value.normalize(), "f")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convert between supported energy units or mass units."
    )
    parser.add_argument("--value", required=True, help="numeric value to convert")
    parser.add_argument(
        "--from",
        dest="from_unit",
        required=True,
        choices=UNITS,
        help="unit of the input value",
    )
    parser.add_argument(
        "--to",
        dest="to_unit",
        required=True,
        choices=UNITS,
        help="unit to convert to",
    )
    args = parser.parse_args()

    try:
        value = Decimal(args.value)
    except InvalidOperation:
        parser.error("--value must be a valid decimal number")
    if not value.is_finite():
        parser.error("--value must be finite")

    from_dimension, from_factor = UNITS[args.from_unit]
    to_dimension, to_factor = UNITS[args.to_unit]
    if from_dimension != to_dimension:
        parser.error(
            f"cannot convert between {from_dimension} and {to_dimension} units"
        )

    converted = value * from_factor / to_factor
    print(
        f"{format_decimal(value)} {args.from_unit} = "
        f"{format_decimal(converted)} {args.to_unit}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
