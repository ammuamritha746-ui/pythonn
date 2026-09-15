blog_views = [150, 800, 2500, 600, 1200, 450, 3000]

total_views = 0
trending_posts = 0

for views in blog_views:
    if views > 1000:
        print(views, "- Trending")
        trending_posts += 1
    elif views >= 500:
        print(views, "- Average")
    else:
        print(views, "- Low Traffic")

    total_views += views

print("Total number of views:", total_views)
print("Number of Trending posts:", trending_posts)