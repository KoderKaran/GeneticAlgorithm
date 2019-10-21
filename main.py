import string
import random as ra


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
        self.maters = None

    def make_pop(self):
        for i in range(self.pop_size):
            member = ''.join(ra.choice(self.letters) for k in range(self.size))
            self.population.append(member)
        print("Initial population:", self.population)

    def fit_check(self, member):
        letters_member = list(member)
        letters_target = list(self.target)
        fitness = 0
        for i in range(len(letters_target)):
            if letters_target[i] == letters_member[i]:
                fitness+=1
        return fitness

    def get_mates(self):
        mate_check = {}
        for i in self.population:
            fit = self.fit_check(i)
            mate_check[i] = fit
        self.maters = sorted(mate_check, key=mate_check.get, reverse=True)[:10]

    def mate(self):
        times = int(self.pop_size / len(self.maters))
        for i in range(times):
            for member in self.maters:
                new_member = []
                self.maters.remove(member)
                other_mater = ra.choice(self.maters)
                gene_pool = list(other_mater) + list(member)
                for letter in range(len(self.target)):
                    new_letter = ra.choice(gene_pool)
                    new_member.append(new_letter)
                    gene_pool.remove(new_letter)
                self.maters.append(member)
                self.new_pop.append(''.join(new_member))

    def mutation(self):
        '''
        for i in range(len(self.new_pop)):
            list_member = list(self.new_pop[i])
            chance = ra.uniform(0, 1)
            if chance < self.mute_rate:
                index_affected = ra.randint(0, len(list_member)-1)
                list_member[index_affected] = ra.choice(self.letters)
            self.new_pop[i] = ''.join(list_member)
            '''
        for i in range(len(self.new_pop)):
            list_member = list(self.new_pop[i])
            for letter in range(len(list_member)):
                chance = ra.uniform(0, 1)
                if chance <= self.mute_rate:
                    list_member[letter] = ra.choice(self.letters)
            self.new_pop[i] = ''.join(list_member)

    def progress(self):
        high_score = 0
        high_member = ""
        for i in self.new_pop:
            if self.fit_check(i) > high_score:
                high_member = i
        print("Generation: " + str(self.generations + 1) + " Closest member: " + high_member)

    def check(self):
        for i in self.new_pop:
            if i == self.target:
                print("Solution found in " + str(self.generations) + " generations!", i)
                return True
        return False

    def reset(self):
        self.population = self.new_pop
        self.maters = None
        self.new_pop = []
        self.generations += 1


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
    inp = input("")
