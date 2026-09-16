def get_mask_card_number(card_number: str) -> str:
    number = ""

    for i in range(len(card_number)):
        if i > 0 and i % 4 == 0:
            number += " "

        if i > 5 and i < 12:
            number += "*"
        else:
            number += card_number[i]

    return number


def get_mask_account(card_number: str) -> str:
    return "**" + card_number[-4::]
