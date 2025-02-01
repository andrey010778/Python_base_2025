import math
import time
#import PIL
from PIL import Image

#def print():
#    pass

#res = print('Hello world')
#img = Image.open('cat.jpg')
#img.show()
#print(res)
start = time.time()
a = int(input())
for _ in range(a):
    _ = input()
    summa = []
    arr = [int(x) for x in input().split()]
for i in range(len(arr)):
    arr1 = arr[:]
    arr1[i] = arr1[i] + 1
    summa.append(math.prod(arr1))
print(max(summa))
end = time.time()
print(f"This code took {(end - start) * 1000} ms to complete")