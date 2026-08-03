from game import SlotMachine
from input_handler import deposit


def main():
    balance = deposit()
    machine = SlotMachine(balance)

    while True:
        ans = input("\nPress Enter to spin (q to quit): ").lower().strip()
        if ans == "q":
            break
        machine.spin()

    print(f"\n🏁 Final balance: ₹{machine.balance}")


if __name__ == "__main__":
    main()
