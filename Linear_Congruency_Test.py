#--------------------------------Imported Functions--------------------------------------#
from Linear_Congruency import zero_or_one
from Linear_Congruency import linear_congruency

#--------------------------------Seed Data--------------------------------------#
import random
initial_seed = random.randint(1,2**31) #Creates a random number that ranges between 1 and 2**31

#--------------------------------Seed Data--------------------------------------#
x = lc.linear_congruency(initial_seed)
#print(x)
choice = lc.zero_or_one(x)