import string
import random


def tracking_gen():
    return "".join(
        random.choice(string.ascii_lowercase + string.digits) for i in range(8)
    )
