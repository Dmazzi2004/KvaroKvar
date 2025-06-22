from pony.orm import Database, Required, Optional
from datetime import datetime

db = Database()

class IzvjesceKvara(db.Entity):
    title = Required(str)
    opis = Required(str)
    category = Required(str)
    status = Required(str)
    prioritet = Required(str)
    datum_prijave = Required(datetime, default=lambda: datetime.now())
    datum_popravka = Optional(datetime)