from datetime import datetime


VERSION = "0.1.0"


def startup():
    print("================================")
    print(" OpenRoIP Backend Starting")
    print(f" Version: {VERSION}")
    print(f" Time: {datetime.now()}")
    print(" Status: Ready")
    print("================================")


if __name__ == "__main__":
    startup()