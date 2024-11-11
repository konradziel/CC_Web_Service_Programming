from dependency_injector import containers, providers
from repositories.post_repository import PostRepository
from services.post_service import PostService
from repositories.comment_repository import CommentRepository
from services.comment_service import CommentService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    post_repository = providers.Singleton(PostRepository)
    comment_repository = providers.Singleton(CommentRepository)
    
    post_service = providers.Factory(PostService, repository=post_repository)
    comment_service = providers.Factory(CommentService, comment_repository=comment_repository, post_repository=post_repository)
