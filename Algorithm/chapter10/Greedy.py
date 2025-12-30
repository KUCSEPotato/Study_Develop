# Greedy Algorithms
# Examples

# Declration of states
states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

# Declration of stations
# Key is station name, value is set of states covered by that station
stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

# stations selected
final_stations = set()

def main():
    global states_needed, final_stations
    
    # greedy algorithm
    while states_needed:
        # best choice at each step
        best_station = None
        states_covered = set() # 아직 방송되지 않은 주 중에서 해당 방송국이 커버하는 주의 집합

        for station, states_for_station in stations.items():
            covered = states_needed & states_for_station # intersection, 아직 방송되지 않은 주 중에서 해당 방송국이 커버하는 주의 집합
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
        
        final_stations.add(best_station)
        states_needed -= states_covered # remove covered states from states_needed

if __name__ == "__main__":
    main()
    print("Selected stations:", final_stations)