from abc import ABC, abstractmethod
from typing import List
from domains.comment_domain import Comment
from domains.post_domain import Post

class ICommentService(ABC):
    @abstractmethod
    async def assing_comments_to_posts(self, all_posts: List[Post]):
        pass
