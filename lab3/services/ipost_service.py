from abc import ABC, abstractmethod
from typing import List
from domains.post_domain import Post

class IPostService(ABC):
    @abstractmethod
    async def get_filtered_posts(self, keyword: str) -> List[Post]:
        pass
