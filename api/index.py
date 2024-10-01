import lancedb
from fastapi import FastAPI
from lancedb.embeddings import EmbeddingFunctionRegistry
from lancedb.pydantic import LanceModel, Vector
from PIL import Image

registry = EmbeddingFunctionRegistry.get_instance()
clip = registry.get("open-clip").create()

class ImageFile(LanceModel):
    vector: Vector(clip.ndims()) = clip.VectorField()
    image_uri: str = clip.SourceField()

    @property
    def image(self):
        return Image.open(self.image_uri)

### Create FastAPI instance with custom docs and openapi url
app = FastAPI(docs_url="/api/py/docs", openapi_url="/api/py/openapi.json")


@app.get("/api/py/helloFastApi")
def hello_fast_api():
    db = lancedb.connect("db")
    names = db.table_names()
    print(names)
    table = db.open_table("images")
    rows = table.search("dog").limit(3).to_pydantic(ImageFile)
    # db.close()

    return {"rows": rows}
