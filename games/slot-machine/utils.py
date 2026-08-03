# utils.py

import random
from config import ROWS, COLS, symbol_count, symbol_value

def get_slot_machine_spin():
    columns = []
    symbols = list(symbol_count.keys())
    weights = list(symbol_count.values())

    for _ in range(COLS):
        column = []
        for _ in range(ROWS):
            value = random.choices(symbols, weights=weights, k=1)[0]
            column.append(value)
        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])


def check_winnings(columns, lines, bet):
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol = columns[0][line]
        win = True

        for column in columns:
            if column[line] != symbol:
                win = False
                break

        if win:
            winnings += symbol_value[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines