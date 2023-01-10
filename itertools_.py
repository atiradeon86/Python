import itertools as it
import time

ind_chars = "\|/-"

indicator = it.cycle(ind_chars)

for _ in range(100):
    print(next(indicator), end='\r')
    time.sleep(0.1)



people = ('Peter', 'Julia', 'Andrew', 'Bobby','‘Margo', 'Bill', 'Alice', 'Anna')

def shift_maker(people_iterable, num_of_shifts):
    peope_per_shift = len(people_iterable) / num_of_shifts
    return it.combinations(people_iterable, int(peope_per_shift))

print(list(shift_maker(people, 3)))