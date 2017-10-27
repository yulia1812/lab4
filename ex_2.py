#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = ['a', 'A', 'b', 'B']

# Реализация задания 2
print(' '.join(map(str, Unique(data1))), ' '.join(map(str, Unique(data2))), ' '.join(Unique(data3, ignore_case=True)))
# **kwargs = {'ignore_case':True}