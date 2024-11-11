from typing import List
from domains.post_domain import Post
from repositories.ipost_repository import IPostRepository
from services.ipost_service import IPostService

class PostService(IPostService):
    def __init__(self, repository: IPostRepository):
        self.repository = repository

    async def get_filtered_posts(self, keyword: str) -> List[Post]:
        all_posts = await self.repository.fetch_posts()
        return [post for post in all_posts if keyword.lower() in post.title.lower() or keyword.lower() in post.body.lower()]
