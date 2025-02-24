class Facebook:
    def __init__(self) -> None:
        self.uzivatele: dict[str, list[str]] = {}

    def pridej_uzivatele(self, *uzivatele: str) -> None:
        for uzivatel in uzivatele:
            self.uzivatele[uzivatel] = []
    def pridej_znamosti(self, *znamosti: tuple[str, str]) -> None:
        for znamost in znamosti:
            self.uzivatele[znamost[0]].append(znamost[1])
            self.uzivatele[znamost[1]].append(znamost[0])
# Vytvoření instance Facebooku
fb = Facebook()

# Seznam unikátních jmen

# Vkládání známostí do Facebooku
fb.pridej_uzivatele(
    "Adam", "Beata", "Cyril", "Dana", "Emil", "František", "Gabriela", "Hana", "Ivan", "Jana",
    "Karel", "Lenka", "Marek", "Nina", "Ondřej", "Petra", "Quentin", "Radka", "Stanislav", "Tereza",
    "Urbán", "Veronika", "Walter", "Xenie", "Yvona", "Zdeněk", "Alex", "Blanka", "Cecilie", "David"
)
  
# Hardkodované známosti

# Vkládání známostí do Facebooku
fb.pridej_znamosti(
    ("Adam", "Beata"), ("Adam", "Cyril"), ("Beata", "Dana"),
    ("Cyril", "Emil"), ("Cyril", "František"), ("Dana", "Gabriela"),
    ("Emil", "Hana"), ("František", "Ivan"), ("Gabriela", "Jana"),
    ("Hana", "Karel"), ("Ivan", "Lenka"), ("Jana", "Marek"),
    ("Karel", "Nina"), ("Lenka", "Ondřej"), ("Marek", "Petra"),
    ("Nina", "Quentin"), ("Ondřej", "Radka"), ("Petra", "Stanislav"),
    ("Quentin", "Tereza"), ("Radka", "Urbán"), ("Stanislav", "Veronika"),
    ("Tereza", "Walter"), ("Urbán", "Xenie"), ("Veronika", "Yvona"),
    ("Walter", "Zdeněk"), ("Xenie", "Alex"), ("Yvona", "Blanka"),
    ("Zdeněk", "Cecilie"), ("Alex", "David"), ("Blanka", "Adam")
)

print(len(fb.uzivatele["Ondřej"]))
