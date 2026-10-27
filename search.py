from vespa.application import Vespa

# 1. Connect to the local Vespa instance 🔌
app = Vespa(url="http://localhost", port=8080)

def search_bm25(query_text: str, hits: int = 5):
    # First: Explicitly search for "the" term to make sure the Vespa engine has some related data
    # yql = 'select id, text from doc where text contains "the"'
    
    # Second: Construct YQL (Vespa Query Language) statement 📝
    yql = "select id, text from doc where userQuery()"
    
    # Query parameters using the "bm25" rank profile defined in app.py ⚙️
    request = {
    "yql": yql,
    "query": query_text,
    "model.defaultIndex": "text",  # Directs userQuery() to search the 'text' field 🎯
    "ranking": "bm25",
    "hits": hits,
    }

    # Send query to Vespa 🚀
    response = app.query(body=request)
    
    return response.hits

if __name__ == "__main__":
    query = "economic boom"
    print(f"🔍 Searching for top hits matching: '{query}'\n")
    
    hits = search_bm25(query)
    
    for i, hit in enumerate(hits, start=1):
        relevance = hit.get("relevance", 0.0)
        doc_id = hit["fields"].get("id", "N/A")
        text_snippet = hit["fields"].get("text", "")[:150]  # First 150 chars
        
        print(f"--- Hit {i} [BM25 Score: {relevance:.4f}] ---")
        print(f"Document ID: {doc_id}")
        print(f"Snippet: {text_snippet}...\n")