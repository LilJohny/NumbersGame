import random


class Generator:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_sequence(self, length):
        pass

    def get_random_number(self, max_number_of_sequence):
        pass

    def is_from_sequence(self, element):
        pass

    def get_generator_name(self):
        pass


class UlamNumbersGenerator(Generator):
    def __init__(self):
        self.sequence = [1, 2]

    def get_sequence(self, length):
        """
        object,number -> list
        Creates a list of Ulam numbers with a certain length.
        """
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

    def get_random_number(self, max_number_of_sequence):
        """
        object,number -> number
        Takes a random number of a list of Ulam numbers
        """
        ulam_sequence = self.get_sequence(max_number_of_sequence)
        return random.choice(ulam_sequence)

    def is_from_sequence(self, element):
        """
        object,number -> bool
        Checks whether an element is from list.
        """
        length = 1
        seq = self.get_sequence(length)
        while seq[len(seq) - 1] < element:
            length += 1
            seq = self.get_sequence(length)
        return element in seq

    def get_generator_name(self):
        """
        object -> str
        Returns a string:'It is Ulam sequence'
        """
        return 'It is Ulam sequence'


class PrimeNumbersGenerator(Generator):
    def __init__(self):
        self.sequence = [2]

    def get_sequence(self, length):
        """
        object,number -> list
        Creates a list of prime numbers with a certain length.
        """
        if length > len(self.sequence):
            last = self.sequence[len(self.sequence) - 1]

        else:
            return self.sequence[:length]

        number = last

        while len(self.sequence) < length:
            number += 1

            if self.is_prime(number):
                self.sequence.append(number)

        return self.sequence

    def is_from_sequence(self, element):
        """
        object,number -> bool
        Checks whether an element is from list.
        """
        if element == 2:
            return True

        return self.is_prime(element)

    def get_random_number(self, max_number_of_sequence):
        """
        object,number -> number
        Takes a random number of a list of prime numbers
        """
        prime_sequence = self.get_sequence(max_number_of_sequence)
        return random.choice(prime_sequence)

    def get_generator_name(self):
        """
        object -> str
        Returns a string:'It is Prime sequence'
        """
        return 'It is Prime sequence'

    @staticmethod
    def is_prime(number):
        """
        number -> bool
        Checks whether the number is prime
        """
        for factor in range(2, (number // 2) + 1):
            if number % factor == 0:
                return False

        return True


class LuckyNumbersGenerator(Generator):
    def __init__(self):
        self.happies = []
        self.create_sequence()

    @staticmethod
    def is_happy(n):
        """
        object,number -> bool
        Makes a list of happy numbers.
        """
        cache = []
        while n != 1:
            n = sum(int(i) ** 2 for i in str(n))
            if n in cache:
                return False
            cache.append(n)
        return True

    def get_sequence(self, length_of_list):
        """
        object,number -> number
        Returns numbers from a list of happy numbers.
        """
        return self.happies[:length_of_list]

    def get_random_number(self, max_number_of_sequence):
        """
        object,number -> number
        Returns one number from a list of happy numbers.
        """
        happies = self.get_sequence(max_number_of_sequence)
        return random.choice(happies)

    def create_sequence(self):
        """
        object -> list
        Creates a list of happy numbers.
        """
        for i in range(1, 1001):
            if self.is_happy(i):
                self.happies.append(i)
        return self.happies

    def is_from_sequence(self, element):
        """
        object,number -> bool
        Checks whether a number belongs to happy ones list.
        """
        return self.is_happy(element)

    def get_generator_name(self):
        """
        object -> str
        Returns a string:'It is Happy sequence'
        """
        return 'It is Happy sequence'
