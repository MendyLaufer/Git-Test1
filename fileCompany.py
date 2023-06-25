class Company:
    def __init__(self, ceo_name, cto_name, cfo_name, hubs_list, employees_list):
        self.ceo_name = ceo_name
        self.cto_name = cto_name
        self.cfo_name = cfo_name
        self.hubs_list = hubs_list
        self.employees_list = employees_list

    def setCeo_name(self, ceo_name):
        self.ceo_name = ceo_name

    def setCto_name(self, cto_name):
        self.cto_name = cto_name

    def setCfo_name(self, cfo_name):
        self.cfo_name = cfo_name

    def addHubs_list(self, hubs):
        self.hubs_list.extend(hubs)

    def addEmployees_list(self, employees):
        self.employees_list.extend(employees)

    def gEmployees_sum(self):
        return len(self.employees_list)