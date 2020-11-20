from thinkbayes import Pmf

# Distribution of outcomes by rolling a six sided die
pmf = Pmf()

for x in [1, 2, 3, 4, 5, 6]:
    pmf.Set(x, 1/6.0) # Set value of each probability to 1/6