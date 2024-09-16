# Get Random Element from collection
import random


def get_random_data(data: list):
    random_index = random.randint(0, len(data) - 1)

    return data[random_index]
