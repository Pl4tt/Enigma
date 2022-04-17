
class Message:
    def __init__(self, header: dict[str, str | list[str]], text: str) -> None:
        self.header = header
        self.text = text