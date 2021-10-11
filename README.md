# Necktie coding test 

This is the programming test for Necktie using Docker, Python and Postgres.

# Installation instructions
1) Clone this repo. 
2) Create a .env file inside the cloned repo and add the following values:

    SECRET_KEY=supersecret
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_SERVER=db
    POSTGRES_PORT=5432
    POSTGRES_DB=postgres

3) Run the following commands:

    docker-compose up

The app is served at `localhost:8000` and the swagger docs are at `http://localhost:8000/docs`


# 1. Choice of Framework & Library: Please explain why you choose the particular framework or library.

I like to take these coding test opportunities to learn something new. In this case, I decided to try out FastAPI as I had heard about it before. I have experience using Flask along with it's ORM Flask-SqlAlchemy so this was a nice project for me to do. 

## a. What are the benefits & drawbacks associated with that choice?
The benefits of this choice was that it was really quick for me to set up given that I didn't have to define SQLAlchemy models. The drawback to this was that it was difficult to do in-memory filtering so I had to do filtering using database queries.

## b. What are the assumptions underlying that choice?
The assumption underlying my choice to use FastAPI is it's touted performance benefits.

# 2. Potential Improvement: Please elaborate on what kind of improvements you would like to implement if you have given more time.
I'd definitely like to add SQLAlchemy models to uitilize the ORM  and add unit tests for other models. Also I'd add logging to the application. I was thinking of adding comments but to be honest, this is such a simple application, I don't think it needs many comments at all. 

# 3. Production consideration: Any extra steps should be taken with caution when deploying your app to a production environment?
Make sure to not seed the production database with initial values. I added intial data as this is just a local project.
# 4. Assumptions

## a. Any assumptions you have made when you designed the data model and API schema?
I assume that a doctor can only have one office but of course, they may have several offices if they're entrepreneurial? I don't know. To keep things simple I just made that assumption. 

## b. Any other assumptions and opinions you have taken throughout the assessments?
I don't think so, the main one was stated above.

# Closing thoughts
I have finished yet another coding test with another newly learned framework and I would like to give credit to probably the best tech blog I've ever read: https://www.jeffastor.com/blog/up-and-running-with-fastapi-and-docker 
Follow my Github and add me on Linkedin :D