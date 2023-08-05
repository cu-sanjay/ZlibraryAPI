# ZlibraryAPI - Python Wrapper for Zlibrary API

![Python Version](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**ZlibraryAPI** is a Python wrapper for the Zlibrary API, which allows you to interact with the Zlibrary service programmatically. With this library, you can perform various actions, such as searching for books, getting book details, downloading books, and more.

## Installation

You can install ZlibraryAPI using pip:
  ```python
  pip install zlibraryapi
  ```
## Usage

Before using the ZlibraryAPI, you need to obtain an API key from Zlibrary. Once you have the API key, you can use the library to access the Zlibrary API.

  ```python
  from zlibraryapi import ZlibraryAPI
  
  # Replace 'YOUR_API_KEY' with your actual API key
  api = ZlibraryAPI(api_key='YOUR_API_KEY')
  
  # Example: Search for books
  results = api.search_books('Python Programming', order='newest', limit=5)
  
  for book in results.get('books', []):
      print(f"Title: {book['title']}, Author: {book['author']}")
  ```

## Available Methods

Here are some of the methods available in the ZlibraryAPI:

- login(email, password): Log in to Zlibrary with your account credentials.
- get_user_info(): Get user information.
- get_most_popular_books(switch_language=None): Get a list of most popular books.
- get_recent_books(): Get a list of recently added books.
- get_user_recommended_books(): Get a list of user-recommended books.
- get_book_formats(book_id, hash_id): Get available formats for a specific book.
- search_books(query, order=None, page=None, limit=None): Search for books based on a query.
- download_book(book_id, hash_id, format_): Download a specific book in the desired format.

Please refer to the [documentation](https://api.zlibraryexau2g3eg.onion/docs) of the Zlibrary API for more details on available endpoints and parameters.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to the Zlibrary team for providing the API and making it accessible to developers.

## Links

- [Zlibrary Website](https://z-lib.org/)
- [Zlibrary API Documentation](https://api.zlibraryexau2g3eg.onion/docs)

## Support

If you need any help or have any questions, please [open an issue](https://github.com/cu-sanjay/zlibraryapi/issues) on GitHub.
