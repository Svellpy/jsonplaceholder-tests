#Урлы и эндпоинты для апишки JSONPlaceholder
class ApiUrls:
    BASE_URL = "https://jsonplaceholder.typicode.com"

class PostsEndpoints:
    GET_ONE = "/posts/{post_id}"
    GET_ALL = "/posts"
    CREATE = "/posts"
    UPDATE = "/posts"
    PACH = "/posts/{post_id}"
    DELETE = "/posts/{post_id}"

class UsersEndpoints:
    GET_ALL = "/users"
    GET_ONE = "/users/{users_id}"

class CommentsEndpoints:
    GET_ALL = "/comments"
    GET_BY_POST = "/posts/{post_id}/comments"