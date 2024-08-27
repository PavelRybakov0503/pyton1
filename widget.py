import masks

def mask_account_card(number: str) -> str:
'''принимает на вход строку формата'''
    if get_mask_card_number in number:
        return masks.get_mask_account(number)

    else:
        cards = masks.get_mask_account(number[-16:])
        new_cards = number.replace(number[-16:],cards)
        return new_cards

def get_date():
    '''фунуция преобразования даты'''

    return f'{date[8:10]},{date[5:7]},{date[0:4]}'
    pass