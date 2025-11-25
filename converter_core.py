#converter_core.py

# 1 unit = X meters
LENGTH__IN_METERS = {
    "m": 1.0,
    "cm": 0.01,
    "mm": 0.001,
    "km": 1000.0,
    "in": 0.0254,
    "ft": 0.3048,
    "yd": 0.9144,
    "mi": 1609.34,
}

def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    #Converts between lenght units via meters.

    #Check supported units
    if from_unit not in LENGTH__IN_METERS:
        raise ValueError(f"Unknown unit: {from_unit}")
    if to_unit not in LENGTH__IN_METERS:
        raise ValueError(f"Unknown unit: {to_unit}")
    
    #Convert to meters
    value_in_meters = value * LENGTH__IN_METERS[from_unit]

    #Convert from meters to desired unit
    converted_value = value_in_meters / LENGTH__IN_METERS[to_unit]

    return converted_value

# 1 unit = X kilograms
WEIGHT_IN_KG = {
    "kg": 1.0,
    "g": 0.001,
    "lb": 0.45359237,
    "oz": 0.0283495231,
}

def convert_weight(value: float, from_unit: str, to_unit: str) -> float:
    #Converts between weight units via kilograms.
    if from_unit not in WEIGHT_IN_KG:
        raise ValueError(f"Unknown weight unit: {from_unit}")
    if to_unit not in WEIGHT_IN_KG:
        raise ValueError(f"Unknown weight unit: {to_unit}")
    
    #Converts to kg
    value_in_kg = value * WEIGHT_IN_KG[from_unit]
    
    #Converts from kg to desired unit
    converted_value = value_in_kg / WEIGHT_IN_KG[to_unit]
    return converted_value


def convert_temp(value: float, from_unit: str, to_unit: str) -> float:
    #Converts between Celsius, Fahrenheit, and Kelvin.

    if from_unit == "c":
        value_c = value
    elif from_unit == "f":
        value_c = (value - 32) * 5/9
    elif from_unit == "k":
        value_c = value - 273.15
    else:
        raise ValueError(f"Unknown temperature unit: {from_unit}")
    
    
    if to_unit == "c":
        return value_c
    elif to_unit == "f":
        return (value_c * 9/5) + 32
    elif to_unit == "k":
        return value_c + 273.15
    else:
        raise ValueError(f"Unknown temperature unit: {to_unit}")