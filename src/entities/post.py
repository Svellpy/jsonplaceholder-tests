from typing import Any, Dict
from dataclasses import dataclass
import json

@dataclass
class Post:
    userId: int
    id: int
    title: str
    body: str

    @staticmethod
    def from_dict(obj: Any) -> "Post":
        _userId = int(obj.get("userId"))
        _id = int(obj.get("id"))
        _title = str(obj.get("title"))
        _body = str(obj.get("body"))
        return Post(_userId, _id, _title, _body)
    
    @staticmethod
    def from_json(json_string: str) -> "Post":
        obj = json.loads(json_string)
        return Post.from_dict(obj)
    
    def to_dict(self) -> Dict[str, Any]:
        return{
            "userId": self.userId,
            "id": self.id,
            "title": self.title,
            "body": self.body,
        }
    
    def to_json(self) -> str:
        return json.dumps(self.to_dict())