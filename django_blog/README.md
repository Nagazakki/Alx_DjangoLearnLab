Django Blog Project

This project is a feature-rich blogging application built with Django. It was developed step-by-step through a series of tasks designed to cover key aspects of web development with Django: authentication, CRUD operations, user interaction, and advanced features such as tagging and search.

Features Implemented
1. Project Setup & Basic Blog Structure

Initialized a new Django project (django_blog) and blog app.

Configured base templates and static files.

Created the Post model with fields for title, content, author, and publish date.

Added views and templates for home and post listing.

2. Authentication & User Profiles

Implemented user registration, login, and logout with Django’s built-in auth system.

Extended the User model with a Profile model (bio, avatar).

Created profile views and forms for updating user information.

3. CRUD for Blog Posts

Added Create, Read, Update, and Delete (CRUD) functionality for posts using class-based views:

PostCreateView

PostDetailView

PostUpdateView

PostDeleteView

Implemented access control so only post authors can edit or delete their posts.

Configured URL patterns (post/new/, post/<pk>/update/, etc.) to match project requirements.

4. Comment Functionality

Added a Comment model linked to Post and User.

Built CommentForm for creating and editing comments.

Implemented views for:

Adding new comments (function-based view).

Updating and deleting comments (class-based views with permission checks).

Integrated comments into the PostDetailView so users can view and interact directly under each post.

5. Advanced Features: Tagging & Search

Created a Tag model with a many-to-many relationship to Post.

Extended PostForm to allow adding and editing tags.

Implemented a search system using Django’s Q objects:

Users can search by title, content, or tag name.

Added dedicated views and templates for displaying posts by tag and search results.

Configured intuitive URLs (/tags/<tag_name>/, /search/).

Deliverables

Models: Post, Comment, Tag, Profile

Forms: User registration, profile update, post form, comment form

Views: Authentication, profile management, post CRUD, comment CRUD, search, tagging

Templates: Home, post list/detail, post form, comment form, profile, search results, tag view

URLs: Configured for all features, with checker-compliant paths for posts and comments