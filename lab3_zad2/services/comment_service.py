from typing import List
from domains.comment_domain import Comment
from domains.post_domain import Post
from repositories.icomment_repository import ICommentRepository
from repositories.ipost_repository import IPostRepository
from services.icomment_service import ICommentService

class CommentService(ICommentService):
    def __init__(self, comment_repository: ICommentRepository, post_repository: IPostRepository):
        self.comment_repository = comment_repository
        self.post_repository = post_repository

    async def assing_comments_to_posts(self, all_posts: List[Post]):
        all_comments = await self.comment_repository.fetch_comments()
        for comment in all_comments:
            for post in all_posts:
                if post.id == comment.postId:
                    post.comments.append(comment)
