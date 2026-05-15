def trigger_error():
    return 10 / 2  # change to 10 / 0 to simulate failure


if __name__ == "__main__":
    trigger_error()
