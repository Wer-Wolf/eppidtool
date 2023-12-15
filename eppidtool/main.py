#!/usr/bin/python3

"""CLI entrypoint utilities"""

from argparse import ArgumentParser, Namespace
from contextlib import suppress
from typing import Final
from . import __doc__ as description, __version__
from .eppid import SERIAL_LENGTH, SERIAL_EXT_LENGTH, Eppid

with suppress(ImportError):
    from pycountry import countries

__all__ = (
    "ARGUMENT_PARSER",
    "main",
    "main_cli"
)

ARGUMENT_PARSER: Final = ArgumentParser(
    prog="eppidtool",
    description=description
)
ARGUMENT_PARSER.add_argument(
    "-v",
    "--version",
    action="version",
    version=f"%(prog)s {__version__}"
)
ARGUMENT_PARSER.add_argument(
    "-a",
    "--adjust",
    action="store_true",
    help="Adjust size of ePPID if necessary"
)
ARGUMENT_PARSER.add_argument(
    "eppid",
    metavar="EPPID",
)


def main(args: Namespace) -> int:
    """Entrypoint for the ePPID tool"""
    eppid_str = args.eppid

    if args.adjust:
        if len(eppid_str) > SERIAL_EXT_LENGTH:
            eppid_str = eppid_str[:SERIAL_EXT_LENGTH]
        elif len(eppid_str) < SERIAL_EXT_LENGTH:
            eppid_str = eppid_str[:SERIAL_LENGTH]

    try:
        eppid = Eppid.from_string(eppid_str)
    except ValueError as e:
        print(f"Parsing failed: {e}")
        return 1

    try:
        country = countries.get(alpha_2=eppid.country).name
    except NameError:
        country = eppid.country

    print(f"Country: {country}")
    print(f"Part Number: {eppid.part_number}")
    print(f"Year/Month/Day: {eppid.year}/{eppid.month}/{eppid.day}")
    print(f"Manufacturer Identification: {eppid.manufacturer}")
    print(f"Manufacturer Sequence Number: {eppid.sequence}")
    if eppid.firmware_version is not None:
        print(f"Firmware Version: {eppid.firmware_version}")

    return 0


def main_cli() -> int:
    """CLI entrypoint"""
    return main(ARGUMENT_PARSER.parse_args())
