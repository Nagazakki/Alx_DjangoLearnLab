Social Media API -  Documentation

Overview
--------
This is a Django REST Framework project that supports user registration, authentication, and social interaction through posts and comments.

----------------------------------------------
1. Setup Instructions
----------------------------------------------
1. Clone or open the project folder.
2. Install dependencies:
   pip install -r requirements.txt
3. Make migrations and migrate:
   python manage.py makemigrations
   python manage.py migrate
4. Create a superuser (optional):
   python manage.py createsuperuser
5. Run the server:
   python manage.py runserver

----------------------------------------------
2. User Authentication Endpoints
----------------------------------------------
Base URL: http://127.0.0.1:8000/api/

Endpoints:
- /register/  [POST] — Register a new user
- /login/     [POST] — Login and receive authentication token
- /profile/   [GET, PUT] — View or edit logged-in user profile

User Fields:
- username
- email
- password
- bio (optional)
- profile_picture (optional)

Example Registration Request:
POST /api/register/
{
  "username": "zachary",
  "email": "zachary@example.com",
  "password": "mypassword"
}

Example Login Request:
POST /api/login/
{
  "username": "zachary",
  "password": "mypassword"
}

Example Response:
{
  "token": "9a23b7c7c1b84b56b4d6f4d93b3c93d2"
}

----------------------------------------------
3. Posts Endpoints
----------------------------------------------
Base URL: http://127.0.0.1:8000/api/

Endpoints:
- /posts/ [GET, POST] — List or create posts
- /posts/{id}/ [GET, PUT, PATCH, DELETE] — Retrieve, update, or delete a post

Fields:
- title
- content
- author (auto)
- created_at
- updated_at

Example Create Request:
POST /api/posts/
Headers:
Authorization: Token your_token_here
Body:
{
  "title": "My First Post",
  "content": "This is my first post."
}

Example Response:
{
  "id": 1,
  "author": "zachary",
  "title": "My First Post",
  "content": "This is my first post.",
  "created_at": "2025-10-10T12:00:00Z"
}

----------------------------------------------
4. Comments Endpoints
----------------------------------------------
Endpoints:
- /comments/ [GET, POST] — List or create comments
- /comments/{id}/ [GET, PUT, PATCH, DELETE] — Retrieve, update, or delete a comment

Fields:
- post
- content
- author (auto)
- created_at
- updated_at

Example Create Comment:
POST /api/comments/
Headers:
Authorization: Token your_token_here
Body:
{
  "post": 1,
  "content": "Nice post!"
}

Response:
{
  "id": 1,
  "post": 1,
  "author": "zachary",
  "content": "Nice post!",
  "created_at": "2025-10-10T14:00:00Z"
}

----------------------------------------------
5. Filtering and Pagination
----------------------------------------------
Pagination Example:
GET /api/posts/?page=2

Search Example:
GET /api/posts/?search=keyword

----------------------------------------------
6. Notes
----------------------------------------------
- Token authentication is required for creating, updating, or deleting.
- Only authors can edit or delete their own posts or comments.
- Pagination and search are automatically handled by Django REST Framework.

FOLLOW & FEED FEATURE UPDATE
================================

Overview:
Added functionality for users to follow other users and view a feed of posts from those they follow.

--------------------
1. MODELS & MIGRATIONS
--------------------
- Updated user model with ManyToMany field:
  following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)

Commands:
python manage.py makemigrations accounts
python manage.py migrate

--------------------
2. FOLLOW MANAGEMENT VIEWS (accounts/views.py)
--------------------
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    user_to_follow = User.objects.get(id=user_id)
    request.user.following.add(user_to_follow)
    return Response({'message': f'You are now following {user_to_follow.username}.'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    user_to_unfollow = User.objects.get(id=user_id)
    request.user.following.remove(user_to_unfollow)
    return Response({'message': f'You unfollowed {user_to_unfollow.username}.'})

--------------------
3. FEED VIEW (posts/views.py)
--------------------
class FeedView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

--------------------
4. URL ROUTES
--------------------
accounts/urls.py:
  path('follow/<int:user_id>/', follow_user),
  path('unfollow/<int:user_id>/', unfollow_user),

posts/urls.py:
  path('feed/', FeedView.as_view()),

--------------------
5. TESTING
--------------------
Use Postman:
- POST /api/accounts/follow/<user_id>/
- POST /api/accounts/unfollow/<user_id>/
- GET /api/feed/

Authentication required (Token or Session).

