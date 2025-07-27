# 🎥 YouTube Trending Video Analyzer

A Python-based data analysis project that fetches and visualizes trending YouTube videos for any selected country. This tool uses the YouTube Data API to extract key metrics like views, likes, comments, and genres, then displays insights through charts and exports to CSV.

---

## 🚀 Features

- ✅ Fetches real-time trending video data via YouTube Data API v3
- ✅ User can select a country using 2-letter region codes (e.g., `IN`, `US`, `JP`)
- ✅ Visualizes top videos by views and likes using Plotly
- ✅ Displays video genres (e.g., Music, Gaming, Education)
- ✅ Exports the data to `.csv` and `.png` files
- ✅ Clean datetime formatting for better reporting

---

## 📦 Tech Stack

| Tool / Library              | Purpose                          |
|-----------------------------|----------------------------------|
| `Python`                    | Programming language             |
| `Pandas`                    | Data analysis & manipulation     |
| `Plotly`                    | Data visualization               |
| `Kaleido`                   | Saving charts as PNG             |
| `Google API Client`         | Accessing YouTube Data API       |

---

## 🛠️ Setup Instructions

1. **Clone this repo**
   ```bash
   git clone https://github.com/yourusername/youtube-trending-analyzer.git
   cd youtube-trending-analyzer
