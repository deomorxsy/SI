#!/usr/bin/python3

def timeconv(dur):
    hours = dur // 3600
    mint = dur // 60
    sec = dur % 60

    return print("{}:{}:{}".format(hours, mint, sec))


if __name__ == "__main__":
    timeconv(int(input()))
