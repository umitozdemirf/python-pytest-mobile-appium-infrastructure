from faker import Faker


class DataGenerator:
    @staticmethod
    def generate_random_string():
        return Faker().domain_word()

    @staticmethod
    def generate_random_integer(min_int, max_int):
        return Faker().random.randint(min_int, max_int)

    @staticmethod
    def generate_email():
        return Faker().email()

    @staticmethod
    def generate_special_character_email():
        return f'#$#½£@{Faker().domain_name()}'
