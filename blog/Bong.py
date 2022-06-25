from marshmallow import Schema, fields, post_load

class Bong:
    def __init__(self, id, name, release, genres):
        self.id = id
        self.name = name
        self.release = release
        self.genres = genres

    def __repr__(self):
        return (
            f'<song(id={self.id}, name={self.name}), '
            f'release={self.release.isoformat()}, genres={self.genres}>'
        )

class BongSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    release = fields.Date()
    genres = fields.List(fields.String())

    @post_load
    def make_song(self, data, **kwargs):
        return Bong(**data)

external_data = {
    'id': 101,
    'name': 'Bohemian Rhapsody',
    'release': '1975-10-31',
    'genres': ['Hard Rock', 'Progressive Rock']
}

bong = BongSchema().load(external_data)
print(bong)
