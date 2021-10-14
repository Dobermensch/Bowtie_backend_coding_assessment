# Necktie coding test 

This is the programming test for Necktie using Docker, Python and Postgres.

# Installation instructions
1) Clone this repo. 
2) Create a .env file inside the cloned repo and add the following values:
```
    SECRET_KEY=supersecret
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_SERVER=db
    POSTGRES_PORT=5432
    POSTGRES_DB=postgres
```
3) Run the following commands:

    `docker-compose up`

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
### After initial rejection 
My biggest assumption was that this would be treated like a MVP/POC. Instead, judging by the remarks that I got, it turns out this is supposed to be a production ready application fit to be deployed and used by clients in the real world but the only problem is that candidates are given less than a day (8 hours) to do it without any product managers or frontend engineers to help them out and then are judged on why the system doesn't support a certain use case! 

Forget the fact that candidates receive nothing in return of submitting the test, not even a $20 coupon. The reviewer didn't even entertain the idea that maybe candidates are short on time and so may find it difficult to think of all the ways to make this perfect. 

# Closing thoughts
I have finished yet another coding test with another newly learned framework and I would like to give credit to probably the best tech blog I've ever read: https://www.jeffastor.com/blog/up-and-running-with-fastapi-and-docker 

### My thoughts on initial rejection

Aside from the reviewer's mistake (thinking I'm storing JSON in text column when I'm actually storing it in JSONB column when the table definition is literally in the project to see) while reviewing my assessment, I would like to address what I find to be the dismissive and unrealistic attitude of the reviewer:

Firstly, the reviewer mentioned something about inconsistent return types. Yes that's true. What's also true is that I can clearly make them consistent without any problem. In addition to that, in a real world setting, the response return types would be determined by working together with frontend engineers. This is not a real world setting. This is a coding test and companies are generally (surprisingly not in the case of necktie) happy with a MVP. So when I see the point inconsistent return types, I really don't know what to say.

Secondly, "price range filter could be better". Oh wow. Yeah, my aim was to deliver the test ASAP, I'm already sorry I didn't think of every single use case around the price range filters. Is this a test for software engineers or product managers?