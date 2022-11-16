#!/usr/bin/python3

"""Tests for ePPID parsing"""

from unittest import TestCase
from typing import Final
from eppidtool.eppid import Eppid

EXAMPLE_COUNTY: Final = "CN"
EXAMPLE_PART_NUMBER: Final = "0WJPC4"
EXAMPLE_MANUFACTURER: Final = "9ZC00"
EXAMPLE_YEAR: Final = "1"
EXAMPLE_MONTH: Final = "5"
EXAMPLE_DAY: Final = "4"
EXAMPLE_SEQUENCE: Final = "836E"
EXAMPLE_FIRMWARE: Final = "A05"


class EppidTest(TestCase):
    """Tests for ePPid parsing"""

    def test_too_short(self) -> None:
        """test behaviour when ePPID is too short"""
        with self.assertRaises(ValueError):
            Eppid.from_string(
                EXAMPLE_COUNTY +
                EXAMPLE_PART_NUMBER +
                EXAMPLE_MANUFACTURER +
                EXAMPLE_YEAR +
                EXAMPLE_MONTH +
                EXAMPLE_DAY +
                "AB"
            )

    def test_too_long(self) -> None:
        """test behaviour when ePPID is too long"""
        with self.assertRaises(ValueError):
            Eppid.from_string(
                EXAMPLE_COUNTY +
                EXAMPLE_PART_NUMBER +
                EXAMPLE_MANUFACTURER +
                EXAMPLE_YEAR +
                EXAMPLE_MONTH +
                EXAMPLE_DAY +
                EXAMPLE_SEQUENCE +
                EXAMPLE_FIRMWARE +
                "A"
            )

    def test_country(self) -> None:
        """test country parsing"""
        eppid = Eppid.from_string(
            EXAMPLE_COUNTY +
            EXAMPLE_PART_NUMBER +
            EXAMPLE_MANUFACTURER +
            EXAMPLE_YEAR +
            EXAMPLE_MONTH +
            EXAMPLE_DAY +
            EXAMPLE_SEQUENCE +
            EXAMPLE_FIRMWARE
        )
        self.assertEqual(eppid.country, EXAMPLE_COUNTY)

    def test_part_number(self) -> None:
        """test part number parsing"""
        eppid = Eppid.from_string(
            EXAMPLE_COUNTY +
            EXAMPLE_PART_NUMBER +
            EXAMPLE_MANUFACTURER +
            EXAMPLE_YEAR +
            EXAMPLE_MONTH +
            EXAMPLE_DAY +
            EXAMPLE_SEQUENCE +
            EXAMPLE_FIRMWARE
        )
        self.assertEqual(eppid.part_number, EXAMPLE_PART_NUMBER[1:6])

    def test_manufacturer(self) -> None:
        """test manufacturer parsing"""
        eppid = Eppid.from_string(
            EXAMPLE_COUNTY +
            EXAMPLE_PART_NUMBER +
            EXAMPLE_MANUFACTURER +
            EXAMPLE_YEAR +
            EXAMPLE_MONTH +
            EXAMPLE_DAY +
            EXAMPLE_SEQUENCE +
            EXAMPLE_FIRMWARE
        )
        self.assertEqual(eppid.manufacturer, EXAMPLE_MANUFACTURER)

    def test_year(self) -> None:
        """test year parsing"""
        eppid = Eppid.from_string(
            EXAMPLE_COUNTY +
            EXAMPLE_PART_NUMBER +
            EXAMPLE_MANUFACTURER +
            EXAMPLE_YEAR +
            EXAMPLE_MONTH +
            EXAMPLE_DAY +
            EXAMPLE_SEQUENCE +
            EXAMPLE_FIRMWARE
        )
        self.assertEqual(eppid.year, int(EXAMPLE_YEAR))

    def test_invalid_year(self) -> None:
        """test invalid year parsing"""
        with self.assertRaises(ValueError):
            Eppid.from_string(
                EXAMPLE_COUNTY +
                EXAMPLE_PART_NUMBER +
                EXAMPLE_MANUFACTURER +
                "A" +
                EXAMPLE_MONTH +
                EXAMPLE_DAY +
                EXAMPLE_SEQUENCE +
                EXAMPLE_FIRMWARE
            )

    def test_month(self) -> None:
        """test month parsing"""
        eppid = Eppid.from_string(
            EXAMPLE_COUNTY +
            EXAMPLE_PART_NUMBER +
            EXAMPLE_MANUFACTURER +
            EXAMPLE_YEAR +
            EXAMPLE_MONTH +
            EXAMPLE_DAY +
            EXAMPLE_SEQUENCE +
            EXAMPLE_FIRMWARE
        )
        self.assertEqual(eppid.month, int(EXAMPLE_MONTH))

    def test_invalid_month(self) -> None:
        """test invalid month parsing"""
        with self.assertRaises(ValueError):
            Eppid.from_string(
                EXAMPLE_COUNTY +
                EXAMPLE_PART_NUMBER +
                EXAMPLE_MANUFACTURER +
                EXAMPLE_YEAR +
                "0" +
                EXAMPLE_DAY +
                EXAMPLE_SEQUENCE +
                EXAMPLE_FIRMWARE
            )

    def test_day(self) -> None:
        """test day parsing"""
        eppid = Eppid.from_string(
            EXAMPLE_COUNTY +
            EXAMPLE_PART_NUMBER +
            EXAMPLE_MANUFACTURER +
            EXAMPLE_YEAR +
            EXAMPLE_MONTH +
            EXAMPLE_DAY +
            EXAMPLE_SEQUENCE +
            EXAMPLE_FIRMWARE
        )
        self.assertEqual(eppid.day, int(EXAMPLE_DAY))

    def test_invalid_day(self) -> None:
        """test invalid day parsing"""
        with self.assertRaises(ValueError):
            Eppid.from_string(
                EXAMPLE_COUNTY +
                EXAMPLE_PART_NUMBER +
                EXAMPLE_MANUFACTURER +
                EXAMPLE_YEAR +
                EXAMPLE_MONTH +
                "0" +
                EXAMPLE_SEQUENCE +
                EXAMPLE_FIRMWARE
            )

    def test_sequence(self) -> None:
        """test sequence parsing"""
        eppid = Eppid.from_string(
            EXAMPLE_COUNTY +
            EXAMPLE_PART_NUMBER +
            EXAMPLE_MANUFACTURER +
            EXAMPLE_YEAR +
            EXAMPLE_MONTH +
            EXAMPLE_DAY +
            EXAMPLE_SEQUENCE +
            EXAMPLE_FIRMWARE
        )
        self.assertEqual(eppid.sequence, EXAMPLE_SEQUENCE)

    def test_firmware_version(self) -> None:
        """test firmware version parsing"""
        eppid = Eppid.from_string(
            EXAMPLE_COUNTY +
            EXAMPLE_PART_NUMBER +
            EXAMPLE_MANUFACTURER +
            EXAMPLE_YEAR +
            EXAMPLE_MONTH +
            EXAMPLE_DAY +
            EXAMPLE_SEQUENCE +
            EXAMPLE_FIRMWARE
        )
        self.assertEqual(eppid.firmware_version, EXAMPLE_FIRMWARE)

    def test_partial_firmware_version(self) -> None:
        """test partial firmware version parsing"""
        with self.assertRaises(ValueError):
            Eppid.from_string(
                EXAMPLE_COUNTY +
                EXAMPLE_PART_NUMBER +
                EXAMPLE_MANUFACTURER +
                EXAMPLE_YEAR +
                EXAMPLE_MONTH +
                EXAMPLE_DAY +
                EXAMPLE_SEQUENCE +
                EXAMPLE_FIRMWARE[0:2]
            )

    def test_missing_firmware_version(self) -> None:
        """test missing firmware version parsing"""
        eppid = Eppid.from_string(
            EXAMPLE_COUNTY +
            EXAMPLE_PART_NUMBER +
            EXAMPLE_MANUFACTURER +
            EXAMPLE_YEAR +
            EXAMPLE_MONTH +
            EXAMPLE_DAY +
            EXAMPLE_SEQUENCE
        )
        self.assertIsNone(eppid.firmware_version)
