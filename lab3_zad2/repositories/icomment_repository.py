from abc import ABC, abstractmethod
from typing import List
from domains.comment_domain import Comment

class ICommentRepository(ABC):
    @abstractmethod
    async def fetch_comments(self) -> List[Comment]:
        pass