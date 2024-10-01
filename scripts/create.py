import lancedb
from imagefile import ImageFile

db = lancedb.connect("../db")
table = db.create_table("images", schema=ImageFile)
