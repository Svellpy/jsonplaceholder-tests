from typing import Any, Dict
from dataclasses import dataclass
import json

@dataclass
class Comment:
    postId: int
    id: int
    name: str
    email: str
    body: str

    @staticmethod
    def from_dict(obj: Any) -> "Comment":
        _postId = int(obj.get("postId"))
        _id = int(obj.get("id"))
        _name = str(obj.get("name"))
        _email = str(obj.get("email"))
        _body = str(obj.get("body"))
        return Comment(_postId, _id, _name, _email, _body)
    