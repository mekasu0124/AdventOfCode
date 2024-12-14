def get_left_right_list() -> list:
    left_list = []
    right_list = []

    with open("./puzzle_input.txt", 'r') as file:
        for line in file:
            parts = line.strip().split('   ')

            if len(parts) == 2:
                left_list.append(int(parts[0]))
                right_list.append(int(parts[1]))

    return [left_list, right_list]

def get_total_simularity(list_a: list, list_b: list):
    total_simularity = 0

    for value in list_a:
        total_occurances = list_b.count(value)
        simularity = value * total_occurances
        total_simularity += simularity

    return total_simularity

left, right = get_left_right_list()

total_simularity = get_total_simularity(left, right)

print(f"Total Simularities: {total_simularity}")
