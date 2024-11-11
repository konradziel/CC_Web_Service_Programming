from abc import ABC, abstractmethod
from typing import List
from domains.post_domain import Post

class IPostService(ABC):
    @abstractmethod
    def filter_posts(self, keyword: str, all_posts: List[Post]) -> List[Post]:
        pass
