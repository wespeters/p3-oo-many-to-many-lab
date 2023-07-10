class Book:
    all = []
    
    def __init__(self, title):
        self.title = title
        self._contracts = []
        self.__class__.all.append(self)

    def contracts(self):
        return self._contracts
        
    def authors(self):
        return [contract.author for contract in self.contracts()]


class Author:
    all = []
    
    def __init__(self, name):
        self.name = name
        self._contracts = []
        self.__class__.all.append(self)

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Contract:
    all = []
    
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author should be an instance of the Author class.")
        if not isinstance(book, Book):
            raise Exception("Book should be an instance of the Book class.")
        if not isinstance(date, str):
            raise Exception("Date should be a string.")
        if not isinstance(royalties, int):
            raise Exception("Royalties should be an integer.")
            
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.__class__.all.append(self)
        self.author.contracts().append(self)
        self.book.contracts().append(self)

    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all, key=lambda contract: contract.date)
