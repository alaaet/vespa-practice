from vespa.deployment import VespaDocker
from vespa.package import ApplicationPackage, Document, Field, RankProfile, Schema

# 1. Define Document Schema 📄
schema = Schema(
    name="doc",
    document=Document(
        fields=[
            Field(name="id", type="string", indexing=["summary"]),
            Field(
                name="text",
                type="string",
                indexing=["index", "summary"],
                index="enable-bm25",  # Enable BM25 term statistics
            ),
        ]
    ),
    rank_profiles=[
        RankProfile(
            name="bm25",
            first_phase="bm25(text)",  # Calculate BM25 score over the 'text' field
        )
    ],
)

# 2. Package the Application 📦
app_package = ApplicationPackage(name="fineweb", schema=[schema])

# 3. Deploy Vespa Container via Docker 🐳
if __name__ == "__main__":
    print("Deploying Vespa container to Docker...")
    vespa_docker = VespaDocker()
    app = vespa_docker.deploy(application_package=app_package)
    print(f"✅ Vespa app deployed successfully! Endpoint: {app.url}")