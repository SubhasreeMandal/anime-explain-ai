from core.explainer import explain
topic = input("Enter a topic:")
anime = input("Choose an anime (e.g., Naruto, One Piece, Attack on Titan):")
level = input("Choose level (beginner / intermediate): ")
result = explain(topic, anime, level)
print("\nExplanation:\n")
print(result)