from typing import List
from domains.post_domain import Post
from repositories.ipost_repository import IPostRepository
from repositories.comment_repository import ICommentRepository
from services.ipost_service import IPostService

class PostService(IPostService):
    def __init__(self, repository: IPostRepository):
        self.repository = repository

    async def get_all_posts(self) -> List[Post]:
        all_posts = await self.repository.fetch_posts()
        return all_posts

    def filter_posts(self, keyword: str, all_posts: List[Post]) -> List[Post]:
        keyword = keyword.lower()
        filtered_posts = []

        for post in all_posts:
            if (keyword in post.title.lower() or
                    keyword in post.body.lower() or
                    any(keyword in comment.body.lower() for comment in post.comments)):
                filtered_posts.append(post)
        
        return filtered_posts