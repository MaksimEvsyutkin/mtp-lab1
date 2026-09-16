import secrets
import string


def generate_password(length: int = 16) -> str:
    """Generate a random secure password."""
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    return "".join(secrets.choice(chars) for _ in range(length))


if __name__ == "__main__":
    pwd = generate_password()
    print(f"Сгенерированный пароль: {pwd}")
