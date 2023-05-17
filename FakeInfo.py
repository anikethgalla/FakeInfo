from faker import Faker

fake=Faker()
for i in range(10):
 namely=(fake.name())
 print(namely)
 print(namely+"@"+fake.domain_name())
 print(fake.address())
 print(fake.country())
 print(fake.url())
 print()
 #fake=Faker("hi_IN")
 #print(fake.name())
