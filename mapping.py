import datetime

MONTHS = [
    "Alfa",
    "Bravo",
    "Charlie",
    "Delta",
    "Echo",
    "Foxtrot",
    "Golf",
    "Hotel",
    "India",
    "Juliett",
    "Kilo",
    "Lima",
]

DAYS = [
    "aardvark",
    "apple",
    "blackjack",
    "bookshelf",
    "cement",
    "decimal",
    "detergent",
    "dinosaur",
    "examine",
    "framework",
    "goldfish",
    "gravity",
    "hockey",
    "hydraulic",
    "inertia",
    "intention",
    "keyboard",
    "microwave",
    "molecule",
    "nebula",
    "potato",
    "rhythm",
    "sailboat",
    "shadow",
    "snapshot",
    "speculate",
    "stairway",
    "sugar",
    "treadmill",
    "unicorn",
    "voyager",
]


def get_pair(dt):
    return (MONTHS[dt.month - 1] + " " + DAYS[dt.day - 1]).title()


def main():
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=1)
    print("Today:   ", get_pair(now))
    print("Tomorrow:", get_pair(tomorrow))


if __name__ == "__main__":
    main()
