#  a basic data class 

# importing dataclass module
from dataclasses import dataclass


@dataclass
class Article():
    '''
    A class for holding an article content
    '''

    # Attributes declaration
    # using type hints 
    title: str
    author: str 
    language: str
    upvotes: int


# A DataClass object
# article = Article('Metaverse', 'kofi teddy', 'python', 0)

# print(article)
# article = Article() gives type errors missing arguments

# Equality of DataClasses
article1 = Article('Metaverse', 'kofi teddy', 'python', 0)
article2 = Article('Everything django docker', 'kofi teddy', 'python', 0)
article3 = Article('Metaverse', 'kofi teddy', 'python', 0)

print('Dataclass equal: ', article1 == article2)
print('Dataclass equal: ', article1 == article3)
