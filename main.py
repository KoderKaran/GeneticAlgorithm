import string
import random as ra
import math
import matplotlib.pyplot as ma
import numpy as np


class Population:
    def __init__(self, target, pop_size, mutation_rate):
        self.generations = 1
        self.target = target.lower()
        self.mute_rate = mutation_rate
        self.pop_size = pop_size
        self.letters = string.ascii_lowercase + " "
        self.size = len(self.target)
        self.new_pop = []
        self.population = []
        self.winner = None
        self.maters = []
        self.data = []

    def make_pop(self):
        for i in range(self.pop_size):
            member = ''.join(ra.choice(self.letters) for k in range(self.size))
            self.population.append(member)
        print("Initial population:", self.population)

    def fit_check(self, member):
        letters_member = list(member)
        letters_target = list(self.target)
        score = 0
        for i in range(len(letters_target)):
            if letters_target[i] == letters_member[i]:
                score += 1
        fitness = (score/self.size)*100
        return math.floor(fitness)

    def get_mates(self):
        for i in self.population:
            for j in range(self.fit_check(i)):
                self.maters.append(i)

    def mate(self):
        for i in range(len(self.population)):
            parent_one = list(ra.choice(self.maters))
            parent_two = list(ra.choice(self.maters))
            midpoint = ra.randint(0, len(parent_one) - 1)
            offspring = "".join(parent_one[:midpoint] + parent_two[midpoint:])
            self.new_pop.append(offspring)

    def mutation(self):
        for i in range(len(self.new_pop)):
            list_member = list(self.new_pop[i])
            chance = ra.uniform(0, 1)
            if chance < self.mute_rate:
                index_affected = ra.randint(0, len(list_member)-1)
                list_member[index_affected] = ra.choice(self.letters)
            self.new_pop[i] = ''.join(list_member)

    def progress(self):
        high_score = 0
        high_member = ""
        for i in self.new_pop:
            if self.fit_check(i) > high_score:
                high_member = i
                high_score = self.fit_check(i)
        self.data.append(high_score)
        print("Generation: " + str(self.generations + 1) + "\nClosest member: " + high_member + "\n")

    def check(self):
        for i in self.new_pop:
            if i == self.target:
                print("Solution found in " + str(self.generations) + " generations!", i)
                return True
        return False

    def reset(self):
        self.population = self.new_pop
        self.maters = []
        self.new_pop = []
        self.generations += 1


    def graph(self):
        gens = list(range(0, self.generations))
        print(self.data)
        ma.plot(gens, self.data, color='blue')
        ma.xlabel("Generation")
        ma.ylabel("Best fitness")
        ma.title("Highest fitness values by generation")
        ma.show()


if __name__ == "__main__":
    target_string = input("What word would you like to generate?")
    population = int(input("How big is each population? (Multiple of ten please)"))
    mute_rate = input("What is the mutation rate percent?")
    while True:
        if "%" in mute_rate:
            mute_rate = mute_rate.replace("%", "")
        else:
            break
    mute_rate = int(mute_rate)/100
    pop = Population(target_string, population, mute_rate)
    pop.make_pop()
    while True:
        pop.get_mates()
        pop.mate()
        pop.mutation()
        pop.progress()
        if pop.check():
            break
        pop.reset()
    pop.graph()
    inp = input("")
