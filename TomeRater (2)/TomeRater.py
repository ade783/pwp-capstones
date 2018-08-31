class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}


    def get_email(self):
        return self.email


    def change_email(self, address):
        self.email = address
        print("Your email has been updated to {email} . " .format(email = self.email))


    def __repr__(self):
        return "You are registered as user: {name}, email: {email}, books_read: {books}.".format \
             (name = self.name, email = self.email, books = len(self.books))


    def __eq__(self, other_user):
        if self.email == other_user.email and self.name == other_user.className
           return True
       else:
           return False

    def read_book(self, book, rating=None):
        self.rating = rating
        self.books[book] = rating

    def get_average_rating(self):
        sum = 0
        number_values = 0
        for key, value in self.books.items():
            number_values += 1
            sum += value
            average = sum / number_values
        return average


class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("ISBN has been updated to: {isbn}".format(isbn=self.isbn))

    def add_rating(self, rating):
        if rating in range(5):
            self.ratings.append(rating)
        else:
            print "Invalid Rating"

    def __eq__(self, other_book):
        if (self.title == other_book.title and self.isbn == other_book.isbn):
            return True
        else:
            return False

    def get_average_rating(self):
        return sum(self.ratings) / len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))




class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title = self.title, author = self.author)


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format\
        (title = self.title, level = self.level, subject = self.subject)


class TomeRater(object):
    def __init__(self):
        self.users = {"fisa_adeniyi@protonmail.com": ade}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
         return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book,email, rating=None):
        if email in self.users.keys():
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book in self.books.keys():
                self.books[book] += 1
            else:
                self.books[book] = 1
            else:
                print("Email not recognised {}".format(email))

    def add_user(self, name, email, books = None):
        self.users[email] = User(name, email)
        if books is not None:
            for book, rating in books.items():
                self.add_book_to_user(book, email, rating)

    def print_catalog(self):
        for key in self.books.keys():
            print(key)

    def print_users(self):
        for value in self.users.values():
            print(value)

    def most_read_book(self):
        return(max(self.books, key=self.books.get))

    def highest_rated_book(self):
        average_ratings_books = {}
        for book in self.books:
            average_ratings_books[book] = book.get_average_rating()
        print(max(average_ratings_books, key = average_ratings_books.get))

    def most_positive_user(self):
        average_ratings_user = {}
        for user in self.users.values():
            average_ratings_user[user] = user.get_average_rating()
        print(max(average_ratings_user, key = average_ratings_user.get))
