from datetime import date


def format_to_value(value: float, format_as_decimal: bool = False) -> str:
    if format_as_decimal:
        value = round(value, 2)
        return value
    
    value = f"R$ {value:.2f}"
    return value.replace(".", ",")


def format_to_date(date_as_object: date, format: str = "%d/%m/%Y") -> str:
    return date_as_object.strftime(format)
