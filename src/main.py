import widget
import processing

print(widget.mask_account_card("Visa Platinum 7000792289606361"))
print(widget.mask_account_card("Счет 73654108430135874305"))
print(widget.get_date("2024-03-11T02:26:18.671407"))

# Выход функции со статусом по умолчанию 'EXECUTED'
client_bank_operations = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

print(f"filter_by_state(): \n\t{processing.filter_by_state(client_bank_operations)}\n")
print(f"filter_by_state(): \n\t{processing.filter_by_state(client_bank_operations, "CANCELED")}\n")

print(f"sort_by_date(): \n\t{processing.sort_by_date(client_bank_operations)}\n")
print(f"sort_by_date(): \n\t{processing.sort_by_date(client_bank_operations, False)}\n")