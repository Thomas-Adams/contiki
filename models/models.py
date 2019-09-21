from sqlalchemy.orm import deferred
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, Text, ForeignKey, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
import datetime

from sqlalchemy.orm import relationship

DATAB_BASE_URL = 'postgresql+psycopg2://postgres:postgres@localhost:5432/contacts'

engine = create_engine(DATAB_BASE_URL)
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(50), nullable=False,unique=True)
    password = Column(String(50), nullable=False, index=True)
    email = Column(String(100), nullable=False, index=True)
    enabled = Column(Boolean, nullable=False, default=False, index=True)
    locked = Column(Boolean, nullable=False, default=False, index=True)
    expired = Column(Boolean, nullable=False, default=False, index=True)
    credentials_expired = Column(Boolean, nullable=True, default=False, index=True)
    last_login = Column(DateTime, nullable=True, index=True)
    roles = relationship('Role', secondary='user_roles')
    created = Column(DateTime, nullable=False, index=True, default=datetime.datetime.utcnow())
    created_by = Column(String(50), nullable=True, index=True)
    modified = Column(DateTime, nullable=True, index=True)
    modified_by = Column(String(50), nullable=True, index=True)
    credentials_modified = Column(DateTime, nullable=True, index=True)
    credential_modified_by = Column(String(50), nullable=True, index=True)


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, index=True)
    description = Column(Text, nullable=True)
    object = Column(String(50), nullable=False, index=True)
    permissions = relationship('Permission', secondary='role_permissions')
    users = relationship('User', secondary='user_roles')
    created = Column(DateTime, nullable=False, index=True, default=datetime.datetime.utcnow())
    created_by = Column(String(50), nullable=True, index=True)
    modified = Column(DateTime, nullable=True, index=True)
    modified_by = Column(String(50), nullable=True, index=True)


class Permission(Base):
    __tablename__ = 'permission'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, index=True)
    description = Column(Text, nullable=True)
    object = Column(String(50), nullable=False, index=True)
    roles = relationship('Role', secondary='role_permissions')
    created = Column(DateTime, nullable=False, index=True, default=datetime.datetime.utcnow())
    created_by = Column(String(50), nullable=True, index=True)
    modified = Column(DateTime, nullable=True, index=True)
    modified_by = Column(String(50), nullable=True, index=True)


class RolePermissions(Base):
    __tablename__ = 'role_permissions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    role_id = Column(Integer, ForeignKey('role.id'), index=True, nullable=False)
    permission_id = Column(Integer, ForeignKey('permission.id'), index=True, nullable=False)
    created = Column(DateTime, nullable=False, index=True, default=datetime.datetime.utcnow())
    created_by = Column(String(50), nullable=True, index=True)


class UserRoles(Base):
    __tablename__ = 'user_roles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    role_id = Column(Integer, ForeignKey('role.id'), index=True, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), index=True, nullable=False)
    created = Column(DateTime, nullable=False, index=True, default=datetime.datetime.utcnow())
    created_by = Column(String(50), nullable=True, index=True)


class Gender(Base):
    __tablename__ = 'gender'

    id = Column(Integer, primary_key=True, autoincrement=True)
    gender = Column(String(50), nullable=False, index=True)


class Salutation(Base):
    __tablename__ = 'salutation'

    id = Column(Integer, primary_key=True, autoincrement=True)
    saluation = Column(String(50), nullable=False, index=True)
    gender_id = Column(Integer, ForeignKey('gender.id'), index=True, nullable=True)
    description = Column(Text, nullable=True)


class Country(Base):
    __tablename__ = 'country'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), nullable=False, index=True)
    code = Column(String(10), nullable=False, index=True)
    domain = Column(String(10), nullable=False, index=True)
    description = Column(Text, nullable=True)
    flag = deferred(Column(LargeBinary, nullable=True))


class Profile(Base):
    __tablename__ = 'profile'

    id = Column(Integer, primary_key=True, autoincrement=True)
    given_name = Column(String(50), nullable=False, index=True)
    sur_name = Column(String(50), nullable=False, index=True)
    gender_id = Column(Integer, ForeignKey('gender.id'), index=True, nullable=False)
    salutation_id = Column(Integer, ForeignKey('salutation.id'), index=True, nullable=False)
    birthday = Column(DateTime, nullable=False, index=True)
    mobile = Column(String(50), nullable=True, index=True)
    phone = Column(String(50), nullable=True, index=True)
    avatar = deferred(Column(LargeBinary, nullable=True))
    created = Column(DateTime, nullable=False, index=True, default=datetime.datetime.utcnow())
    created_by = Column(String(50), nullable=True, index=True)
    modified = Column(DateTime, nullable=True, index=True)
    modified_by = Column(String(50), nullable=True, index=True)


class AddressType(Base):
    __tablename__ = 'address_type'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, index=True)
    address_format = Column(String(255), nullable=True, index=True)
    description = Column(Text, nullable=True)
    created = Column(DateTime, nullable=False, index=True, default=datetime.datetime.utcnow())
    created_by = Column(String(50), nullable=True, index=True)
    modified = Column(DateTime, nullable=True, index=True)
    modified_by = Column(String(50), nullable=True, index=True)


class ContactGroup(Base):
    __tablename__ = 'contact_group'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, index=True)
    description = Column(Text, nullable=True)
    avatar = deferred(Column(LargeBinary, nullable=True))
    created = Column(DateTime, nullable=False, index=True, default=datetime.datetime.utcnow())
    created_by = Column(String(50), nullable=True, index=True)
    modified = Column(DateTime, nullable=True, index=True)
    modified_by = Column(String(50), nullable=True, index=True)


