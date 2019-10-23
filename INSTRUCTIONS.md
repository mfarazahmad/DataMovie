# Instructions

The following is an IMDB movie dataset available via Kaggle
https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset/data

The column names in this dataset should be more or less self-descriptive. Some of the key
columns that pertain to this mini-project are: ‘actor_1_name’, ‘actor_2_name’, ‘actor_3_name’,
‘director_name’, ‘budget’ and ‘gross’. You can make assumptions about these names as you
see fit in case they do not seem descriptive enough.
The task requires the following (Note: please use any libraries that you see fit, if applicable, for
the following steps):

1. Import the file into a local db
2. Then write functions in Python to perform the following:
    a. Load the relevant data from the db in Step 1 into your program :
    b. For this data, compute the top 10 genres in decreasing order by their profitability.
    Note: You could (but are not required to) compute profitability as simply as:
        i. ‘gross’ - ’budget’ or
        ii. (‘gross’ - ‘budget’)/’budget’
        iii. Anything advanced that you can think of
    c. Return the top 10 actors or directors in decreasing order by their profitability (use
    any definition you choose for profitability using the above guidance).
    d. Bonus questions ( Note: If you choose to do any of the bonus questions
    below, any one question is more than adequate ):
        i. Choice 1: Find the best actor, director pairs (up to 10) that have the
        highest IMDB_ratings, if there are indeed any such pairs.
        ii. Choice 2: Any interesting questions that you would like to work on if you
        would (for e.g. imdb_score, actor facebook_likes
        iii. Choice 3: Build a REST API to return an actor’s information (simple text
        output)
3. Write unit tests for your functions. Note: This is an important step for this project.
4. Commit code to a git repo (gitlab or github) and send us a link to it.
5. Also document your steps, libraries used and any instructions.

## Note: Please feel free to make assumptions as you see fit.