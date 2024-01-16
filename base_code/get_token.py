import random
import string

def generate_random_token_string(length):
    characters = string.ascii_letters + string.digits  # Bao gồm chữ cái và số
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

# random_token = generate_random_token_string(12)
# print(random_token)
