import random
import time

def log_random_number():
    # Generate a random number
    rand_num = random.randint(1, 100)

    # Open log file in append mode
    with open("random_log.txt", "a") as log_file:
        log_file.write(f"{time.ctime()}: {rand_num}\n")
    print(f"Logged number: {rand_num}")

if __name__ == "__main__":
    log_random_number()
