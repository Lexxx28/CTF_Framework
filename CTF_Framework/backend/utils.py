def check_fields(input: dict, list: list) -> bool:
    for item in list:
        if not input.get(item):
            return True
    return False