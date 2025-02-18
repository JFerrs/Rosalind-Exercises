##Given  positive integers n<= 40 and k<=5, return the total number of rabbit pairs that will be present 
## after n monnths if we begin with 1 pair and in each generation, every pair of reproducttion-age rabbits 
## produces a litter of k rabbit pairs (instead of only 1 pair).



def Rabbit_number( months, offspring):
    parents = 1
    child = 1
    for itr in range(months - 1):
        rabits = parents + (child * offspring)
        child = parents
        parents = rabits
    return child
print(Rabbit_number(31, 5))


def Fibonacci_loop(months, offspring):
    parent, child = 1, 1
    for itrs in range(months - 1):
        child, parent = parent, parent + (child * offspring)
    return child

print(Fibonacci_loop(31, 5)) 