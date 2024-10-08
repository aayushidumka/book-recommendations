import random
import pandas as pd

# Read the CSV file containing Goodreads data
data = pd.read_csv('goodreads_data.csv')
# Drop the 'Description' column from the data
data = data.drop("Description", axis=1)
# Rename a column for clarity
data.rename(columns={'Unnamed: 0': 'Serial #'}, inplace=True)
# Convert DataFrame to a dictionary with tuples of relevant book info
data_dict = data.set_index('Serial #')[['Book', 'Author', 'Genres', 'Avg_Rating', 'Num_Ratings', 'URL']].apply(tuple, axis=1).to_dict()

def find_genre(book_dict, genre):
    """This function takes in the dictionary with the book data, the user-input of desired genre, and an empty book list as the two parameters. 
    It returns a list of book numbers (key of the dictionary) that correspond with books within the specified genre."""
    book_list = []
    # Iterate through the books in the dictionary
    for key in range(len(book_dict)):
        book_info = book_dict.get(key)
        # Parse the genre string into a list
        genre_list = book_info[2]
        genre_list = genre_list[2:-2].split("', '")
        # Add book to list if it matches the genre
        if genre in genre_list:
            book_list.append(key)
    return book_list

def genre_shelf(book_dict):
    """This function takes in the dictionary with the book data as its parameter. It generates and returns a unique set of all genres 
    available within a book dictionary."""
    # Collect a unique set of all genres
    genre_set = set()
    for key in range(len(book_dict)):
        book_info = book_dict.get(key)
        # Parse the genre string into a list
        genre_list = book_info[2]
        genre_list = genre_list[2:-2].split("', '")
        # Add genre to the set of genres
        for genre in genre_list:
            genre_set.add(genre)
    return genre_set

def randomize_books(user_books, random_number):
    """This function takes in a list of all books with the user-desired genre and a random number of books that the user inputs as its parameters. 
    It randomly selects a specified number of books from a list, or all books if the requested number exceeds the list's size."""
    # Randomly select books up to the requested number, or return all if fewer are available
    if len(user_books) < random_number:
        print("Disclaimer: This genre only has", len(user_books), "book(s)")
        return user_books
    return random.sample(user_books, random_number)

def rating_list(randomized_books):
    """This function takes in the random sample of a user desired number of books with the randomized_books as its parameter. 
    It extracts and returns a list of ratings from a specified list of book identifiers."""
    # Collect the ratings of the randomized books
    rating_list = []
    for key in randomized_books:
        book_info = data_dict.get(key)
        rating = book_info[3]
        rating_list.append(float(rating))
    return rating_list

def merge(arr, left_i, mid_i, right_i): # referenced Professor Teymourian's Github
    """The merge function takes two pre-sorted halves of an array and merges them into a single sorted sequence."""
    # Helper function for merging two halves in merge sort
    n_1 = mid_i - left_i + 1
    n_2 = right_i - mid_i
    left = [0] * n_1
    right = [0] * n_2
    for i in range(0, n_1):
        left[i] = arr[left_i + i]
    for j in range(0, n_2):
        right[j] = arr[mid_i + 1 + j]
    i = 0           
    j = 0          
    k = left_i      
    while i < n_1 and j < n_2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < n_1:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < n_2:
        arr[k] = right[j]
        j += 1
        k += 1

def merge_sort(arr, left, right): # referenced Professor Teymourian's Github
    """The merge_sort function recursively divides the array into halves, sorts each half, and then uses merge to combine these sorted halves back into a fully sorted array."""
    # Merge sort algorithm
    if left < right:
        mid = left + (right - left) // 2
        merge_sort(arr, left, mid) 
        merge_sort(arr, mid+1, right) 
        merge(arr, left, mid, right) 

def sorted_recommendations(my_arr, randomized_books, data_dict):
    """This function takes in the reversed sorted array of ratings (high to low), the list of randomized book numbers, and the original book dictionary. 
    It matches sorted ratings with their corresponding book details and returns a list of these details in sorted order."""
    # Match sorted ratings to book details
    sorted_books = []
    for rating in my_arr:
        for key in randomized_books:
            book_info = data_dict.get(key)
            book_rating = float(book_info[3])
            if book_rating == rating:
                sorted_books.append(book_info)
                break
    return sorted_books

def main():
    """The main function prompts the user to input a desired book genre and the number of book recommendations they want, verifies 
    the existence of the genre, retrieves and sorts a list of books from that genre based on ratings, and then prints out detailed information for each recommended book."""
    user_genre = input("Please enter the genre you are interested in (write in Title Case): ").strip()
    genre_set = genre_shelf(data_dict)
    while user_genre not in genre_set:
        print("Genre does not exist. Please try again!")
        user_genre = input("Please enter the genre you are interested in (write in Title Case): ").strip()
    num_books = int(input("How many books do you want recommended? "))
    user_books = find_genre(data_dict, user_genre)
    randomized_books = randomize_books(user_books, num_books)
    my_arr = rating_list(randomized_books)
    merge_sort(my_arr, 0, len(my_arr)-1)
    my_arr.reverse()
    sorted_books = sorted_recommendations(my_arr, randomized_books, data_dict)
    book_counter = 1
    for key in sorted_books:
        name, author, genres, rating, num_ratings, url = key
        print("Book ", book_counter, ":", sep="")
        print("\tBook Name:", name)
        print("\tAuthor Name:", author)
        print("\tGenres:", genres)
        print("\tAverage Rating:", rating)
        print("\tNunber of Ratings:", num_ratings)
        print("\tGoodreads URL:", url)
        print()
        book_counter += 1

main()
