class Dmytro:
    def __init__(self, first_name=None, last_name=None, birth_year=None):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    def calculate_course(self):

        if self.birth_year is None:
            return None
        current_year = 2025
        age = current_year - self.birth_year
        if 17 <= age <= 21:
            return age - 15
        return None

    def get_name_list(self):

        return [self.first_name, self.last_name]


student = Dmytro("Дмитро", "Цьопич", 2008)
print(student.calculate_course())
print(student.get_name_list())
