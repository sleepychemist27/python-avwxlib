# python-avwxlib
python-avwxlib is a user-friendly python module for obtaining up-to-date METARs, TAFS, and PIREPS from aerodromes worldwide built on the avwx.rest api.

## Installation

pip install is not currently possible, but I am in the process of packaging it and submitting it to PyPI. In the meantime, download both files to your working directory and use as directed. 

It is necessary to register your own free account at [avwx.rest](https://avwx.rest) and obtain your access token. Copy and paste this token as a string on line 6 of avwx.py.
## Usage

```python
from avwx import Station, Metar, Taf

JFK = Station('JFK')
JFK.get_metar()
JFK.get_taf()
JFK.get_info()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
