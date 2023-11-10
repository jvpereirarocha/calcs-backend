from datetime import date


def format_to_value(value: float) -> str:
    value = f"R$ {value:.2f}"
    return value.replace(".", ",")


def format_to_date(date_as_object: date, format: str = "%d/%m/%Y") -> str:
    return date_as_object.strftime(format)
