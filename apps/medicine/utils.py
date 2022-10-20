
class MedicineStatus:
    need_take = 'need take'
    taken = 'taken'

    @classmethod
    def choice(cls) -> tuple[tuple, ...]:
        return (
            ('need_take', cls.need_take),
            ('taken', cls.taken),
        )
