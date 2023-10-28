class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        try:
            self.phones.append(Phone(phone))
        except ValueError as e:
            return str(e)

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return f"Phone {phone} removed"
        return f"Phone {phone} not found"

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                try:
                    p.value = new_phone
                    return f"Phone {old_phone} edited to {new_phone}"
                except ValueError as e:
                    return str(e)
        return f"Phone {old_phone} not found"

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return f"Phone {phone} not found"

    def __str__(self):
        phone_str = "; ".join(str(p) for p in self.phones)
        return f"Contact name: {self.name}, phones: {phone_str}"

class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]
        return f"Record {name} not found"

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return f"Record {name} deleted"
        return f"Record {name} not found"

if __name__ == "__main__":
    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    for name, record in book.data.items():
        print(record)

    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")
    print(john)

    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")

    result = book.delete("Jane")
    print(result)
