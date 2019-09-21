from models.models import User
from app import ma

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User


class UserTableSchema(ma.TableSchema):
    class Meta:
        table  = User.__table__


if __name__ == '__main__':

    userschema =  UserSchema()
    print(userschema)

    user_tableschema = UserTableSchema()
    print(user_tableschema)