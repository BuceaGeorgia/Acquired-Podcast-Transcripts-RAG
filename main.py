
# total words in all transcripts

with open("/Users/georgia.bucea/apps/practice_ai/RAG/data/aquired/acquired_transcripts_all.txt", "r") as f:
    text = f.read()

words = text.split()
print(f"Total words in all transcripts: {len(words)}")
