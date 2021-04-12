from enum import IntEnum

LOCATION_TYPE_CHOICES = [
    (1, 'Country'),
    (2, 'City'),
    (3, 'Area'),
    (4, 'Thana'),
    (5, 'Postcode'),
    (6, 'PostOffice'),
    (7, 'Division')
]


class GENDER(IntEnum):
    MALE = 0
    FEMALE = 1
    OTHER = 2

    @classmethod
    def get_choices(cls):
        return [(key.value, key.name) for key in cls]


class DeliveryStatus(IntEnum):
    PROGRESS = 0
    ONGOING = 1
    FAILED = 2
    DONE = 3

    @classmethod
    def get_choices(cls):
        return [(key.value, key.name) for key in cls]
