from bird import Bird

class Eagle(Bird):
    def __init__(self, initial_feather_count) -> None:
        super().__init__()
        self.__current_location = ""
        self.__number_of_feathers = initial_feather_count

    def fly(self):
        self.__current_location = "in the air"

    def molt(self):
        self.__number_of_feathers -= -1
