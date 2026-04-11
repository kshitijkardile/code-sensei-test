def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def get_primes(limit):
    """Return all prime numbers up to limit."""
    return [n for n in range(2, limit + 1) if is_prime(n)]


if __name__ == "__main__":
    # Test
    print("Is 17 prime?", is_prime(17))
    print("Primes up to 30:", get_primes(30))