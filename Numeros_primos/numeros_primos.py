import time

def verify_prime(number):
    for i in range(number + 1):
        if i not in (0, 1, number):
            if (number % i) == 0:
               return "Não é primo"

    return "É primo"

if __name__ == "__main__":
    start1 = time.time()
    print(f"O número 100: ")
    for i in range(1, 100):
        print(f"{i}: {verify_prime(100)}")
    end1 = time.time()

    start2 = time.time()
    print(f"O número 1.000: ")
    for i in range(1, 1000):
        print(f"{i}: {verify_prime(1000)}")
    end2 = time.time()

    start3 = time.time()
    print(f"O número 1.000.000: ")
    for i in range(1, 1000000):
        print(f"{i}: {verify_prime(1000000)}")
    end3 = time.time()

    print(f"\nTempo 1: {(end1 - start1) * 1000}s")
    print(f"Tempo 2: {(end2 - start2) * 1000}s")
    print(f"Tempo 3: {(end3 - start3) * 1000}s")
