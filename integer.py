class IntegerSet:
    def __init__(self, elements):
        self.elements = set(elements)

    def sum(self):

        return sum(self.elements)

    def mean(self):

        if not self.elements:
            return None
        return sum(self.elements) / len(self.elements)

    def max(self):

        if not self.elements:
            return None
        return max(self.elements)

    def min(self):

        if not self.elements:
            return None
        return min(self.elements)


if __name__ == "__main__":
    my_set = IntegerSet([1, 2, 3, 4, 5])
    print("Sum:", my_set.sum())
    print("Mean:", my_set.mean())
    print("Max:", my_set.max())
    print("Min:", my_set.min())

    empty_set = IntegerSet([])
    print("Sum of empty set:", empty_set.sum())
    print("Mean of empty set:", empty_set.mean())
    print("Max of empty set:", empty_set.max())
    print("Min of empty set:", empty_set.min())
