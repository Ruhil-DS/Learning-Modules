import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, Integer, ForeignKey
from sqlalchemy import select

from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


# We need to extend the base with the classes. One for each table that we have in the file
class USER(Base):
    __tablename__ = 'user'  # Same table name as in the db
    # Now, we define the schema of the table. Use the same names as that in the .sqlite3 file
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    # We can define a many-to-one relationship as follows ->
    # articles = relationship("ARTICLE", secondary="authors")


class ARTICLE(Base):
    __tablename__ = 'article'
    article_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    content = Column(String)
    # We need to define many-to-many relationship between users and articles.
    # Whenever I get users, i want articles too
    # In our case, an article can have many users(as authors)
    # Authors linking to user's table through a secondary table called article_authors
    authors_relationship = relationship("USER", secondary="authors")


class AUTHORS(Base):
    __tablename__ = 'authors'
    article_id = Column(Integer, ForeignKey("article.article_id"), primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("user.user_id"), primary_key=True, nullable=False)


# We now want to set up a connection with a db.
# We do this by connecting to a db by an engine

engine = create_engine("sqlite:///database.sqlite3")

# We can now get a connection and run a query -
'''
statement = select(USER)
print("-----------QUERY------------")
print(statement)
with engine.connect() as connection:
    print("-------------result------------")
    for row in connection.execute(statement):
        print(row)
'''

# We usually don't create a connection everytime, we create a session to work with.
""" 
comment
with Session(engine) as session:
    articles = session.query(ARTICLE).filter(ARTICLE.article_id.like("_") ).all()

    print("-----------------------------")
    for article in articles:
        print("article title : ", article.title)
        print()
        print()
        for author in article.authors_relationship:
            print("Author Email: ", author.email)
            print("Author Username: ", author.username)
            print("Author User ID: ", author.user_id)
            print()
        print("Article Content : ", article.content)
        print("-----------------------------")

"""

# We can also implement a transaction. We set autoflush = False in the session
''' comment
with Session(engine, autoflush=False) as session:
    session.begin()
    try:
        article = ARTICLE(title="Added using code",
                          content="This content has been added using the python connection as well. wuhuuu")
        session.add(article)

        session.flush()

        print(article.article_id)
        author1 = AUTHORS(user_id=1, article_id=article.article_id)
        author2 = AUTHORS(user_id=3, article_id=article.article_id)
        session.add(author1)
        session.add(author2)
    except:
        print("----- Rolling back -----")
        session.rollback()
    else:
        print("---- Committing ----")
        session.commit()
'''

# Alternative way ->
# We append to "authors" via the relationship
with Session(engine, autoflush=False) as session:
    session.begin()
    try:
        article = ARTICLE(title="Relationships 2",
                          content="Using the python connection as well with relationships. wuhuuu 2222")
        author1 = session.query(USER).filter(USER.username == "Aman").one()
        author2 = session.query(USER).filter(USER.user_id == 4).one()

        article.authors_relationship.append(author1)
        article.authors_relationship.append(author2)


        session.add(article)


    except:
        print("----- Rolling back -----")
        session.rollback()
    else:
        print("---- Committing ----")
        session.commit()

