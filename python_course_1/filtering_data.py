DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
    {
        'name': 'Juancho',
        'age': 16,
        'organization': 'Kiddos',
        'position': 'Frontend Developer',
        'language': 'javascript',
    },
    {
        'name': 'Astrid',
        'age': 17,
        'organization': 'Kiddos',
        'position': 'Backend Developer',
        'language': 'python',
    },
]


def run():

    # Filtering workers using list comprehensions
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']  # (1)
    all_platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']  # (2)
    adults = list(filter(lambda worker: worker['age'] > 18, DATA))  # (3)
    adults_names = list(map(lambda worker: worker['name'], adults))  # (4)
    old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA))  # (5) - With this symbol (|) we can add dictionaries to another dictionary. old_people is a new list with dictionaries with a new key and value added to each dictionary. 
    old_people_selected = list(filter(lambda worker: worker['old'] == True, old_people))  # (6)
    list_old_people = list(map(lambda worker: worker['name'], old_people_selected))  # (7)


    for worker in all_python_devs:  # (1)
        print(worker)
        
    print(':::::::::')

    for worker in all_platzi_workers:  # (2)
        print(worker)    

    print(':::::::::')

    for worker in adults:  # (3)
        print(worker)

    print(':::::::::')

    for worker in adults_names:  # (4)
        print(worker)
    
    print(':::::::::')

    for worker in old_people:  # (5)
        print(worker)

    print(':::::::::')

    for worker in old_people_selected:  # (6)
        print(worker)

    print(':::::::::')

    for worker in list_old_people:  # (7)
        print(worker)


if __name__ == '__main__':
    run()


# These are the outputs of each point (n):


# (1) --> 

# Facundo
# Karo
# Pablo
# Lorena
# Astrid

# (2) --> 

# Facundo
# Héctor
# Gabriel
# Isabella

# (3) --> 

# {'name': 'Facundo', 'age': 72, 'organization': 'Platzi', 'position': 'Technical Coach', 'language': 'python'}
# {'name': 'Luisana', 'age': 33, 'organization': 'Globant', 'position': 'UX Designer', 'language': 'javascript'}
# {'name': 'Héctor', 'age': 19, 'organization': 'Platzi', 'position': 'Associate', 'language': 'ruby'}
# {'name': 'Gabriel', 'age': 20, 'organization': 'Platzi', 'position': 'Associate', 'language': 'javascript'}
# {'name': 'Isabella', 'age': 30, 'organization': 'Platzi', 'position': 'QA Manager', 'language': 'java'}
# {'name': 'Karo', 'age': 23, 'organization': 'Everis', 'position': 'Backend Developer', 'language': 'python'}
# {'name': 'Ariel', 'age': 32, 'organization': 'Rappi', 'position': 'Support', 'language': ''}
# {'name': 'Pablo', 'age': 32, 'organization': 'Master', 'position': 'Human Resources Manager', 'language': 'python'}
# {'name': 'Lorena', 'age': 56, 'organization': 'Python Organization', 'position': 'Language Maker', 'language': 'python'}

# (4) --> 

# Facundo
# Luisana
# Héctor
# Gabriel
# Isabella
# Karo
# Ariel
# Pablo
# Lorena

# (5) -->

# {'name': 'Facundo', 'age': 72, 'organization': 'Platzi', 'position': 'Technical Coach', 'language': 'python', 'old': True}
# {'name': 'Luisana', 'age': 33, 'organization': 'Globant', 'position': 'UX Designer', 'language': 'javascript', 'old': False}
# {'name': 'Héctor', 'age': 19, 'organization': 'Platzi', 'position': 'Associate', 'language': 'ruby', 'old': False}
# {'name': 'Gabriel', 'age': 20, 'organization': 'Platzi', 'position': 'Associate', 'language': 'javascript', 'old': False}
# {'name': 'Isabella', 'age': 30, 'organization': 'Platzi', 'position': 'QA Manager', 'language': 'java', 'old': False}
# {'name': 'Karo', 'age': 23, 'organization': 'Everis', 'position': 'Backend Developer', 'language': 'python', 'old': False}
# {'name': 'Ariel', 'age': 32, 'organization': 'Rappi', 'position': 'Support', 'language': '', 'old': False}
# {'name': 'Juan', 'age': 17, 'organization': '', 'position': 'Student', 'language': 'go', 'old': False}
# {'name': 'Pablo', 'age': 32, 'organization': 'Master', 'position': 'Human Resources Manager', 'language': 'python', 'old': False}
# {'name': 'Lorena', 'age': 56, 'organization': 'Python Organization', 'position': 'Language Maker', 'language': 'python', 'old': False}
# {'name': 'Juancho', 'age': 16, 'organization': 'Kiddos', 'position': 'Frontend Developer', 'language': 'javascript', 'old': False}
# {'name': 'Astrid', 'age': 17, 'organization': 'Kiddos', 'position': 'Backend Developer', 'language': 'python', 'old': False}

# (6) -->

# {'name': 'Facundo', 'age': 72, 'organization': 'Platzi', 'position': 'Technical Coach', 'language': 'python', 'old': True}

# (7) -->

# Facundo