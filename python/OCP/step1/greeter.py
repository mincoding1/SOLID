class Greeter:
    def __init__(self) -> None:
        super().__init__()
        self.formality = "normal"

    def greet(self) -> str:
        if self.formality == "formal":
            return "Good evening, sir."
        elif self.formality == "casual":
            return "Sup bro?"
        elif self.formality == "intimate":
            return "Hello Darling!"
        else:
            return "Hello."

    def set_formality(self, formality:str):
        self.formality = formality
