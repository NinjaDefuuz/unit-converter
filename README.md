- [LB23 Unit Converter](#lb23-unit-converter)
  - [Features](#features)
  - [Current Converter Types](#current-converter-types)
  - [Tech Stack](#tech-stack)
  - [How to run](#how-to-run)
  - [Adding New Converters](#adding-new-converters)
  - [Future Plans](#future-plans)
  - [Author](#author)


# LB23 Unit Converter
A simple and extendable unit converter built with Python, Flask and vanilla Javascript.
Supports multiple converter types and dynamically updates available units based on the selected category.

Started as a roadmap.sh project, to be implemented to my own website.

## Features
- Dynamic dropdown that change units based on converter type
- Length converter
- Weight converter
- Clean UI with simple HTML/CSS
- Flask backend with structured converter functions
- Easy to extend with new converter types (temperature, mass air flow, etc.)

## Current Converter Types
- Length units
  - m, cm, mm, km
  - in, ft, yd, mi
- Weight units
  - kg, g, lb, oz
- Temperature Units (Planned)
  - °C, °F, K
- Air units (Planned)
  - bar, psi, Pa, kPa
  - m³/s, m³/h, CFM, l/s
- Mass Units (Planned)
  - kg, metric ton, long ton, short ton

## Tech Stack
- Flask
- HTML / CSS
- JavaScript
- Jinja2 templates

## How to run

1. Install dependencies (Flask):
    
    pip install flask

1. Run the project:
    
    python app.py

1. Open the browser:

    http://127.0.0.1:5000

## Adding New Converters
Add new converters simply by:
1. Creating a function in converter_core.py
2. Expanding UNITS_OPTIONS in converter.html
3. Adding logic in app.py:
   
   elif converter_type == "your_type":

    converted = convert_your_type(value, from_unit, to_unit)


## Future Plans

- [x] Implement Length converter
- [x] Implement Weight converter
- [ ] Implement temperature converter
- [ ] Implement air converter
- [ ] Implement Mass converter
- [ ] Implement HVAC converter
- [ ] Mobile friendly UI redesign
- [ ] Add unit symbols
- [ ] Dark mode

## Author
**Lars Jonny Steine Jensen / LB23**

*A multi-project engineering mind learning Python, data science, and messing around with other cool stuff.*