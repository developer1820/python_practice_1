class Employee:
    """ This class contains information about employee."""
    company_name = "ABC group"

    def __init__(self, name, id):
        self.employee_name = name
        self.employee_id = id
        self.task_assign = 15

    def decide_level(self, level):
        levels = {"A": "Director",
                  "B": "Architect",
                  "C": "senior",
                  "D": "Junior"}
        self.employee_level = levels[level]

    def employee_details(self, job_title, position, salary):
        print(f"""Hello {self.employee_name} here is your employee information,
                  You are working at {Employee.company_name},
                  Your employee id is {self.employee_id},
                  Your job title is {job_title},
                  You are working at {self.employee_level} level,
                  Your salary is {salary},
                  And {self.task_assign} task were assign to you.
                  """)

    def best_employee(self, task_completed, num_sick_leaves):
        self.task_completed = task_completed
        # print(self.task_completed)
        self.num_sick_leaves = num_sick_leaves
        # print(self.num_sick_leaves)
        if self.task_assign == int(task_completed) and num_sick_leaves == 0:
            print()
            print("You are the Best employee of the year".upper())
            print()
        else:
            print("Sorry, you are not employee of the year!" +
                  "Try hard next time!!")

    def employee_bonus(self):
        if self.task_completed == 15 and self.num_sick_leaves == 0:
            print("You are eligible for the bonus of £1000.")
        elif self.task_completed >= 10 and self.num_sick_leaves <= 5:
            print("You are eligible for the bonus of £500.")
        elif self.task_completed >= 7 and self.num_sick_leaves <= 10:
            print("You are eligible for the bonus of £200.")
        elif self.task_completed >= 5 and self.num_sick_leaves <= 15:
            print("You are eligible for the bonus of £100.")
        else:
            print("Sorry, you are not eligible for bonus.")


name_employee1 = input("What is your name?:")
id_employee1 = int(input("What is your id number?:"))
levels_employee1 = input("What level are you in? \
please select from(A, B, C, D):")
employee1 = Employee(name_employee1, id_employee1)
employee1.decide_level(levels_employee1)
employee1.employee_details("Software Engineer", "Junior Level", 2000)
task_employee1 = int(input("How many tasks have you completed?:"))
sick_leave_employee1 = int(input("For how many days were you off sick?:"))
employee1.best_employee(task_employee1, sick_leave_employee1)
print("Let's find out how much bonus you can get")
employee1.employee_bonus()
