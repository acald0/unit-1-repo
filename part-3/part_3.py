my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def formating_book(dictionary):
    printable = f"The author {dictionary["author"]} wrote {dictionary["title"]} in {dictionary["year"]}. {dictionary["title"]} has {dictionary["pages"]} pages and a {dictionary["rating"]} rating."
    return printable

print(formating_book(my_book))

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def print_title(dictionary):
    return dictionary["title"]

def print_author(dictionary):
    return dictionary["author"]

def print_year(dictionary):
    return dictionary["year"]

def print_rating(dictionary):
    return dictionary["rating"]

def print_pages(dictionary):
    return dictionary["pages"]

print(print_title(my_book))
print(print_author(my_book))
print(print_year(my_book))
print(print_rating(my_book))
print(print_pages(my_book))

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

book_library = [
    {"title": "1984",
     "author": "George Orwell",
     "pages": 328},
     {"title": "Fahrenheit 451",
     "author": "Ray Bradbury",
     "pages": 158},
     {"title": "To Kill a Mockingbird",
     "author": "Harper Lee",
     "pages": 384}
]

def all_titles(library_list):
    titles = []
    index = 0
    while index < len(library_list):
        titles.append(library_list[index]["title"])
        index += 1
    return titles

print(all_titles(book_library))

def pages_sum(library_list):
        pages = 0
        index = 0
        while index < len(library_list):
            pages += library_list[index]["pages"]
            index += 1
        return pages

print(pages_sum(book_library))

def change_pages(pages, index, library_list):
    library_list[index]["pages"] = pages
    return library_list

print(change_pages(400, 2, book_library))