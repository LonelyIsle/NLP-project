import pandas as pd
import numpy as np
import re,os

def load_data(path="C:/Users/will/Desktop/COSC 4397/res_proj/dataset in python pickle and excel format/reviews_segment.pkl"):
    df = pd.read_pickle(path)
    df["review_text_clean"] = df["review_text"].astype(str).str.lower()
    return df

queries = {
    "audio_quality": ("audio", "quality", ["poor"]),
    "wifi_signal": ("wifi", "signal", ["strong"]),
    "mouse_button": ("mouse", "button", ["click", "problem"]),
    "gps_map": ("gps", "map", ["useful"]),
    "image_quality": ("image", "quality", ["sharp"])
}