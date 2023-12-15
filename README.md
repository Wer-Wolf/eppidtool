[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
![Tests](https://github.com/Wer-Wolf/eppidtool/actions/workflows/Tests.yaml/badge.svg)
[![codecov](https://codecov.io/github/Wer-Wolf/eppidtool/graph/badge.svg?token=MLRT213ONH)](https://codecov.io/github/Wer-Wolf/eppidtool)

# eppidtool

The `eppidtool` package can be used to parse Dell ePPIDs, which can be found on various components inside Dell computers.

It also contains an CLI entrypoint, which can be used to quickly decode
ePPIDs from the command line.

To use it, execute `eppidtool` or `python3 -m eppidtool` followed by the ePPID.

## Requirements

Python >= 3.10 is required to use this package.

## Optional Features

If `pycountry` is installed, the country of origin as specified by the ePPID will be displayed in a more user-friendly form
(for example "Germany" instead of "DE").

To automatically install `pycountry`, install `eppidtool` with:

    python3 -m pip install 'eppidtool[extra]'

## Code Examples

```
from eppidtool.eppid import Eppid

eppid = Eppid.from_string("CN0WJPC49ZC00154836EA05")
print(eppid.country)            # CN
print(eppid.part_number)        # WJPC4
print(eppid.manufacturer)       # 9ZC00
print(eppid.year)               # 1
print(eppid.month)              # 5
print(eppid.day)                # 4
print(eppid.sequence)           # 836E
print(eppid.firmware_version)   # A05
```

## CLI Examples

```
$ python3 -m eppidtool CN0WJPC49ZC00154836EA05
Country: China
Part Number: WJPC4
Year/Month/Day: 1/5/4
Manufacturer Identification: 9ZC00
Manufacturer Sequence Number: 836E
Firmware Version: A05
```

If your ePPID seems to be faulty, try the `--adjust` option:
```
$ python3 -m eppidtool CN0WJPC49ZC00154836EA0 --adjust
Country: China
Part Number: WJPC4
Year/Month/Day: 1/5/4
Manufacturer Identification: 9ZC00
Manufacturer Sequence Number: 836E
```
