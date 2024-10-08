# book-recommendations
UT Austin: CS 313E Elements of Software Design - Term Project
By: Aayushi Dumka & Nicole Li

OVERVIEW:
This Python program is a system that recommends books to users based on their reading genre preferences. It will take input from a genre that the user wants to explore and print out a user-desired number of random recommendations within that genre out of a dictionary of 10,000 books. Additionally, it will sort the output of recommended books based on the book ratings, so the user will get an output of randomized books with the highest rated book at the top of the output.

EXPLANATION OF DATASET:
The dataset is from Kaggle titled "Best Books - 10k Multi-Genre Data" will be used. This data set comprises 10k of the most recommended books of all time. For each book, it includes the name, author, description, genres, average rating, number of ratings, and URL. 

Users can download the dataset directly from Kaggle by visiting: 
https://www.kaggle.com/datasets/ishikajohari/best-books-10k-multi-genre-data

LIBRARIES:
We used the pandas library to read in the books dataset, so that the recommendation will be pulled from the given data based on user-desired filtering. Also, we used the random library to generate random numbers that will result in random book recommendations being outputted.

DATA STRUCTURES:
To complete this software program, we utilized dictionaries and lists as our main 
data structures. The dictionary was used to hold individual book information from the Kaggle dataset, with each book number corresponding to each key, and the book’s information corresponding to the key’s respective values. Lists were used to store information gathered from the dictionary, from genre lists to randomized book lists.

ALGORITHM: MERGE SORT
Additionally, since the dataset is very large and users can ask for a large number of books from the dataset, we wanted to make it easy to sort the output of randomized books by the average book rating. Therefore, we used a merge sort as it has a fast run time when it comes to sorting a large number of data elements. The merge sort was used to sort the ratings of a list of randomized books in descending order.

PROJECT RESULTS:
The system provides a quick and relevant set of book recommendations to the user based on user input. User interaction is straightforward and intuitive via the command line interface. 

Limitations: Since the recommendations are genre-based without considering the user history or deeper preferences, the suggestions may not always align perfectly with every user’s tastes. The quality of recommendations is highly dependent on the dataset. Any inaccuracies or biases in the dataset could affect recommendation quality.



