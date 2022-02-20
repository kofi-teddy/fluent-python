# contacts model


class Address:
    def __init__(self, street, city, state, zipcode, street2=''):
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city}, {self.state} {self.zipcode}')
        return '\n'.join(lines)


class AddressBook:
    def __init__(self):
        self._employee_addresses = {
            1: Address('Comm. 2 Alang', 'Aggrey road', 'Tema', '2244'),
            2: Address('Comm. 10', 'May flour Area', 'C10', '2244'),
            3: Address('East Legon', 'Ahodwo Area', 'Accra', '2244'),
            4: Address('Lebanon', 'Ashaiman', 'Tema', '2244'),
            5: Address('Comm. 7', 'Biggies Area', 'Tema', '2244'),
        }
    
    def get_employee_address(self, employee_id):
        address = self._employee_addresses.get(employee_id)
        if not address:
            raise ValueError(employee_id)
        return  address
