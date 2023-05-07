class Greeter:
    def __init__(self) -> None:
        super().__init__()
        self.__formality = "normal"

    def greet(self) -> str:
        if self.__formality == "formal":
            return "Good evening, sir."
        elif self.__formality == "casual":
            return "Sup bro?"
        elif self.__formality == "intimate":
            return "Hello Darling!"
        else:
            return "Hello."

    def set_formality(self, formality: str):
        self.__formality = formality
