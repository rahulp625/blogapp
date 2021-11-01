			Blog Application

1. Home Page:
    • Shows all published posts posted by multiple authors in chronological order (i.e. newest posts first).
    • For logged in authors, all their unpublished posts are also listed.  
    • Each blog contains title, author,content and Read More button. On clicking the read more button, the visitor will be directed to detailed blog page.
    • For logged in users who are also authors, the blogs posted by them contains Edit and Delete buttons. On clicking Edit button , the author will be redirected to edit page and on clicking Delete button, the author will be redirected to confirm deletion page.

2. Blog Detail Page :
    • Contains the details of a particular blog.
    • Logged in as well as not logged in, both users are able to view this page.

3. Edit Page :
    • Only the aurthor of the blog and superuser are able to visit this page and make changes to its title , slug, content, category and status.
    • Allows the author and superuser to publish/unpublish a post. Lets say, if the author or superuser would like to make changes to a post but would like for the post to not show up on the website, then he can mark the status as unpublished which keeps the post in the database but stops it from being published on the website. The unpublished post will not be visible to other users/aurthors.
    • Once updated the user/superuser will be redirected to home page.

4. Delete Page :
    • Asks for confirmation.
    • Once confirmed, the post will be deleted from website as well as database and the aurthor will be redirected to home page.
 
5. Add Post Page :
    • The users are able to make new posts. Each posts contain  title, slug, author, content, category and status(i.e published or not published). 
    • If published the post will be visible to all visitors else will remain as draft and not visible to other users/visitors on the website.

6. Login Page:
    • Contains username and password,
    • Once logged in, the user will be directed to his home page where all posts (i.e. published as well as unpublished) are listed. The unpublished posts are marked hidden.

 Security Measure:

    • Unauthorized Access is Prohibited : Access to edit page through url by using id or slug by someone other than author or superuser is restricted.

7. Permalinks:
All blog links are permalinks. While creating a blog, fill a unique text in slug that is similar to the title but unique, containing only letters, numbers, underscores or hyphens


Blog Model
Contains the attributes-
title, slug, author, content, created_on, updated_on, published, category

Category Model-
Containes name only.


The project is made using django framework and uses sqlite db.

How to run-
1. Create a virtual environment and run pip install -r requirements.txt
2. Then run python manage.py runserver

The database is also included in the repo.
Superuser name-
admin
password - python123
