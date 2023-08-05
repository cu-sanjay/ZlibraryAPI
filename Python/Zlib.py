import requests
from typing import Union, Dict

class ZlibraryAPI:
    def __init__(self, api_key: str = None):
        self.__domain = "https://api.zlibraryexau2g3eg.onion"
        self.__headers = {
            'Authorization': f'Bearer {api_key}' if api_key else None,
            'accept': 'application/json',
            'user-agent': 'ZlibraryAPI/1.0',
        }
        self.__logged = bool(api_key)

    def login(self, email: str, password: str) -> Dict[str, str]:
        response = self.__makePostRequest('/user/login', data={
            "email": email,
            "password": password,
        })
        self.__logged = response.get('success', False)
        return response

    def get_user_info(self) -> Dict[str, str]:
        return self.__makeGetRequest('/user/profile')

    def get_most_popular_books(self, switch_language: str = None) -> Dict[str, str]:
        params = {"switch-language": switch_language} if switch_language else {}
        return self.__makeGetRequest('/book/most-popular', params=params)

    def get_recent_books(self) -> Dict[str, str]:
        return self.__makeGetRequest('/book/recently')

    def get_user_recommended_books(self) -> Dict[str, str]:
        return self.__makeGetRequest('/user/book/recommended')

    def get_book_formats(self, book_id: Union[int, str], hash_id: str) -> Dict[str, str]:
        return self.__makeGetRequest(f'/book/{book_id}/{hash_id}/formats')

    def search_books(self, query: str, order: str = None, page: int = None, limit: int = None) -> Dict[str, str]:
        params = {k: v for k, v in {"query": query, "order": order, "page": page, "limit": limit}.items() if v is not None}
        return self.__makeGetRequest('/book/search', params=params)

    def download_book(self, book_id: Union[int, str], hash_id: str, format_: str) -> bytes:
        url = f'/book/{book_id}/{hash_id}/{format_}/file'
        response = requests.get(self.__domain + url, headers=self.__headers)
        if response.status_code == 200:
            return response.content
        else:
            print("Failed to download book.")
            return None

    def __makePostRequest(self, url: str, data: dict = None) -> Dict[str, str]:
        response = requests.post(
            self.__domain + url,
            json=data,
            headers=self.__headers,
        ).json()
        if not response.get('success', False):
            print(response.get('error'))
        return response

    def __makeGetRequest(self, url: str, params: dict = None) -> Dict[str, str]:
        response = requests.get(
            self.__domain + url,
            params=params,
            headers=self.__headers,
        ).json()
        if not response.get('success', False):
            print(response.get('error'))
        return response
