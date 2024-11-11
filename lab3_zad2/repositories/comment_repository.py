from typing import List
from domains.comment_domain import Comment
from repositories.icomment_repository import ICommentRepository
import aiohttp
from utils.consts import COMMENT_URL

class CommentRepository(ICommentRepository):       
    async def fetch_comments(self) -> List[Comment]:
        async with aiohttp.ClientSession() as session:
            async with session.get(COMMENT_URL) as response:
                data = await response.json()
                return [Comment(**comment) for comment in data]
        