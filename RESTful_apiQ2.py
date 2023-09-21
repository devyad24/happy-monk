import requests

api = 'https://api.example.com/books'

def fetch_books(api):
    try:
        response = requests.get(api)
        response.raise_for_status()

        data = response.json()

        while 'next' in data.get('links', {}):
            next_url = data['links']['next']['url']
            next_response = requests.get(next_url)
            next_response.raise_for_status()
            next_data = next_response.json()
            data['books'].extend(next_data.get('books', []))
        
        return data['books']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from teh API: {e}")
        return []

def extract_data_from_books(books):
    num_books = len(books)
    if num_books == 0:
        return {
            'total_books': 0,
            'average_publication_year': None,
            'most_prolific_author': None,
            'top_genres': []
        }

    publication_years = [book.get('publication_year', 0) for book in books]
    average_publication_year = sum(publication_years) / num_books

    author_counts = {}
    for book in books:
        authors = book.get('authors', [])
        for author in authors:
            author_name = author.get('name')
            author_counts[author_name] = author_counts.get(author_name, 0 ) + 1
    
    most_prolific_author = max(author_counts, key=author_counts.get)

    genres = [book.get('genre', '') for book in books]
    genre_counts = {genre: genres.count(genre) for genre in set(genres)}
    top_genres = sorted(genre_counts, key=genre_counts.get, reverse=True)[:5]


    return {
        'total_books': num_books,
        'average_publication_year': average_publication_year,
        'most_prolific_author': most_prolific_author,
        'top_genres': top_genres
    }

def main():
    books = fetch_books(api)
    if not books:
        print("Error occured whie fetching data from api.")
        return 
    
    analysis_result = extract_data_from_books(books)

    print(f"Total Books: {analysis_result['total_books']}")
    print(f"Average Publication Year: {analysis_result['average_publication_year']:.2f}")
    print(f"Most Prolific Author: {analysis_result['most_prolific_author']}")
    print("Top 5 Genres with most books:")
    for i, genre in enumerate(analysis_result['top_genres'], start=1):
        print(f"{i}. {genre}")


if __name__ == "__main__":
    main()