import random
import datetime

geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
target = "Not all those who wander are lost."

def generateParent(length):
    genes = list("")
    for i in range(0,length):
        geneIndex = random.randint(0, len(geneset) -1);
        genes.append(geneset[geneIndex])
    return(''.join(genes))

def getFitness(candidate, target):
   fitness = 0
   for i in range(0, len(candidate)):
       if target[i] == candidate[i]:
           fitness += 1
   return(fitness)

def mutate(parent):
   geneIndex = random.randint(0, len(geneset) -1);
   index = random.randint(0, len(parent) - 1)
   genes = list(parent)
   genes[index] = geneset[geneIndex]
   return(''.join(genes))

def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    fitness = getFitness(candidate, target)
    print ("%s\t%i\t%s" % (candidate, fitness, str(timeDiff)))

length = len(target)
print("Target = ", target)
parent = generateParent(length)
print("Parent = ", parent)
fitness = getFitness(parent, target)
print("Fitness = ", fitness)
display(parent, datetime.datetime.now())
new_parent = mutate(parent)
print("New parent = ", new_parent)


while fitness < len(parent):
    child = mutate(parent)
    childFitness = getFitness(child, target)

    if childFitness > fitness:
        fitness = childFitness
        parent = child
        display(parent, datetime.datetime.now())