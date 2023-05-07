class Board:
    def __init__(self) -> None:
        super().__init__()
        self.__spots = []
        for i in range(9):
            self.__spots.append(str(i))

    def get_first_row(self) -> []:
        first_row = []
        first_row.append(self.__spots[0])
        first_row.append(self.__spots[1])
        first_row.append(self.__spots[2])
        return first_row

    def get_second_row(self) -> []:
        second_row = []
        second_row.append(self.__spots[3])
        second_row.append(self.__spots[4])
        second_row.append(self.__spots[5])
        return second_row

    def get_third_row(self) -> []:
        third_row = []
        third_row.append(self.__spots[6])
        third_row.append(self.__spots[7])
        third_row.append(self.__spots[8])
        return third_row

    def display(self):
        formatted_first_row = self.__spots[0] + "|" + self.__spots[1] + "|" + self.__spots[2] + "\n" + self.__spots[3] + "|" + self.__spots[4] + "|" + self.__spots[5] + "\n" + self.__spots[6] + "|" + self.__spots[7] + "|" + self.__spots[8] + "\n"
        print(formatted_first_row)
