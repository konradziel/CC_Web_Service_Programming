from dependency_injector.wiring import Provide
import asyncio

from container import Container
from services.ipost_service import IPostService

KEYWORD = "sunt"

async def main(
        service: IPostService = Provide[Container.service],
) -> None:
    filtered_posts = await service.get_filtered_posts(KEYWORD)

    print(f"Filtered posts containing keyword '{KEYWORD}':")
    for post in filtered_posts:
        print(f"ID: {post.id}, Title: {post.title}")

if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    asyncio.run(main())
