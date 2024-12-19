# Advent Of Code: https://adventofcode.com/2024/day/1


class PuzzleOneMain:
    def get_distance(self, left_list: list, right_list: list) -> int:
        # get the smallest number in each list
        smallest_left = min(left_list)
        smallest_right = min(right_list)

        """
        Conditionally obtain the distance between the two
        numbers based off which number is the smaller of the
        two. This is going to look confusing but it is setup
        to be like:

        if left is smaller than right
            subtract left from right
        else
            subtract right from left

        in otherwords, figure out which number is the smaller
        of the two and rearrange the formula so that you subtract
        the bigger number from the smaller number to negate obtaining
        a negative number
        """

        if smallest_left <= smallest_right:
            distance = smallest_right - smallest_left
        else:
            distance = smallest_left - smallest_right

        left_list.remove(smallest_left)
        right_list.remove(smallest_right)

        return distance

    def get_total_distance(self):
        # create a variable to hold the total distances
        total_distances = 0

        # separate the text file's puzzle data into two lists
        left, right = self.get_left_right_list()

        # iterate the lists
        while left and right:
            distance = self.get_distance(left, right)

            total_distances += distance

        return total_distances

    def get_left_right_list(self) -> list:
        left_list = []
        right_list = []

        with open("./puzzle_input.txt", 'r') as file:
            for line in file:
                parts = line.strip().split('   ')

                if len(parts) == 2:
                    left_list.append(int(parts[0]))
                    right_list.append(int(parts[1]))

        return [left_list, right_list]


if __name__ == '__main__':
    main = PuzzleOneMain()
    
    total_distance = main.get_total_distance()
    print(total_distance)
