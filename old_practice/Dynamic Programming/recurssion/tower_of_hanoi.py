def tower_of_hanoi(num_of_discs:int, from_rod:int, helper_rod: int, to_rod:int):
    if num_of_discs==0:
        return
    tower_of_hanoi(num_of_discs-1, from_rod, to_rod, helper_rod)
    print(f"{from_rod}->{to_rod}")
    tower_of_hanoi(num_of_discs-1, helper_rod, from_rod, to_rod)


print(tower_of_hanoi(2,'A','B','C'))