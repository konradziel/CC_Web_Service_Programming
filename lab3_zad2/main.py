from dependency_injector.wiring import Provide
import asyncio

from container import Container
from services.ipost_service import IPostService
from services.icomment_service import ICommentService

KEYWORD = "atque"

async def main(
        post_service: IPostService = Provide[Container.post_service],
        comment_service: ICommentService = Provide[Container.comment_service]
) -> None:
    all_posts = await post_service.get_all_posts()

    await comment_service.assing_comments_to_posts(all_posts=all_posts)

    filtered_posts = post_service.filter_posts(KEYWORD, all_posts=all_posts)

    print(f"Filtered posts containing keyword '{KEYWORD}':")
    for post in filtered_posts:
        print(f"ID: {post.id}, Title: {post.title}")
        print(f"Comments: {post.comments}")

if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    asyncio.run(main())
