def traveling_salesperson_prob(cities, distances):
    """
    Solve the Traveling Salesperson Problem using a brute-force approach.
    
    param cities: List of cities to visit.
    param distances: A dictionary where keys are tuples of city pairs and values are distances between them.
    return: The shortest path and its distance.
    """
    from itertools import permutations

    min_distance = float('inf')
    best_path = None

    # 모든 순열 탐색
    for perm in permutations(cities):
        current_distance = 0
        
        # 연속된 도시 간 거리 합산
        for i in range(len(perm) - 1):
            current_distance += distances[(perm[i], perm[i+1])]
        
        # 마지막 도시에서 출발 도시로 돌아오는 거리까지 포함하려면:
        current_distance += distances[(perm[-1], perm[0])]

        # 최소 거리 갱신
        if current_distance < min_distance:
            min_distance = current_distance
            best_path = perm

    return best_path, min_distance

def main():
    # Example usage of traveling_salesperson_prob function
    cities = ['A', 'B', 'C']
    distances = {
        ('A', 'B'): 10,
        ('A', 'C'): 15,
        ('B', 'C'): 20,
        ('B', 'A'): 10,
        ('C', 'A'): 15,
        ('C', 'B'): 20
    }
    
    best_path, min_distance = traveling_salesperson_prob(cities, distances)
    
    print(f"Best path: {best_path} with distance: {min_distance}")

if __name__ == "__main__":
    main()