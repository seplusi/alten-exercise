class Age:
    def __init__(self, dict_var):
        self.dict_var = dict_var

    def get_older_person(self):
        items_iter = iter(self.dict_var.items())
        oldest_age = next(items_iter)
        for item in items_iter:
            if item[1] > oldest_age[1]:
                oldest_age = item

        return oldest_age

dict_with_data = {'Luis': 44, 'Pedro': 32, 'Manuel': 45, 'Jona': 12}
age_obj = Age(dict_with_data)

print(age_obj.get_older_person())