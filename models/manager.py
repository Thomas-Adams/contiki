import datetime

from models.models import engine, User, Role, Permission, UserRoles, RolePermissions, Gender, Salutation, Country, \
    Profile, AddressType, ContactGroup, Contact, Address, ObjectType, AttributeCategory, AttributeDataType, \
    AttributeList, \
    AttributeListValues, ContactAttributes
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
import unittest

session_factory = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = session_factory()
    session.begin(subtransactions=True)
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


class Manager(object):
    meta = None

    def __init__(self, meta):
        self.meta = meta

    def create(self, **kwargs):
        self.instance = self.meta()
        for k, v in kwargs.items():
            setattr(self.instance, k, v)

        with session_scope() as session:
            session.add(self.instance)
            session.commit()

        return self.instance

    def update(self, entity, **kwargs):
        for k, v in kwargs.items():
            setattr(entity, k, v)

        with session_scope() as session:
            session.add(entity)

        return entity

    def delete(self, entity):
        with session_scope() as session:
            session.delete(entity)


class UserManager(Manager):

    def __init__(self):
        super(UserManager, self).__init__(User)


class RoleManager(Manager):

    def __init__(self):
        super(RoleManager, self).__init__(Role)


class PermissionManager(Manager):

    def __init__(self):
        super(PermissionManager, self).__init__(Permission)


class UserRolesManager(Manager):

    def __init__(self):
        super(UserRolesManager, self).__init__(UserRoles)


class RolePermissionsManager(Manager):

    def __init__(self):
        super(RolePermissionsManager, self).__init__(RolePermissions)


class GenderManager(Manager):

    def __init__(self):
        super(GenderManager, self).__init__(Gender)


class SalutationManager(Manager):

    def __init__(self):
        super(SalutationManager, self).__init__(Salutation)


class CountryManager(Manager):

    def __init__(self):
        super(CountryManager, self).__init__(Country)


class ProfileManager(Manager):

    def __init__(self):
        super(ProfileManager, self).__init__(Profile)


class AddressTypeManager(Manager):

    def __init__(self):
        super(AddressTypeManager, self).__init__(AddressType)


class ContactGroupManager(Manager):

    def __init__(self):
        super(ContactGroupManager, self).__init__(ContactGroup)


class ContactManager(Manager):

    def __init__(self):
        super(ContactManager, self).__init__(Contact)


class AddressManager(Manager):

    def __init__(self):
        super(AddressManager, self).__init__(Address)


class ObjectTypeManager(Manager):

    def __init__(self):
        super(ObjectTypeManager, self).__init__(ObjectType)


class AttributeDataTypeManager(Manager):

    def __init__(self):
        super(AttributeDataTypeManager, self).__init__(AttributeDataType)


class AttributeCategoryManager(Manager):

    def __init__(self):
        super(AttributeCategoryManager, self).__init__(AttributeCategory)


class AttributeListManager(Manager):

    def __init__(self):
        super(AttributeListManager, self).__init__(AttributeList)


class AttributeListValuesManager(Manager):

    def __init__(self):
        super(AttributeListValuesManager, self).__init__(AttributeListValues)


class ContactAttributesManager(Manager):

    def __init__(self):
        super(ContactAttributesManager, self).__init__(ContactAttributes)


class TestManager(unittest.TestCase):

    def test_manager(self):
        manager = Manager(User)

        user = manager.create(user_name='tadams', password='tadams', email='tadams@enargit.org',
                              enabled=True, locked=False, expired=False, credentials_expired=False,
                              created=datetime.datetime.utcnow())
        print(user)
        self.assertIsNotNone(user)

    def test_user_manager(self):
        manager = UserManager()
        user = manager.create(user_name='tadams2', password='tadams2', email='tadams@enargit.org',
                              enabled=True, locked=False, expired=False, credentials_expired=False,
                              created=datetime.datetime.utcnow())
        print(user)
        self.assertIsNotNone(user)


if __name__ == '__main__':
    unittest.main()
