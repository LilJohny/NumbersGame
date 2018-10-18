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
        self.sequence = [1, 2]

    def get_sequence(self, length):
        if length > len(self.sequence):
            for _ in range(length - len(self.sequence)):
                possible_members = []
                for j in range(len(self.sequence)):
                    for p in range(j + 1, len(self.sequence)):
                        possible_members.append(
                            self.sequence[j] + self.sequence[p])
                possible_members = [var for var in possible_members if all(
                    i < var for i in self.sequence) and possible_members.count(var) == 1]

                self.sequence.append(min(possible_members))
            return self.sequence
        else:
            return self.sequence[:length]

    def get_random_number(self, max_number_of_sequnce):
        ulam_sequence = self.get_sequence(max_number_of_sequnce)
        return random.choice(ulam_sequence)


class PrimeNumbersGenerator(Generator):
    def __init__(self, *args, **kwargs):
        self.sequence = [2]

    def get_sequence(self, length):
        self.sequence = [2]

        number = 3

        while len(self.sequence) < length:
            if PrimeNumbersGenerator.isPrime(number):
                self.sequence.append(number)

            number += 1

        return self.sequence

    def get_random_number(self, max_number_of_sequnce):
        prime_sequence = self.get_sequence(max_number_of_sequnce)
        return random.choice(prime_sequence)

    def isPrime(number):
        for factor in range(2, (number//2)+1):
            if(number % factor == 0):
                return False

        return True
