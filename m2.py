import pandas as pd
import os,re

def load_data(path="reviews_segment.pkl"):
    df = pd.read_pickle(path)
    df["review_text_clean"] = df["review_text"].astype(str).str.lower()
    df["review_title_clean"] = df["review_title"].astype(str).str.lower()
    df["customer_review_rating"] = pd.to_numeric(df["customer_review_rating"], errors="coerce")
    return df.dropna(subset=["customer_review_rating"])

queries = {
    "audio_quality": ("audio", "quality", ["poor", "bad", "terrible", "awful"], "neg"),
    "wifi_signal": ("wifi", "signal", ["strong", "great", "excellent", "stable"], "pos"),
    "mouse_button": ("mouse", "button", ["problem", "issue", "broken", "stuck", "unresponsive"], "neg"),
    "gps_map": ("gps", "map", ["helpful", "accurate", "useful", "detailed"], "pos"),
    "image_quality": ("image", "quality", ["sharp", "clear", "high", "excellent"], "pos")
}

def proximity_match(text, aspect1, aspect2, opinions, max_distance=10):
    words = re.findall(r'\w+', text.lower())
    aspect_positions = [i for i, word in enumerate(words) if word in (aspect1, aspect2)]
    opinion_positions = {op: [i for i, word in enumerate(words) if word == op] for op in opinions}

    for a_pos in aspect_positions:
        for o_pos, op_positions in opinion_positions.items():
            for o_pos in op_positions:
                if abs(a_pos - o_pos) <= max_distance:
                    return True
    return False

def match_m2(title, body, rating, aspect1, aspect2, opinions, polarity):
    if polarity == "pos" and rating < 4:
        return False
    if polarity == "neg" and rating > 2:
        return False
    
    opinions_set = set(opinions)

    return (
        proximity_match(title, aspect1, aspect2, opinions_set) or 
        proximity_match(body, aspect1, aspect2, opinions_set)
    )

def run_m2(df, queries):
    output_dir = "Outputs/M2_Results"
    os.makedirs(output_dir, exist_ok=True)

    for query_name, (a1, a2, ops, polarity) in queries.items():
        filename = f"{output_dir}/{query_name}_test4.txt"
        with open(filename, "w") as f:
            for _, row in df.iterrows():
                if match_m2(row["review_title_clean"], row["review_text_clean"], row["customer_review_rating"], a1, a2, ops, polarity):
                    f.write(row["review_id"].replace("'", "") + "\n")
    
    print("M2 outputs files saved in:", output_dir)

if __name__ == "__main__":
    df = load_data("/Users/will/Desktop/COSC 4397/reviews_segment.pkl")
    run_m2(df, queries)