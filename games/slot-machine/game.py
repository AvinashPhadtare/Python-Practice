# game.py

import random
from utils import get_slot_machine_spin, print_slot_machine, check_winnings
from input_handler import get_number_of_lines, get_bet


class SlotMachine:

    def __init__(self, balance):
        self.balance = balance
        self.free_spins = 0

    def spin(self):
        print(f"\n💰 Current balance: ₹{self.balance}")
        print(f"🎁 Free spins available: {self.free_spins}")

        lines = get_number_of_lines()
        bet = get_bet()

        total_bet = bet * lines

        # 🎁 FREE SPIN
        if self.free_spins > 0:
            print("🎉 Using FREE SPIN!")
            self.free_spins -= 1
            total_bet = 0
        else:
            if total_bet > self.balance:
                print("❌ Not enough balance!")
                return

        print(f"\n🎯 Betting ₹{bet} on {lines} lines (Total: ₹{total_bet})")

        slots = get_slot_machine_spin()
        print_slot_machine(slots)

        winnings, winning_lines = check_winnings(slots, lines, bet)

        # 🎯 MULTIPLIER
        multiplier = random.choice([1, 2, 3])
        winnings *= multiplier

        # 🎁 BONUS
        if random.random() < 0.1:
            bonus = random.randint(10, 50)
            winnings += bonus
            print(f"🎉 BONUS WON: ₹{bonus}")

        # 🎁 FREE SPIN REWARD
        if random.random() < 0.15:
            free_spin_reward = random.randint(1, 3)
            self.free_spins += free_spin_reward
            print(f"🎁 You won {free_spin_reward} FREE SPIN!")

        net = winnings - total_bet
        self.balance += net

        print(f"\n💵 Winnings: ₹{winnings} (x{multiplier})")

        if winnings > 0:
            print("✅ Winning lines:", *winning_lines)
        else:
            print("❌ No win this time")

        print(f"💰 New balance: ₹{self.balance}")