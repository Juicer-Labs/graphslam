from json.tool import main
from unicodedata import name
import numpy as np

from transformation_funcs import inv_t


def test(amount):

    count = 0

    for _ in range(0, amount):

        # matrix to test
        # m = np.random.randint(100, size=(3, 3))
        m = np.random.rand(3, 3)

        # inv_t() inverse matrix
        inverse_a = inv_t(m)

        # np.linalg.inv() inverse matrix
        inverse_b = np.linalg.inv(m)

        # count += 1 if np.array_equal(inverse_a, inverse_b) else 0
        count += 1 if np.allclose(inverse_a, inverse_b) else 0

        print(inverse_a)
        print("\n")
        print(inverse_b)

    print("inverse matrix testing with {}/{} correct.".format(count, amount))


if __name__ == '__main__':
    test(1)
