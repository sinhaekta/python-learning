def main():
    print("Running main logic")

if __name__ == "__main__":
    main()

#example
def cleanup_logs():
    print("Cleaning old logs")

def main():
    cleanup_logs()

if __name__ == "__main__":
    main()

# importing a  module
from math_utils import say_hello

say_hello()