from typing import List
from domains.post_domain import Post
from repositories.ipost_repository import IPostRepository
import aiohttp
from utils.consts import API_URL

class PostRepository(IPostRepository):
    async def fetch_posts(self) -> List[Post]:
        async with aiohttp.ClientSession() as session:
            async with session.get(API_URL) as response:
                data = await response.json()
                return [Post(**post) for post in data]
