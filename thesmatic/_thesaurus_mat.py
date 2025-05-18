from pydantic import BaseModel
from typing import Union, Literal
from agriculture import Agriculture
from administration import Administration

class ThesaurusMatiereArchivesLocales(BaseModel):
    termes_de_premier_niveau: Union[Administration, Agriculture]

for name, obj in globals().items():
    if isinstance(obj, type) and issubclass(obj, BaseModel):
        obj.model_rebuild()
