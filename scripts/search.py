import lancedb
from imagefile import ImageFile

db = lancedb.connect("../db")
table = db.open_table("images")

rows = table.search("dog").limit(3).to_pydantic(ImageFile)
print(rows)