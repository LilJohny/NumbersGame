import random


class Generator():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_sequence(self, length):
        pass

    def get_random_number(self, max_number_of_sequnce):
        pass


class UlamNumbersGenerator(Generator):
    def __init__(self):
        self.sequence = [1, 2, 3]

    def get_sequence(self, length):
        first = 0
        second = 1

        for i in range(length - 2):
            if i % 2 == 0:
                self.sequence.append(
                    self.sequence[first] + self.sequence[second + 1])
                second += 1
            else:
                self.sequence.append(
                    self.sequence[first + 1] + self.sequence[second + 1])
                first += 1
                second += 1
        return self.sequence

    def get_random_number(self, max_number_of_sequnce):
        ulam_sequence = self.get_sequence(max_number_of_sequnce)
        return random.choice(ulam_sequence)
