import common
import common.validators as validators
import common.models as models


common.validators.is_boolean('true')
common.validators.is_json('{}')
common.validators.is_date('2020-01-01')

john_post = models.Post()
john_posts = models.Posts()
john = models.User()

print(type(john))

print('\n\n***** self *****')
for k in dict(globals()).keys():
    print(k)


print('\n\n***** common *****')
for k in common.__dict__.keys():
    print(k)


print('\n\n***** models *****')
for k in common.models.__dict__.keys():
    print(k)
