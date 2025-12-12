# Movie recommendation system (User-Based Collaborative Filtering)

## Overview
It implements a collaborative filtering recommendation based on users, using MovieLens 100K Dataset.
The system recommends movies for a target user based on the preferences of similar users. The similarity is computed using cosine similarity.

---

## How It Works

1. Builds a user–item rating matrix from MovieLens data.
2. Computes user–user similarity using cosine similarity.
3. Selects the top N users most similar to the target user.
4. Predicts ratings for movies the target user has not rated using a weighted average of similar users’ ratings.
5. Returns the top M recommended movies with predicted ratings.

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Cosine Similarity
- MovieLens 100K Dataset

## Key Concepts Demonstrated
- Collaborative Filtering
- Sparse Matrix Handling
- Cosine Similarity
- Weighted Rating Prediction
- Recommendation Ranking

## Example Output
```bash
[('Toy Story (1995)', 5.0),
 ('Fargo (1996)', 4.8),
 ('Shawshank Redemption, The (1994)', 4.7)]
```
## How to Run
1. Clone the repository
2. Place MovieLens dataset files inside the ```bash dataset/``` folder
3.Run:
```bash
python test.py
```
4. Enter:
  - Target user ID
  - Number of similar users
  - Number of recommendations
