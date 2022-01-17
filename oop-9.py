# oop
# extending built-ins 


class Contact:
    # all_contacts: list['Contact'] = []
    all_contacts = ContactList()

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self) -> str:
        return(
            f'{self.__class__.__name__}('
            f'{self.name!r}, {self.email!r}'
            f')'
        )


class AddressHolder:
    def __init__(self, street: str, city: str, state: str, code: str) -> None:
        self.street = street
        self.city = city 
        self.state = state
        self.code = code


class Friend(Contact, AddressHolder):
    def __init__(
        self,
        name: str, 
        email: str, 
        phone: str, 
        street: str, 
        city: str, 
        state: str, 
        code: str) -> None:
        Contact.__init__(self, name, email)
        AddressHolder.__init__(self, street, city, state, code)
        self.phone = phone
