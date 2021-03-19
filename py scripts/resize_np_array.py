import numpy as np
import fire
from typing import Tuple


def resize(oldsize, newsize):
    temp = np.random.randn(oldsize[0], oldsize[1])
    print(np.reshape(temp, newsize))


if __name__ == "__main__":
    resize((4, 5), (5, 4))
