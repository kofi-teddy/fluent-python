def tower_of_hanoi(n: int, A: str, B: str, C: str) -> None:
    if n == 1:
        print(f"Move disk 1 from {A} to {C}")
        return
    
    # move n-1 disk from A to B using C as auxiliary
    tower_of_hanoi(n-1, A, C, B)
    print(f"Move disk {n} from {A} to {C}") 

    # move disk n-1 from B to C using A
    tower_of_hanoi(n-1, B, A, C)


tower_of_hanoi(3, 'A', 'B', 'C')


