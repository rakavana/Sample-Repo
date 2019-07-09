import math
import os
import sys

import requests

print(sys.version)
print(sys.executable)


def adjacentElementsProduct(inputArray):
    largeValue = 0
    length = len(inputArray)
    for i in range(len(inputArray) - 1):
        if i != len(inputArray) - 1:
            largeValue1 = inputArray[i] * inputArray[i + 1]
            if largeValue < largeValue1:
                largeValue = largeValue1
        else:
            largeValue2 = inputArray[length - 1] * inputArray[length]
            if largeValue < largeValue2:
                largeValue = largeValue2
    print(largeValue)


r = requests.get("https://www.google.com")
print(r.status_code)
