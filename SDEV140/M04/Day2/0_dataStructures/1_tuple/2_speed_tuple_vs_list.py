import time

rang = range(31526536)
example_tuple = tuple(rang)
example_list = list(rang)


t_start = time.time()
print(example_list[315265])
t_end = time.time()

print(f"List time:  {(t_end - t_start):.20f}")


t_start = time.time()
print(example_tuple[315265])
t_end = time.time()

print(f"Tuple time: {(t_end - t_start):.20f}")


