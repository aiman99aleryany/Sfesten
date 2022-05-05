# !python3 - attempt1
"""
This module will focus on part OOA 1-1 which is (identify the type of information) for now it will only be for vcard
"""


class VcardFields(object):
    """assuming that we choose a vcard to convert into a qrcode these will be the initials data"""
    # TODO: create an optional argument to take optional input if there more information to provide for the vcard
    def __init__(self, name='', lastname='', title='', phone_number='', phone_number2='',
                 fax='', email='', address='', website=''):
        self.name = name
        self.lastname = lastname
        self.title = title
        self.phone_number = phone_number
        self.phone_number2 = phone_number2
        self.fax = fax
        self.email = email
        self.address = address
        self.website = website

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_lastname(self, lastname):
        self.lastname = lastname

    def get_lastname(self):
        return self.lastname

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number2(self, phone_number2):
        self.phone_number2 = phone_number2

    def get_phone_number2(self):
        return self.phone_number2

    def set_fax(self, fax):
        self.fax = fax

    def get_fax(self):
        return self.fax

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def set_website(self, website):
        self.website = website

    def get_website(self):
        return self.website

