#!/usr/bin/python3

"""Dell ePPID decoder"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Final, Optional
import re
from base_repr import repr_to_int

SERIAL_LENGTH: Final = 20
SERIAL_EXT_LENGTH: Final = 23

REGEX: Final = re.compile(
    r"""
    ([A-Z]{2})       # country-code
    .([A-Z\d]{5})    # part number
    ([A-Z\d]{5})     # manufacturer id
    (\d)             # year (last digit)
    ([1-9A-C])       # month (base36)
    ([1-9A-V])       # date (base36)
    ([A-Z\d]{4})     # sequence number
    ([A-Z\d]{3})?    # optional firmware version
    """,
    re.X | re.A
)

__all__ = (
    "Eppid",
)


@dataclass(frozen=True, slots=True)
class Eppid:
    """Dell ePPID content"""

    country: str

    part_number: str

    manufacturer: str

    year: int

    month: int

    day: int

    sequence: str

    firmware_version: Optional[str]

    @classmethod
    def from_string(cls, eppid: str) -> Eppid:
        """Parse ePPID from string"""
        if len(eppid) > SERIAL_EXT_LENGTH:
            raise ValueError("ePPID is too long")

        if len(eppid) < SERIAL_LENGTH:
            raise ValueError("ePPID is too short")

        result = REGEX.fullmatch(eppid)
        if result is None:
            raise ValueError(f"Malformed ePPID '{eppid}'")

        return cls(
            country=result[1],
            part_number=result[2],
            manufacturer=result[3],
            year=int(result[4]),
            month=repr_to_int(result[5], base=36),
            day=repr_to_int(result[6], base=36),
            sequence=result[7],
            firmware_version=result[8]
        )
