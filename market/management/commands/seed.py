import random
import string
import time

import faker
from django.core.management import BaseCommand

from core.models import User
from market.models import Product, ProductCategory, ProductStatus
from market.models.product_provider import ProductProvider


class Command(BaseCommand):
    def __init__(self, stdout=None, stderr=None, no_color=False, force_color=False):
        super().__init__(stdout, stderr, no_color, force_color)
        self.faker = faker.Faker()

    def handle(self, *args, **options):
        self.seed_products_statuses()
        self.seed_users()
        self.seed_products_categories()
        self.seed_products_owners()
        self.seed_products()

    def seed_users(self):
        self.stdout.write("Users seeding has started.")
        users_count = 123

        for _ in range(users_count):
            profile = self.faker.profile()
            print(profile)
            username = profile["username"]
            email = profile["mail"]

            letters = string.ascii_lowercase
            password = "".join(random.choice(letters) for _ in range(12))

            User.objects.create_user(username, email, password)

        self.stdout.write("Users seeding has finished.")

    def seed_products(self):
        self.stdout.write("Products seeding has started.")
        start = time.time()

        products_count = 1000

        for _ in range(products_count):
            batch = list()

            for _ in range(10):
                title = self.faker.word()
                description = self.faker.paragraph(nb_sentences=3)
                price = random.uniform(3, 1000)
                status = ProductStatus.objects.get(name="active")

                product_owners_count = ProductProvider.objects.count()
                owner = ProductProvider.objects.get(id=random.uniform(1, product_owners_count))

                categories_count = ProductCategory.objects.count()
                category = ProductCategory.objects.get(id=random.uniform(1, categories_count))

                batch.append(
                    Product(
                        title=title,
                        description=description,
                        price=price,
                        status_id=status.id,
                        owner_id=owner.id,
                        category_id=category.id,
                    )
                )

            Product.objects.bulk_create(batch)
        end = time.time()

        self.stdout.write("Products seeding has finished.")
        self.stdout.write(f"Completed in {end - start}")

    def seed_products_categories(self):
        self.stdout.write("Products categories seeding has started.")
        name = self.faker.color_name()
        ProductCategory.objects.create(name=name)
        self.stdout.write("Products categories seeding has finished.")

    def seed_products_statuses(self) -> None:
        self.stdout.write("Products statuses seeding has started.")
        statuses = ["pending", "inactive", "active"]

        for idx, status in enumerate(statuses):
            ProductStatus.objects.create(id=idx + 1, name=status)

        self.stdout.write("Products statuses seeding has finished.")

    def seed_products_owners(self):
        self.stdout.write("Products owners seeding has started.")
        users = User.objects.all()
        for user in users:
            description = self.faker.paragraph(nb_sentences=5)
            phone = self.faker.phone_number()
            ProductProvider.objects.create(description=description, phone=phone, user_id=user.id)
        self.stdout.write("Products owners seeding has finished.")
