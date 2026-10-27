from vespa.application import Vespa

app = Vespa(url="http://localhost", port=8080)

# Query to match all documents regardless of terms 🌐
response = app.query(yql='select * from doc where true')

print("HTTP Status Code:", response.status_code)
print("Total Hits Found:", len(response.hits))
if response.hits:
    print("Sample Hit:", response.hits[0])