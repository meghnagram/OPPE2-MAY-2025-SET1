def get_short_books(book_data:list) -> set:
    """Returns the list of ISBNs of the books with pages less than 200."""
    
    
    return {isbn for isbn, pages, _, _ in book_data if pages < 200}
    

def get_medium_books(book_data:list) -> set:
    """Returns the list of isbns of the books with pages Between 200 and 500(inclusive)."""
    
    
    return {isbn for isbn, pages, *_ in book_data if 200 <= pages <= 500}
    

def get_pages_by_isbn(book_data:list, isbn: str) -> int:
    """Returns the number of pages in the book given the ISBN."""
    
    
    return next((pages for book_isbn, pages, *_ in book_data if isbn == book_isbn), None)
    

def count_by_language(book_data:list) -> dict:
    """Returns a dict with the languages as keys and the number of books of that language as values."""
    
    
    counts = {}
    for book in book_data:
        lang = book[2]
        if lang not in counts:
            counts[lang] = 0
        counts[lang] += 1 
    return counts
    

def total_pages_in_genre_lang(book_data:list, genre:str, lang:str) -> int:
    """Returns the total number of pages from all the books with the given genre and language."""
    
    
    return sum(pages for _,pages, book_lang, book_genre in book_data if book_genre == genre  and book_lang == lang)

# #aNOTHER mETHOD:

# def get_short_books(book_data:list) -> set:
#     """Returns the list of ISBNs of the books with pages less than 200."""
#     l=[]
#     for i in book_data:
#         if i[1]<200:
#             l.append(i[0])
#     return set(l)
    

# def get_medium_books(book_data:list) -> set:
#     """Returns the list of isbns of the books with pages Between 200 and 500(inclusive)."""
#     l=[]
#     for i in book_data:
#         if 200<=i[1]<=500:
#             l.append(i[0])
#     return set(l)
    

# def get_pages_by_isbn(book_data:list, isbn: str) -> int:
#     """Returns the number of pages in the book given the ISBN."""
#     for v in book_data:
#         if isbn==v[0]:
#             return v[1]
#     return None
    

# def count_by_language(book_data:list) -> dict:
#     """Returns a dict with the languages as keys and the number of books of that language as values."""
#     d={}
#     for i in book_data:
#         d[i[2]]=0 
#     sum=0 
#     for k in d.keys():
#         for i in book_data:
#             if k == i[2]:
#                 sum +=1
#         d[k]=sum
#         sum=0 
#     return d
    
        
    

# def total_pages_in_genre_lang(book_data:list, genre:str, lang:str) -> int:
#     """Returns the total number of pages from all the books with the given genre and language."""
#     sum=0 
#     for i in book_data:
#         if i[2]==lang:
#             if i[3]==genre:
#                 sum +=i[1]
#     return sum
                

# Book Data Analysis
# Given a list of tuples (isbn: str, pages: int, language: str, genre: str), implement the following functions:

# get_short_books: Fewer than 200 pages
# get_medium_books: Between 200 and 500 pages inclusive
# get_pages_by_isbn: Extract the number of pages in the particular ISBN. Returns None if does not exists.
# count_by_language: Get the counts of books by language as a dict with language as keys and number of books in that language as values.
# total_pages_in_genre_lang: The total number of pages from all the books in the particular genre and language.
# NOTE: This is a function-type question. You do not have to take input or print the output. Just complete the required function. You may define helper functions inside the main function if needed.

# Examples

# >>> books_data = [
#     ("978-3-16-148410-0", 150, "English", "Thriller"),
#     ("978-0-14-103620-2", 450, "Tamil", "Fantasy"),
#     ("978-1-4028-9467-2", 200, "English", "Fiction"),
#     ("978-0-393-04002-2", 350, "Hindi", "History"),
#     ("978-0-06-112008-4", 300, "English", "Fiction"),
#     ("978-1-60413-970-0", 175, "Bengali", "Mystery"),
#     ("978-0-7432-7356-5", 420, "English", "Science Fiction"),
#     ("978-1-56619-909-4", 100, "Tamil", "Romance"),
#     ("978-1-4088-4994-7", 270, "Telugu", "Biography"),
#     ("978-0-374-53243-2", 540, "English", "Thriller")
#     ]

# >>> get_short_books(books_data)
# {'978-3-16-148410-0', '978-1-60413-970-0', '978-1-56619-909-4'}
# >>> get_medium_books(book_data)
# {'978-0-14-103620-2', '978-1-4028-9467-2', '978-0-393-04002-2', '978-0-06-112008-4', '978-1-4088-4994-7', '978-0-7432-7356-5'}
# >>> get_pages_by_isbn(book_data, "978-0-7432-7356-5")
# 420
# >>> count_by_language(book_data)
# {
#     "English": 5,
#     "Tamil": 2,
#     "Hindi": 1,
#     "Bengali": 1,
#     "Telugu": 1,
# }
# >>> total_pages_in_genre_lang(book_data, 'Fiction', 'English')
# 500
    
