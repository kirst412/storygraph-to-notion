from storygraph_api import User, Book
from dotenv import load_dotenv
import os

def get_book_details(book_id, cookie):
    book = Book()
    result = book.book_info(book_id, cookie=cookie)
    print(result)
    print(type(result))
    return result

def main():
    load_dotenv()

    cookie = os.getenv("COOKIE")
    uname = os.getenv('STORY_USERNAME')
    user = User()
    result = eval(user.currently_reading(uname,cookie=cookie))
    print(result)
    """
    result looks like this, need to use eval to make sure it's a list of dictionaries:
    [
        {
            "title": "Onyx Storm",
            "book_id": "687a5a4d-4233-4edd-af78-bfd633d21040"
        },
        {
            "title": "Designing Machine Learning Systems: An Iterative Process for Production-Ready Applications",
            "book_id": "9ab88a45-b8a2-4974-95e4-18edac16b64c"
        }
    ]
    """
    details = []
    for book in result:
        print(book)
        details.append(get_book_details(book['book_id'], cookie))
    print(details)

if __name__ == '__main__':
    main()
