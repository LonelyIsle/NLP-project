import pandas as pd
import numpy as np
import re,os

def load_data(path):
    df = pd.read_pickle(path)
    df["review_text_clean"] = df["review_text"].astype(str).str.lower()
    if "rating" not in df.columns and "customer_review_rating" in df.columns:
        df["rating"] = df["customer_review_rating"]
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    return df

queries = {
    "audio_quality": ("audio", "quality", ["poor"], "neg"),
    "wifi_signal": ("wifi", "signal", ["strong"], "pos"),
    "mouse_button": ("mouse", "button", ["click", "problem"], "neg"),
    "gps_map": ("gps", "map", ["useful"], "pos"),
    "image_quality": ("image", "quality", ["sharp"], "pos")
}

def match_m1(review_text, rating, aspect1, aspect2, opinions, polarity):
    text = review_text.lower()
    if pd.isna(rating):
        return False
    if polarity == "pos" and rating < 4:
        return False
    if polarity == "neg" and rating > 2:
        return False

    for op in opinions:
        if (aspect1 in text and op in text) or (aspect2 in text and op in text):
            return True
    return False


def run_m1(df, queries):
    output_dir = 'M1_Results'
    os.makedirs(output_dir, exist_ok=True)
    
    for query_name, (a1, a2, ops, pol) in queries.items():
        filename = f"{output_dir}/{query_name}_m1.txt"
        with open(filename, 'w') as f:
            for _, row in df.iterrows():
                if match_m1(row["review_text_clean"], row["rating"], a1, a2, ops, pol):
                    f.write(row["review_id"].replace("'","") + "\n")
                    
        print(f"M1 results are saved in : ", output_dir)
        
if __name__ == "__main__":
    df = load_data("/Users/will/Desktop/COSC 4397/reviews_segment.pkl")
    run_m1(df, queries)
