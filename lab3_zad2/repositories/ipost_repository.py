from abc import ABC, abstractmethod
from typing import List
from domains.post_domain import Post

class IPostRepository(ABC):
    @abstractmethod
    async def fetch_posts(self) -> List[Post]:
        pass