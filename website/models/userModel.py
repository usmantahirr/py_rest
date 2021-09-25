# from .. import app
# TODO: create db instance, import app somehow, create model

class UserModel(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)

  # toString() replacement
  def __repr__(self) -> str:
    return f"User(id={id}, name={name})"
