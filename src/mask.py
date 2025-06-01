def get_mask_card_number(card_number: int) -> str:  # XXXX XX** **** XXXX
    """Функция принимает на вход номер карты и возвращает ее маску"""
    return f"{str(card_number)[0:4]} {str(card_number)[4:6]}** **** {str(card_number)[12:16]}"


def get_mask_account(account_number: int) -> str:  # **XXXX
    """Функция принимает на вход номер счета и возвращает его маску"""
    return f"**{str(account_number)[12:16]}"
