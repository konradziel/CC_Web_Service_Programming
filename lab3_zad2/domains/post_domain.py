from dataclasses import dataclass, field
from typing import List
from domains.comment_domain import Comment

@dataclass
class Post:
    userId: int
    id: int
    title: str
    body: str
    comments: List['Comment'] = field(default_factory=list)