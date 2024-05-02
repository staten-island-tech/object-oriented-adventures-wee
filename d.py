import random

population = ['Red', 'Blue', 'Green']
weights = [0.6, 0.3, 0.1]

chosen = random.choices(population, weights, k=5)
print(chosen)