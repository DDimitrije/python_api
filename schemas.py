from marshmallow import Schema, fields

#Plain
class PlainManifestacijaSchema(Schema):
    id_manifestacija = fields.Int(dump_only=True)
    imeManifestacija = fields.Str(required=True)
    datum = fields.Str(required=True)
    vremeStarta = fields.Str(required=True)


class PlainTrkaSchema(Schema):
    id_trka = fields.Int(dump_only=True)
    nazivTrka = fields.Str(required=True)
    startTrka = fields.Str(required=True)
    krajTrka = fields.Str(required=True)
    storno = fields.Str(required=True)
    #id_manifestacije = fields.Int(required=True)


class PlainTrkacSchema(Schema):
    id_trkac = fields.Int(dump_only=True)
    bib = fields.Str(required=True)
    tagCode = fields.Str(required=True)
    imePrezime = fields.Str(required=True)
    godinaRodjenja = fields.Str(required=True)
    mestoStanovanja = fields.Str(required=True)
    drzava = fields.Str(required=True)
    klub = fields.Str(required=True)
    starosnaKategorija = fields.Str(required=True)
    email = fields.Str(required=True)
    smsBroj = fields.Str(required=True)
    storno = fields.Str(required=True) #treba da bude bollean ili int
    #trka_id = fields.Int(required=True)
    #manifestacija_id = fields.Int(required=True)


class PlainAndroidSchema(Schema):
    id_android = fields.Int(dump_only=True)
    bib_android = fields.Str(required=True)
    pozicija_android =fields.Str(required=True)
    tag_code_android = fields.Str(required=True)
    vreme_sistemsko_android = fields.Str(required=True)
    storno_android = fields.Str(required=True)


class PlainCitacSchema(Schema):
    id_citac = fields.Int(dump_only=True)
    bib_citac = fields.Str(required=True)
    ime_preziem_citac = fields.Str(required=True)
    age_group_citac = fields.Str(required=True)
    age_gun_time = fields.Str(required=True)
    age_net_time = fields.Str(required=True)
    age_storno = fields.Str(required=True)


class PlainNegativni_poeniSchema(Schema):
    id_negativni_poeni = fields.Int(dump_only=True)
    pozicija_negativni = fields.Str(required=True)
    broj_poena_negativni = fields.Str(required=True)
    kazna_sec_negativni = fields.Str(required=True)
    storno_negativni = fields.Str(required=True)


#Schema
class ManifestacijaSchema(PlainManifestacijaSchema):
    trkas = fields.List(fields.Nested(PlainTrkaSchema()), dump_only=True)
    #trkacs = fields.List(fields.Nested(PlainTrkacSchema()), dump_only=True)


class TrkaSchema(PlainTrkaSchema):
    manifestacija_id = fields.Int(required=True, load_only=True)
    manifestacija = fields.Nested(PlainManifestacijaSchema(), dump_only=True) # koristi se samo za vracanje podataka od klijenata
    trkacs = fields.List(fields.Nested(PlainTrkacSchema()), dump_only=True)

    androids = fields.List(fields.Nested(PlainAndroidSchema()), dump_only=True)
    citacs = fields.List(fields.Nested(PlainCitacSchema()), dump_only=True)
    negativni_poenis = fields.List(fields.Nested(PlainNegativni_poeniSchema()), dump_only=True)


class TrkacSchema(PlainTrkacSchema):
    #manifestacija_id = fields.Int(load_only=True)
    #trkas = fields.List(fields.Nested(PlainTrkaSchema()), dump_only=True)
    trka_id = fields.Int(required=True, load_only=True)
    trka = fields.Nested(PlainTrkaSchema(), dump_only=True)
    #manifestacija = fields.Nested(PlainManifestacijaSchema(), dump_only=True)



#Update
class TrkaUpdateSchema(Schema):
    nazivTrka = fields.Str()
    startTrka = fields.Str()
    krajTrka = fields.Str()
    storno = fields.Str()
    manifestacija_id = fields.Int()

class TrkacUpdateSchema(Schema):
    bib = fields.Str()
    tagCode = fields.Str()
    imePrezime = fields.Str()
    godinaRodjenja = fields.Str()
    mestoStanovanja = fields.Str()
    drzava = fields.Str()
    klub = fields.Str()
    starosnaKategorija = fields.Str()
    email = fields.Str()
    smsBroj = fields.Str()
    storno = fields.Str()
    trka_id = fields.Int()


class AndroidSchema(PlainAndroidSchema):
    trka_id = fields.Int(required=True, load_only=True)
    trka = fields.Nested(PlainTrkaSchema(), dump_only=True)

class CitacSchema(PlainCitacSchema):
    trka_id = fields.Int(required=True, load_only=True)
    trka = fields.Nested(PlainTrkaSchema(), dump_only=True)

class Negativni_poeniSchema(PlainNegativni_poeniSchema):
    trka_id = fields.Int(required=True, load_only=True)
    trka = fields.Nested(PlainTrkaSchema(), dump_only=True)

class AndroidUpdateSchema(Schema):
    bib_android = fields.Str()
    pozicija_android = fields.Str()
    tag_code_android = fields.Str()
    vreme_sistemsko_android = fields.Str()
    storno_android = fields.Str()
    smsBroj = fields.Str()
    storno = fields.Str()
    trka_id = fields.Int()

class CitacUpdateSchema(Schema):
    bib_citac = fields.Str()
    ime_preziem_citac = fields.Str()
    age_group_citac = fields.Str()
    age_gun_time = fields.Str()
    age_net_time = fields.Str()
    age_storno = fields.Str()
    trka_id = fields.Int()

class Negativni_poeniUpdateSchema(Schema):
    pozicija_negativni = fields.Str()
    broj_poena_negativni = fields.Str()
    kazna_sec_negativni = fields.Str()
    storno_negativni = fields.Str()
    trka_id = fields.Int()

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    user = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)