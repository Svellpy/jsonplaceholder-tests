from typing import Optional, Dict, Any
import httpx

class BaseClient:

    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.Client(timeout=30.0)
        self.client.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })

    def get(self, endpoint: str, params: Optional[Dict] = None) -> httpx.Response:
        url = f"{self.base_url}{endpoint}"
        return self.client.get(url,params=params)
    
    def post(self, endpoint: str, data: Optional[Dict] = None) -> httpx.Response:
        url = f"{self.base_url}{endpoint}"
        return self.client.post(url, json=data)
    
    def put(self, endpoint: str, data: Optional[Dict] = None) -> httpx.Response:
        url = f"{self.base_url}{endpoint}"
        return self.client.put(url, json=data)
    
    def patch(self, endpoint: str, data: Optional[Dict] = None) -> httpx.Response:
        url = f"{self.base_url}{endpoint}"
        return self.client.patch(url, json=data)
    
    def delete(self, endpoint: str) -> httpx.Response:
        url = f"{self.base_url}{endpoint}"
        return self.client.delete(url)
    
    def close(self):
        self.client.close()
