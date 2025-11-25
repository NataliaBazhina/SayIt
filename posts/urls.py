from rest_framework.routers import SimpleRouter
from posts.views import PostViewSet, CommentViewSet
from posts.apps import PostsConfig

app_name = PostsConfig.name

router = SimpleRouter()
router.register("posts", PostViewSet, basename="posts")
router.register("comments", CommentViewSet, basename="comments")

urlpatterns = [] + router.urls