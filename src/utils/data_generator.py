import random
import string

def random_string(length: int = 10) -> str:
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def random_email() -> str:
    domains = ["test.com", "example.com", "demo.org"]
    return f"{random_string(8)}@{random.choice(domains)}"

def random_post_data(user_id: int = 1) -> dict:
    return {
        "userId": user_id,
        "title": f"Test Title {random_string(5)}",
        "body": f"Test Body {random_string(20)}"
    }