import random


def largest_rectangle(n):
    rectangles = []
    for i in range(n):
        w = random.randint(2, 9)
        h = random.randint(w, 9)
        rectangles.append((w, h))

    return sorted(rectangles, key=lambda x: x[0] * x[1], reverse=True)


print(largest_rectangle(50))
