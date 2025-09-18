from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

# Make sure visuals directory exists
os.makedirs("visuals", exist_ok=True)

# Longer example texts
positive_text = """This product is amazing great fantastic excellent wonderful
happy love enjoy awesome best outstanding superb brilliant
great value totally recommend absolutely fantastic excellent"""
negative_text = """Terrible bad worst horrible disappointing poor sad hate awful
problem broken useless waste terrible experience never again
worst quality disappointing very poor awful horrible bad"""

# Positive WordCloud
wc_pos = WordCloud(width=800, height=400, background_color="white").generate(positive_text)
plt.figure(figsize=(10,5))
plt.imshow(wc_pos, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud - Positive Reviews", fontsize=16)
plt.savefig("visuals/wordcloud_positive.png")
plt.close()

# Negative WordCloud
wc_neg = WordCloud(width=800, height=400, background_color="white").generate(negative_text)
plt.figure(figsize=(10,5))
plt.imshow(wc_neg, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud - Negative Reviews", fontsize=16)
plt.savefig("visuals/wordcloud_negative.png")
plt.close()

print("✅ Word clouds generated in sentiment-analysis/visuals/")

