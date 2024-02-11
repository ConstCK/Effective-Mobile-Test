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
        return (organization.istitle() and
                len(organization) > 1)

    @classmethod
    def phone_validation(cls, phone: str) -> bool:
        return (len(phone) > 10 and
                phone.startswith("+") and
                phone[1:].isdigit())
