from bp2md.repair import BanglaRepair

repair = BanglaRepair()

samples = [
    "শবদ্যািয়",
    "প িা",
    "েি",
    "।।",
]

for text in samples:
    print("Before:", text)
    print("After :", repair.repair(text))
    print("-" * 40)