from vespa.application import Vespa

app = Vespa(url="http://localhost", port=8080)

# Fetch document with ID "0"
doc = app.get_data(schema="doc", data_id="0")
print(doc.json)