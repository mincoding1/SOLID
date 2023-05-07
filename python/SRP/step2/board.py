class Board:
    def __init__(self) -> None:
        super().__init__()
        self.spots = []
        for i in range(9):
            self.spots.append(str(i))

    def get_first_row(self) -> []:
        first_row = []
        first_row.append(self.spots[0])
        first_row.append(self.spots[1])
        first_row.append(self.spots[2])
        return first_row

    def get_second_row(self) -> []:
        second_row = []
        second_row.append(self.spots[3])
        second_row.append(self.spots[4])
        second_row.append(self.spots[5])
        return second_row

    def get_third_row(self) -> []:
        third_row = []
        third_row.append(self.spots[6])
        third_row.append(self.spots[7])
        third_row.append(self.spots[8])
        return third_row

    def display(self):
        formatted_first_row = self.spots[0] + "|" + self.spots[1] + "|" + self.spots[2] + "\n" + self.spots[3] + "|" + self.spots[4] + "|" + self.spots[5] + "\n" + self.spots[6] + "|" + self.spots[7] + "|" + self.spots[8] + "\n"
        print(formatted_first_row)
