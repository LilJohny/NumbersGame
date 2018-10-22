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
        '''
        object,number -> list
        This function creates and returns the list of Ulam numbers with a random sequence.
        '''
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
        '''
        object,number -> number
        This function returns a random number.
        '''
        ulam_sequence = self.get_sequence(max_number_of_sequnce)
        return random.choice(ulam_sequence)


class PrimeNumbersGenerator(Generator):
    def __init__(self, *args, **kwargs):
        self.sequence = [2]

    def get_sequence(self, length):
        '''
        object,number -> list
        This function creates and returns a list of prime numbers with a random sequence.
        '''
        if(length > len(self.sequence)):
            last = self.sequence[len(self.sequence) - 1]

        else:
            return self.sequence[:length]

        number = last

        while len(self.sequence) < length:
            number += 1

            if self.isPrime(number):
                self.sequence.append(number)

        return self.sequence

    def get_random_number(self, max_number_of_sequnce):
        '''
        object,number -> number
        This function returns a random number.
        '''
        prime_sequence = self.get_sequence(max_number_of_sequnce)
        return random.choice(prime_sequence)

    @staticmethod
    def isPrime(number):
        '''
        number -> bool
        This function checks wheather the number is prime
        '''
        for factor in range(2, (number//2)+1):
            if(number % factor == 0):
                return False

        return True

class Lucky_Numbers_Generator(Generator):
    def __init__(self):
        self.happies = []
        self.create_sequence()

    def ishappy(self, n):
        '''
        object,number -> bool
        This function creates a list of happy numbers
        '''
        cache = []
        while n != 1:
            n = sum(int(i)**2 for i in str(n))
            if n in cache:
                return False
            cache.append(n)
        return True

    def get_sequence(self, length_of_list):
        '''
        object,number -> number
        This function returns a list of happy numbers in a random sequence 
        '''
        return self.happies[:length_of_list]

    def get_random_number(self, max_number_of_sequnce):
        '''
        object,number -> number
        This function chooses random numbers out of happy numbers.
        '''
        happies = self.get_sequence(max_number_of_sequnce)
        return random.choice(happies)

    def create_sequence(self):
        '''
        object -> list
        This function creates a list of numbers in a random sequence.random
        '''
        for i in range(1, 1001):
            if self.ishappy(i):
                self.happies.append(i)
        return self.happies