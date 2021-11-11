import random
import sys

def random_picker() -> str:
    inputs = sys.argv[1:]
    chosen = random.choice(inputs)
    return chosen

if __name__ == "__main__":
    print(f"THE CHOSEN FROM {[i for i in sys.argv[1:]]} is: ({random_picker().upper()})")
    