from datasets import load_dataset
from vespa.application import Vespa
from tqdm import tqdm

# 1. Connect to running Vespa container 🔌
vespa_app = Vespa(url="http://localhost", port=8080)

# 2. Stream dataset from Hugging Face 🌊
print("Connecting to FineWeb dataset stream...")
dataset = load_dataset(
    "HuggingFaceFW/fineweb", 
    name="sample-10BT", 
    split="train", 
    streaming=True
)

# 3. Format documents into Vespa's payload format 🛠️
def document_generator(stream, max_docs=500):
    for idx, sample in enumerate(stream):
        if idx >= max_docs:
            break
        yield {
            "id": str(idx),
            "fields": {
                "id": str(idx),
                "text": sample["text"],
            },
        }

# 4. Batch Feed asynchronously ⚡
if __name__ == "__main__":
    NUM_DOCS = 500
    print(f"Feeding {NUM_DOCS} documents into Vespa...")
    
    vespa_app.feed_iterable(
        iter=tqdm(document_generator(dataset, max_docs=NUM_DOCS), total=NUM_DOCS),
        schema="doc",
    )
    print("✅ Ingestion complete!")