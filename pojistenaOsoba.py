from pydantic import BaseModel, constr, conint

class PojistenaOsoba(BaseModel):

    jmeno: constr(min_length=3)
    prijmeni: constr(min_length=3)
    vek: conint(ge=18)
    telefon: constr(regex=r'^[+][0-9]{12}$')

    def __str__(self):
        return f"{self.jmeno}\t{self.prijmeni}\t{self.vek}\t{self.telefon}"