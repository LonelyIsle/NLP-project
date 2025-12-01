**NLP-project**

This project aims to find relevant reviews in a large data set after implementing and evaluating 3 different models: boolean_search, 
M1(uses a polarity filter) and M2(uses a polarity filter, proximity filter, and review titles). This is mostly done to ensure that only relevant
reviews are presented to the user based on their search.

```bash 
NLP-PROJECT/
│
├── codes/
│   ├── boolean_search.py      # Baseline Boolean model
│   ├── m1.py                  # Method 1 (polarity-based filtering)
│   ├── m2.py                  # Method 2 (polarity + proximity + title relevancy)
│   ├── data.py                # Shared data-loading utilities
│   └── README.md              # How to run each code file
│
├── outputs/
│   ├── Boolean_Results/       # Output files produced by boolean_search.py
│   │     audio_quality_test1.txt
│   │     audio_quality_test2.txt
│   │     audio_quality_test3.txt
│   │     gps_map_test1.txt
│   │     gps_map_test2.txt
│   │     gps_map_test3.txt
│   │     ...etc
│   │
│   ├── M1_Results/            # Output files produced by m1.py
│   │     audio_quality_m1.txt
│   │     gps_map_m1.txt
│   │     image_quality_m1.txt
│   │     mouse_button_m1.txt
│   │     wifi_signal_m1.txt
│   │
│   └── M2_Results/            # Output files produced by m2.py
│         audio_quality_test4.txt
│         gps_map_test4.txt
│         image_quality_test4.txt
│         mouse_button_test4.txt
│         wifi_signal_test4.txt
│
├── NLP Report.pdf             # Full write-up of the project
└── README.md                  # Project overview + instructions
```
