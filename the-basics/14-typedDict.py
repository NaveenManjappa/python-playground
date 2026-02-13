from typing import TypedDict


class Movie(TypedDict):
    title: str
    year: int
    is_released: bool


# Example usage:
my_favorite_movie: Movie = {"title": "Inception", "year": 2010, "is_released": True}
# This will raise an error because 'year' should be an integer, not a string.
my_favorite_movie["year"] = "2010"  # Type checker will flag this
# This will raise an error because 'is_released' should be a boolean, not a string.
my_favorite_movie["is_released"] = "Yes"  # Type checker will flag this
