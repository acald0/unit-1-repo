### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here

# def new_book():
#     title = input("The title of the book: ")
#     author = input("The author of the book: ")
#     year = input("The year the book was published: ")
#     rating = input("The rating of the book: ")
#     pages = input("Total pages in the book: ")

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return book_dictionary

# print(new_book())

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here
# def new_book():
#     title = input("The title of the book: ")
#     author = input("The author of the book: ")
#     year = int(input("The year the book was published: "))
#     rating = float(input("The rating of the book: "))
#     pages = int(input("Total pages in the book: "))
#     # print(type(year))
#     # print(type(rating))
#     # print(type(pages))

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return book_dictionary

# print(new_book())


### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here
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

    return book_dictionary

print(new_book())



### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here


### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

