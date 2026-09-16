import math
import secrets
import string


def generate_password(length: int = 16) -> str:
    """Generate a random secure password."""
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    return "".join(secrets.choice(chars) for _ in range(length))


def calculate_entropy(password: str) -> float:
    """Calculate Shannon entropy bits for password."""
    if not password:
        return 0.0
    pool_size = 0
    if any(c.islower() for c in password):
        pool_size += 26
    if any(c.isupper() for c in password):
        pool_size += 26
    if any(c.isdigit() for c in password):
        pool_size += 10
    if any(c in "!@#$%^&*()-_=+" for c in password):
        pool_size += 14

    if pool_size == 0:
        return 0.0
    return len(password) * math.log2(pool_size)


if __name__ == "__main__":
    pwd = generate_password()
    entropy = calculate_entropy(pwd)
    print(f"Сгенерированный пароль: {pwd}")
    print(f"Энтропия: {entropy:.2f} бит")
