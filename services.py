class InputValidator:
    def __init__(self) -> None:
        pass

    @classmethod
    def name_validation(cls, name: str) -> bool:
        return (name.isalpha() and
                name.istitle() and
                len(name) > 1)

    @classmethod
    def organization_validation(cls, organization: str) -> bool:
        return len(organization) > 1

    @classmethod
    def phone_validation(cls, phone: str) -> bool:
        return (len(phone) > 10 and
                phone.startswith("+") and
                phone[1:].isdigit())


class BookPaginator:
    def __init__(self) -> None:
        pass

    @staticmethod
    def paginate_data(data: list[str], size: int = 2):
        start: int = 0
        while start < len(data):
            yield data[start:size + start]
            start += size

