from googleapiclient.discovery import build
import pandas as pd
import plotly.express as px

API_KEY = "Your Youtube API Key"
youtube = build("youtube", "v3", developerKey=API_KEY)

def get_category_map(region="IN"):
    category_request = youtube.videoCategories().list(part="snippet", regionCode=region)
    category_response = category_request.execute()
    return {
        item["id"]: item["snippet"]["title"]
        for item in category_response["items"]
    }

def fetch_trending_videos(region="IN", max_results=25):
    category_map = get_category_map(region)
    request = youtube.videos().list(
        part="snippet,statistics",
        chart="mostPopular",
        regionCode=region,
        maxResults=max_results
    )
    response = request.execute()

    videos = []
    for item in response["items"]:
        cat_id = item["snippet"].get("categoryId", "NA")
        videos.append({
            "Title": item["snippet"]["title"],
            "Channel": item["snippet"]["channelTitle"],
            "Views": int(item["statistics"].get("viewCount", 0)),
            "Likes": int(item["statistics"].get("likeCount", 0)),
            "Comments": int(item["statistics"].get("commentCount", 0)),
            "Published": item["snippet"]["publishedAt"][:10],
            "Genre": category_map.get(cat_id, "Unknown"),
            "Region": region
        })
    return pd.DataFrame(videos)

# ---------- User Input ----------
region = input("Enter a 2-letter region code (e.g., IN, US, GB): ").upper().strip()
if not region:
    region = "IN"

# ---------- Fetch & Process ----------
df = fetch_trending_videos(region=region)
df["Published"] = pd.to_datetime(df["Published"])

# ---------- Save CSV ----------
csv_name = f"trending_videos_{region}.csv"
df.to_csv(csv_name, index=False)
print(f"✅ CSV saved as '{csv_name}'")

# ---------- Visualize ----------
fig1 = px.bar(df.sort_values("Views", ascending=False).head(10),
              x="Title", y="Views", color="Channel",
              title=f"Top 10 Trending Videos by Views ({region})")
fig1.write_image(f"top_views_{region}.png")
print(f"📊 Chart saved as 'top_views_{region}.png'")

fig2 = px.bar(df.sort_values("Likes", ascending=False).head(10),
              x="Title", y="Likes", color="Genre",
              title=f"Top 10 Trending Videos by Likes ({region})")
fig2.write_image(f"top_likes_{region}.png")
print(f"📊 Chart saved as 'top_likes_{region}.png'")

