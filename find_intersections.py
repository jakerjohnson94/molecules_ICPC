# """
# Write a function that will find the intersection with the widest
# angle between the strings (that is, lowest index pairs)
# that will maximize the potential interior area.
# """


def find_intersections(w1, w2):
    """
  # Return a sorted list of tuples that represent intersection points.
  # The sorting order should be from best to worst (e.g. lowest indices
  # to highest) Return None if no intersections are found.
    """
    intersections = []
    for i, x in enumerate(w1):
        for j, y in enumerate(w2):
            if x == y:
                intersections.append((i, j))

    intersections.sort(key=lambda x: sum(x))
    return intersections if intersections else None


words = ('OIMDIHEIAFNL', 'CHJDBJMHPJKD')


print(find_intersections(*words))
