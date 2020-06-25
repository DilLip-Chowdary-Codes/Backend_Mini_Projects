import factory
import datetime
from project_management_portal import models

# class UserFactory(factory.Factory):
#     class Meta:
#         model = models.User

#     username = "John"

# UserFactory()
# UserFactory()
# UserFactory()

# class RentalFactory(factory.Factory):
#     class Meta:
#         model = models.User
#     from factory import fuzzy, LazyAttribute
#     username = fuzzy.FuzzyDate(start_date=datetime.date(2000, 1, 1))
#     phone_no = LazyAttribute(lambda o: o.begin + o.duration)

#     class Params:
#         duration = 12

# class UserFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = models.User

#     username = "John Doe"

# class GroupFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = models.Group

#     name = "Admins"

# class GroupLevelFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = models.GroupLevel

#     user = factory.SubFactory(UserFactory)
#     group = factory.SubFactory(GroupFactory)
#     rank = 1

# class UserWithGroupFactory(UserFactory):
#     membership = factory.RelatedFactory(GroupLevelFactory, 'user')

# class UserWith2GroupsFactory(UserFactory):
#     membership1 = factory.RelatedFactory(GroupLevelFactory, 'user', group__name='Group1')
#     membership2 = factory.RelatedFactory(GroupLevelFactory, 'user', group__name='Group2')

class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Country

    name = factory.Iterator(["France", "Italy", "Spain"])
    lang = factory.Iterator(['fr', 'it', 'es'])

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User

    name = factory.Faker('name')
    lang = factory.SelfAttribute('country.lang')
    country = factory.SubFactory(CountryFactory)

class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Company

    name = "ACME, Inc."
    country = factory.SubFactory(CountryFactory)
    # owner = factory.SubFactory(UserFactory, country=country)
    # owner = factory.SubFactory(UserFactory, country=factory.SelfAttribute('country'))
    owner = factory.SubFactory(UserFactory(username=factory.Faker('name'), country=country))

    # owner = factory.SubFactory(
    #     UserFactory,country=factory.LazyAttribute())

# class PostFactor(factory.django.DjangoModelFactory):

#     class Meta:
#         model = models.Post
#     title = factory.Faker('name')
#     posted_by = factory.SubFactory(
#         UserFactory, username = factory.SelfAttribute('..title'))

# ouput : username = given_name in input

# class PostFactor(factory.django.DjangoModelFactory):

#     class Meta:
#         model = models.Post
#     title = factory.Faker('name')
#     posted_by = factory.SubFactory(
#         UserFactory, name = factory.SelfAttribute('..title'))

# class PostFactor(factory.django.DjangoModelFactory):

#     class Meta:
#         model = models.Post
#     title = factory.Faker('name')
#     posted_by = factory.SubFactory(
#         UserFactory, name = factory.LazyAttribute(lambda obj: obj.factory_parent.title))
class PostFactor(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Post
    title = factory.Faker('name')
    posted_by = factory.SubFactory(
        UserFactory, name = factory.LazyAttribute(lambda obj: f'author for {obj.factory_parent.title}'))