class Contact(Base):
    __tablename__ = 'contact'

    id = Column(Integer, primary_key=True, autoincrement=True)
    given_name = Column(String(50), nullable=False, index=True)
    sur_name = Column(String(50), nullable=False, index=True)
    gender_id = Column(Integer, ForeignKey('gender.id'), index=True, nullable=False)
    salutation_id = Column(Integer, ForeignKey('salutation.id'), index=True, nullable=False)
    birthday = Column(DateTime, nullable=False, index=True)
    avatar = Column(LargeBinary, nullable=True)
    group_id = Column(Integer, ForeignKey('contact_group.id'), index=True, nullable=False)
    addresses = relationship('Address')
    created = Column(DateTime, nullable=False, index=True, default=datetime.datetime.utcnow())
    created_by = Column(String(50), nullable=True, index=True)
    modified = Column(DateTime, nullable=True, index=True)
    modified_by = Column(String(50), nullable=True, index=True)


class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True, autoincrement=True)
    type_id = Column(Integer, ForeignKey('address_type.id'), index=True, nullable=False)
    contact_id = Column(Integer, ForeignKey('contact.id'), index=True, nullable=False)
    street_name = Column(String(255), nullable=True, index=True)
    street_suffix = Column(String(255), nullable=True, index=True)
    zipcode = Column(String(255), nullable=True, index=True)
    post_box = Column(String(255), nullable=True, index=True)
    country_id = Column(Integer, ForeignKey('country.id'), index=True, nullable=True)
    url = Column(String(255), nullable=True, index=True)
    mobile = Column(String(50), nullable=True, index=True)
    phone = Column(String(50), nullable=True, index=True)
    email = Column(String(100), nullable=True, index=True)


class ObjectType(Base):
    __tablename__ = 'object_type'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, index=True)
    table_name = Column(String(50), nullable=False, index=True)
    description = Column(Text, nullable=True)
    created = Column(DateTime, nullable=False, index=True, default=datetime.datetime.utcnow())
    created_by = Column(String(50), nullable=True, index=True)
    modified = Column(DateTime, nullable=True, index=True)
    modified_by = Column(String(50), nullable=True, index=True)


class AttributeDataType(Base):
    __tablename__ = 'attribute_data_type'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, index=True)
    default_format = Column(String(50), nullable=False, index=True)
    created = Column(DateTime, nullable=False, index=True, default=datetime.datetime.utcnow())
    created_by = Column(String(50), nullable=True, index=True)
    modified = Column(DateTime, nullable=True, index=True)
    modified_by = Column(String(50), nullable=True, index=True)


class AttributeCategory(Base):
    __tablename__ = 'attribute_category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, index=True)
    description = Column(Text, nullable=True)
    created = Column(DateTime, nullable=False, index=True, default=datetime.datetime.utcnow())
    created_by = Column(String(50), nullable=True, index=True)
    modified = Column(DateTime, nullable=True, index=True)
    modified_by = Column(String(50), nullable=True, index=True)


class AttributeList(Base):
    __tablename__ = 'attribute_list'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, index=True)
    description = Column(Text, nullable=True)
    created = Column(DateTime, nullable=False, index=True, default=datetime.datetime.utcnow())
    created_by = Column(String(50), nullable=True, index=True)
    modified = Column(DateTime, nullable=True, index=True)
    modified_by = Column(String(50), nullable=True, index=True)


class AttributeListValues(Base):
    __tablename__ = 'attribute_list_values'

    id = Column(Integer, primary_key=True, autoincrement=True)
    list_id = Column(Integer, ForeignKey('attribute_list.id'), index=True, nullable=True)
    name = Column(String(50), nullable=False, index=True)
    value = Column(String(50), nullable=False, index=True)
    description = Column(Text, nullable=True)
    created = Column(DateTime, nullable=False, index=True, default=datetime.datetime.utcnow())
    created_by = Column(String(50), nullable=True, index=True)
    modified = Column(DateTime, nullable=True, index=True)
    modified_by = Column(String(50), nullable=True, index=True)


class Attribute(Base):
    __tablename__ = 'attribute'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, index=True)
    category_id = Column(Integer, ForeignKey('attribute_category.id'), index=True, nullable=False)
    object_type_id = Column(Integer, ForeignKey('object_type.id'), index=True, nullable=False)
    data_type_id = Column(Integer, ForeignKey('attribute_data_type.id'), index=True, nullable=False)
    list_id = Column(Integer, ForeignKey('attribute_list.id'), index=True, nullable=True)
    description = Column(Text, nullable=True)
    created = Column(DateTime, nullable=False, index=True, default=datetime.datetime.utcnow())
    created_by = Column(String(50), nullable=True, index=True)
    modified = Column(DateTime, nullable=True, index=True)
    modified_by = Column(String(50), nullable=True, index=True)


class ContactAttributes(Base):
    __tablename__ = 'contact_attribute'

    id = Column(Integer, primary_key=True, autoincrement=True)
    contact_id = Column(Integer, ForeignKey('contact.id'), index=True, nullable=False)
    category_id = Column(Integer, ForeignKey('attribute.id'), index=True, nullable=False)
    value = Column(String(50), nullable=True, index=True)
    created = Column(DateTime, nullable=False, index=True, default=datetime.datetime.utcnow())
    created_by = Column(String(50), nullable=True, index=True)



if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
