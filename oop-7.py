# OOP
# Inheritance
# overriding and super
from __future__ import annotations
from pprint import pprint


class Emailable():
    email: str


class MailSender(Emailable):
    def send_mail(self, message: str) -> None:
        print(f'Sending mail to {self.email=}')  
        # add email logic here


class ContactList(list['Contact']):
    def search(self, name: str) -> list['Contact']:

        matching_contacts: list['Contact'] = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


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


class Supplier(Contact):
    def order(self, order: 'Order') -> None:
        print(
            'if this were a real system we would send'
            f'{order} order to {self.name}'
        )


class Friend(Contact):
    def __init__(self, name: str, email: str, phone: str) -> None:
        super().__init__(name, email)
        self.phone = phone


class EmailableContact(Contact, MailSender):
    pass


# c_1 = Contact('kofi', 'kofi@skycrew.tech')
# s_1 = Supplier('louis', 'louis@skycrew.tech')
# print(c_1.name, c_1.email, s_1.name, s_1.email)

# pprint(c_1.all_contacts)

# c_1.order('I need pliers')

# s_1.order('I need pliers')

# print(Contact.all_contacts)

# c1 = Contact('Kofi T', 'kofi@skycrew.tech')
# c1 = Contact('Kofi A', 'Fii@skycrew.tech')
# c2 = Contact('Louis A', 'lous@skycrew.tech')
# c3 = Contact('Sefaah O', 'sefaah@skycrew.tech')
# # print([c.name for c in Contact.all_contacts.search('Kofi')])

# # print([] == list())

# f = Friend('Selorm A', 'selorm@skycrew.tech', '023000000')
# print(Contact.all_contacts)

e = EmailableContact('Kofi T', 'kofi@skycrew.tech')
print(Contact.all_contacts)

print(e.send_mail('Hello, test e-mail here'))