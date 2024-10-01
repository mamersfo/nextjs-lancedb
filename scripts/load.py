import lancedb
from itertools import chain
from pathlib import Path
import pandas as pd
from imagefile import ImageFile

db = lancedb.connect("../db")
table = db.open_table("images")

p = Path("../public/images").expanduser()

uris = [
    str(f)
    for f in chain(p.glob("*.jpg"), p.glob("*.jpeg"), p.glob("*.png"), p.glob("*.webp"))
    if f.is_file()
]

table.add(pd.DataFrame({"image_uri": uris}))
