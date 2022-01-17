# oop
# extending built-ins 

# class ContactList(list['Contact']):
#     def search(self, name: str) -> list['Contact']:

#         matching_contacts: list['Contact'] = []
#         for contact in self:
#             if name in contact.name:
#                 matching_contacts.append(contact)
#         return matching_contacts


# class Contact:
#     # all_contacts: list['Contact'] = []
#     all_contacts = ContactList()

#     def __init__(self, name: str, email: str) -> None:
#         self.name = name
#         self.email = email
#         Contact.all_contacts.append(self)

#     def __repr__(self) -> str:
#         return(
#             f'{self.__class__.__name__}('
#             f'{self.name!r}, {self.email!r}'
#             f')'
#         )


# class AddressHolder:
#     def __init__(self, street: str, city: str, state: str, code: str) -> None:
#         self.street = street
#         self.city = city 
#         self.state = state
#         self.code = code


# class Friend(Contact, AddressHolder):
#     def __init__(
#         self,
#         name: str, 
#         email: str, 
#         phone: str, 
#         street: str, 
#         city: str, 
#         state: str, 
#         code: str) -> None:
#         Contact.__init__(self, name, email)
#         AddressHolder.__init__(self, street, city, state, code)
#         self.phone = phone


class ContactList(list['Contact']):
    def search(self, name: str) -> list['Contact']:

        matching_contacts: list['Contact'] = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


# solving the above diamond inheritance problem
class Contact:
    # all_contacts: list['Contact'] = []
    all_contacts = ContactList()

    def __init__(
        self, 
        /,
        name: str = '' , 
        email: str = '',
        **kwargs: Any) -> None:
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
    def __init__(
        self, 
        /,
        street: str = '', 
        city: str = '', 
        state: str = '', 
        code: str = '') -> None:
        super().__init__(**kwargs) # type: ignore [call-arg]
        self.street = street
        self.city = city 
        self.state = state
        self.code = code


class Friend(Contact, AddressHolder):
    def __init__(
        self,
        /,
        phone: str='', 
        **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.phone = phone
