import pandas as pd
import random

# Define new dataset with updated post types
data_updated = [
    {
        "post_id": i + 1,
        "post_type": random.choice(["reel", "static_image", "carousel", "text", "video"]),
        "content_category": random.choice(
            ["travel", "food", "motivation", "fashion", "technology", "news", "nature", 
             "sports", "education", "health", "entertainment", "history", "art", "gaming", 
             "science", "fitness", "politics", "books", "pets"]
        ),
        "likes": random.randint(100, 3000),
        "shares": random.randint(20, 600),
        "comments": random.randint(10, 200),
        "user_sentiment": random.choice(["positive", "neutral", "negative"])
    } for i in range(25)
]

# Convert to DataFrame
df_updated = pd.DataFrame(data_updated)

# Define the file path to save the CSV
csv_path_updated = 'social_media_dataset_updated.csv'

# Save the DataFrame as a CSV file
df_updated.to_csv(csv_path_updated, index=False)

# Return the file path and content
with open(csv_path_updated, 'r') as file:
    file_content = file.read()

# Print file path for reference and return the content
print(f"CSV file saved at: {csv_path_updated}")
#file_content  # This will display the file content in output
