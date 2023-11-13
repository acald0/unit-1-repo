### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here
# with open("library.txt", "w") as f:
#     f.write("title, author, year, rating, pages\n")

with open("library.txt", "a") as f:
    f.write("Pride and Prejudice, Jane Austen, 1813, 4.8, 273\n")

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here
with open("library.txt", "r") as f:
    file = f.readlines()

    for line in file:
        title, author, year, rating, pages = line.split(',')

        book_dictionary = {
            "title": title,
            "author": author,
            "year": int(year),
            "rating": float(rating),
            "pages": int(pages)
        }

    print(book_dictionary)
### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

def formating_book(dictionary_list):
    info = ''
    index = 0
    while index < len(dictionary_list):
        printable = f"The author {dictionary_list[index]["author"]} wrote {dictionary_list[index]["title"]} in {dictionary_list[index]["year"]}. {dictionary_list[index]["title"]} has {dictionary_list[index]["pages"]} pages and a {dictionary_list[index]["rating"]}/5 rating.  \n \n"
        info += printable
        index += 1
    return info

def new_book():
    title = input("The title of the book: ")
    author = input("The author of the book: ")
    try:
        year = int(input("The year the book was published: "))
    except:
        year = int(input("Enter a number for the year: "))
    try:
        rating = float(input("The rating of the book: "))
    except:
        rating = float(input("Enter a number for the rating: "))
    try:
        pages = int(input("Total pages in the book: "))
    except:
        pages = int(input("Enter a number for the pages: "))


    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    # book_library.append(book_dictionary)
    return book_dictionary

def all_titles(library_list):
    titles = []
    index = 0
    while index < len(library_list):
        titles.append(library_list[index]["title"])
        index += 1
    return titles



def pages_sum(library_list):
        pages = 0
        index = 0
        while index < len(library_list):
            pages += library_list[index]["pages"]
            index += 1
        return pages




def main_menu(book_library):
    condition = input("Would you like to interact with the library? (Y/N) ")
    while condition == "Y" or condition == "y":
        try:
            choice = int(input("Enter 1 to view your library, enter 2 to add a new book, enter 3 to view all titles in library, enter 4 to get a total pages of library, enter 5 to quit the application: "))
        except:
            choice = int(input("Enter a number to choose an option: "))
        if choice == 1:
            print(formating_book(book_library))
        elif choice == 2:
            print(new_book())
        elif choice == 3:
            print(all_titles(book_library))
        elif choice == 4:
            print(pages_sum(book_library))
        elif choice == 5:
            break
        else:
            print("Invalid choice")
    else:
        print("Application terminated.")
    condition


if __name__ == "__main__":
    main_menu(book_dictionary)