import core.search.linear as linear
import core.search.binary as binary

def buble_search_max(numbers):
    max_el = int()

    return max_el

def main():
    numbers = [23,44,12,59,95,356,76,15,10]
    print(linear.linear_search(numbers, 356))

    numbers2 = [101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117]
    print(binary.binary_search(numbers2, 103, 0, len(numbers2)))

if __name__ == "__main__":
    main()