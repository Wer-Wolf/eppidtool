#!/usr/bin/python3

"""Dell ePPID decoder"""

from __future__ import annotations
from dataclasses import dataclass
import re
import base36

SERIAL_LENGTH = 20
SERIAL_EXT_LENGTH = 23

regex = re.compile(r"""([A-Z]{2})       # country-code
                       .([A-Z\d]{5})    # part number
                       ([A-Z\d]{5})     # manufacturer id
                       (\d)             # year (last digit)
                       ([0-9A-C])       # month (base36)
                       ([0-9A-V])       # date (base36)
                       ([A-Z\d]{4})     # sequence number
                       ([A-Z\d]{3})?    # optional firmware version
                       """, re.X | re.A)

__all__ = (
    "Eppid",
)


@dataclass(frozen=True)
class Eppid:
    """Dell ePPID content"""

    country: str

    part_number: str

    manufacturer: str

    year: int

    month: int

    day: int

    sequence: str

    firmware_version: str

    __slots__ = (
        "country",
        "part_number",
        "manufacturer",
        "year",
        "month",
        "day",
        "sequence",
        "firmware_version"
    )

    @classmethod
    def from_string(cls, eppid: str) -> Eppid:
        """Parse ePPID from string"""
        if len(eppid) > SERIAL_EXT_LENGTH:
            raise ValueError("ePPID is too long")
        elif len(eppid) < SERIAL_LENGTH:
            raise ValueError("ePPID is too short")

        result = regex.fullmatch(eppid)
        if result is None:
            raise ValueError(f"Malformed ePPID '{eppid}'")

        return cls(
            country=result[1],
            part_number=result[2],
            manufacturer=result[3],
            year=int(result[4]),
            month=base36.loads(result[5]),
            day=base36.loads(result[6]),
            sequence=result[7],
            firmware_version=result[8]
        )
