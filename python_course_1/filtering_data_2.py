DATA = [
    {
        'name': 'Juan',
        'age': 25,
        'country': 'Colombia',
        'occupation': 'Backend Developer',
        'nat_language': 'spanish',
    },
    {
        'name': 'Zuri',
        'age': 23,
        'country': 'Colombia',
        'occupation': 'Frontend Developer',
        'nat_language': 'spanish',
    },
    {
        'name': 'Astrid',
        'age': 18,
        'country': 'Norway',
        'occupation': 'Backend Developer',
        'nat_language': 'norwegian',
    },
    {
        'name': 'Karoline',
        'age': 17,
        'country': 'Denmark',
        'occupation': 'UX Designer',
        'nat_language': 'danish',
    },
    {
        'name': 'Anders',
        'age': 26,
        'country': 'Sweden',
        'occupation': 'Frontend Developer',
        'nat_language': 'swedish',
    },
    {
        'name': 'Jim',
        'age': 32,
        'country': 'United States',
        'occupation': 'Frontend Developer',
        'nat_language': 'english',
    },
    {
        'name': 'Julia',
        'age': 66,
        'country': 'United Kingdom',
        'occupation': 'Human Resources Manager',
        'nat_language': 'english',
    },
    {
        'name': 'Luis',
        'age': 59,
        'country': 'Mexico',
        'occupation': 'Support',
        'nat_language': 'spanish',
    },
    {
        'name': 'Valentina',
        'age': 35,
        'country': 'Venezuela',
        'occupation': 'Technical Coach',
        'nat_language': 'spanish',
    },
    {
        'name': 'Madhur',
        'age': 29,
        'country': 'India',
        'occupation': 'Associate',
        'nat_language': 'hindi',
    },
    {
        'name': 'Logan',
        'age': 31,
        'country': 'Canada',
        'occupation': 'Associate',
        'nat_language': 'english',
    },
    {
        'name': 'Antonella',
        'age': 24,
        'country': 'Argentina',
        'occupation': 'Human Resources Manager',
        'nat_language': 'spanish',
    },
    {
        'name': 'Polina',
        'age': 33,
        'country': 'Ukraine',
        'occupation': 'QA Manager',
        'nat_language': 'ukrainian',
    },
    {
        'name': 'Urassaya',
        'age': 30,
        'country': 'Thailand',
        'occupation': 'QA Manager',
        'nat_language': 'thai',
    },
    {
        'name': 'Irina',
        'age': 26,
        'country': 'Ukraine',
        'occupation': 'Technical Coach',
        'nat_language': 'ukrainian',
    },
    {
        'name': 'Miguel',
        'age': 16,
        'country': 'Costa Rica',
        'occupation': 'Student',
        'nat_language': 'spanish',
    },
    {
        'name': 'Martina',
        'age': 19,
        'country': 'Argentina',
        'occupation': 'Backend Developer',
        'nat_language': 'spanish',
    },
    {
        'name': 'Lars',
        'age': 27,
        'country': 'Norway',
        'occupation': 'Frontend Developer',
        'nat_language': 'norwegian',
    },
    {
        'name': 'Eloïse',
        'age': 21,
        'country': 'France',
        'occupation': 'UX Designer',
        'nat_language': 'french',
    },
    {
        'name': 'Henry',
        'age': 42,
        'country': 'Canada',
        'occupation': 'Support',
        'nat_language': 'french',
    },
    {
        'name': 'Maria',
        'age': 25,
        'country': 'Russia',
        'occupation': 'UX Designer',
        'nat_language': 'russian',
    },
    {
        'name': 'Karl',
        'age': 32,
        'country': 'Germany',
        'occupation': 'Technical Coach',
        'nat_language': 'german',
    },
]


def run():
    
    # Filtering by native language:

    # List comprehensions:
    spanish_speakers = [worker['name'] for worker in DATA if worker['nat_language'] == 'spanish']  # (1)

    # Filter, map:
    filter_english_speakers = list(filter(lambda worker: worker['nat_language'] == 'english', DATA))  # (2)

    english_speakers = list(map(lambda worker: worker['name'], filter_english_speakers))  # (3)

    # Filtering by country

    filter_norwegians = list(filter(lambda worker: worker['country'] == 'Norway', DATA))  # (4)

    norwegians = list(map(lambda worker: worker['name'], filter_norwegians))  # (5)

    # Filtering by age

    underage = [worker['name'] for worker in DATA if worker['age'] < 18]  # (6)

    youngsters = [worker['name'] for worker in DATA if worker['age'] <= 25]  # (7)

    key_old_added = list(map(lambda worker: worker | {'old': worker['age'] >= 65}, DATA))  # (8)

    filter_old_people = list(filter(lambda worker: worker['age'] >= 65, key_old_added))  # (9)

    old_people = list(map(lambda worker: worker['name'], filter_old_people))  # (10)

    # Filtering by occupation

    filter_backend_devs = list(filter(lambda worker: worker['occupation'] == 'Backend Developer', DATA))  # (11)

    backend_devs = list(map(lambda worker: worker['name'], filter_backend_devs))  # (12)

    frontend_devs = [worker['name'] for worker in DATA if worker['occupation'] == 'Frontend Developer']  # (13)

    all_people = list(map(lambda worker: worker['name'], DATA))  # (14)


    for worker in spanish_speakers:  # (1)
        print(worker)

    print(':::::::::::')

    for worker_dict in filter_english_speakers:  # (2)
        print(worker_dict)

    print(':::::::::::')

    for worker in english_speakers:  # (3)
        print(worker)

    print(':::::::::::')

    for worker_dict in filter_norwegians:  # (3)
        print(worker_dict)

    print(':::::::::::')

    for worker_dict in filter_norwegians:  # (4)
        print(worker_dict)

    print(':::::::::::')

    for worker in norwegians:  # (5)
        print(worker)

    print(':::::::::::')

    for worker in underage:  # (6)
        print(worker)

    print(':::::::::::')

    for worker in youngsters:  # (7)
        print(worker)

    print(':::::::::::')

    for worker_dict in key_old_added:  # (8)
        print(worker_dict)

    print(':::::::::::')

    for worker_dict in filter_old_people:  # (9)
        print(worker_dict)

    print(':::::::::::')

    for worker in old_people:  # (10)
        print(worker)

    print(':::::::::::')

    for worker_dict in filter_backend_devs:  # (11)
        print(worker_dict)

    print(':::::::::::')

    for worker in backend_devs:  # (12)
        print(worker)

    print(':::::::::::')

    for worker in frontend_devs:  # (13)
        print(worker)

    print(':::::::::::')

    for worker in all_people:  # (14)
        print(worker)


if __name__ == '__main__':
    run()


# These are the outputs:


# (1) -->

# Juan
# Zuri
# Luis
# Valentina
# Antonella
# Miguel
# Martina

# (2) -->

# {'name': 'Jim', 'age': 32, 'country': 'United States', 'occupation': 'Frontend Developer', 'nat_language': 'english'}
# {'name': 'Julia', 'age': 66, 'country': 'United Kingdom', 'occupation': 'Human Resources Manager', 'nat_language': 'english'}
# {'name': 'Logan', 'age': 31, 'country': 'Canada', 'occupation': 'Associate', 'nat_language': 'english'}

# (3) -->

# Jim
# Julia
# Logan

# (4) -->

# {'name': 'Astrid', 'age': 18, 'country': 'Norway', 'occupation': 'Backend Developer', 'nat_language': 'norwegian'}
# {'name': 'Lars', 'age': 27, 'country': 'Norway', 'occupation': 'Frontend Developer', 'nat_language': 'norwegian'}

# (5) -->

# Astrid
# Lars

# (6) -->

# Karoline
# Miguel

# (7) -->

# Juan
# Zuri
# Astrid
# Karoline
# Antonella
# Miguel
# Martina
# Eloïse
# Maria

# (8) -->

# {'name': 'Juan', 'age': 25, 'country': 'Colombia', 'occupation': 'Backend Developer', 'nat_language': 'spanish', 'old': False}
# {'name': 'Zuri', 'age': 23, 'country': 'Colombia', 'occupation': 'Frontend Developer', 'nat_language': 'spanish', 'old': False}
# {'name': 'Astrid', 'age': 18, 'country': 'Norway', 'occupation': 'Backend Developer', 'nat_language': 'norwegian', 'old': False}
# {'name': 'Karoline', 'age': 17, 'country': 'Denmark', 'occupation': 'UX Designer', 'nat_language': 'danish', 'old': False}
# {'name': 'Anders', 'age': 26, 'country': 'Sweden', 'occupation': 'Frontend Developer', 'nat_language': 'swedish', 'old': False}
# {'name': 'Jim', 'age': 32, 'country': 'United States', 'occupation': 'Frontend Developer', 'nat_language': 'english', 'old': False}
# {'name': 'Julia', 'age': 66, 'country': 'United Kingdom', 'occupation': 'Human Resources Manager', 'nat_language': 'english', 'old': True}
# {'name': 'Luis', 'age': 59, 'country': 'Mexico', 'occupation': 'Support', 'nat_language': 'spanish', 'old': False}
# {'name': 'Valentina', 'age': 35, 'country': 'Venezuela', 'occupation': 'Technical Coach', 'nat_language': 'spanish', 'old': False}
# {'name': 'Madhur', 'age': 29, 'country': 'India', 'occupation': 'Associate', 'nat_language': 'hindi', 'old': False}
# {'name': 'Logan', 'age': 31, 'country': 'Canada', 'occupation': 'Associate', 'nat_language': 'english', 'old': False}
# {'name': 'Antonella', 'age': 24, 'country': 'Argentina', 'occupation': 'Human Resources Manager', 'nat_language': 'spanish', 'old': False}
# {'name': 'Polina', 'age': 33, 'country': 'Ukraine', 'occupation': 'QA Manager', 'nat_language': 'ukrainian', 'old': False}
# {'name': 'Urassaya', 'age': 30, 'country': 'Thailand', 'occupation': 'QA Manager', 'nat_language': 'thai', 'old': False}
# {'name': 'Irina', 'age': 26, 'country': 'Ukraine', 'occupation': 'Technical Coach', 'nat_language': 'ukrainian', 'old': False}
# {'name': 'Miguel', 'age': 16, 'country': 'Costa Rica', 'occupation': 'Student', 'nat_language': 'spanish', 'old': False}
# {'name': 'Martina', 'age': 19, 'country': 'Argentina', 'occupation': 'Backend Developer', 'nat_language': 'spanish', 'old': False}
# {'name': 'Lars', 'age': 27, 'country': 'Norway', 'occupation': 'Frontend Developer', 'nat_language': 'norwegian', 'old': False}
# {'name': 'Eloïse', 'age': 21, 'country': 'France', 'occupation': 'UX Designer', 'nat_language': 'french', 'old': False}
# {'name': 'Henry', 'age': 42, 'country': 'Canada', 'occupation': 'Support', 'nat_language': 'french', 'old': False}
# {'name': 'Maria', 'age': 25, 'country': 'Russia', 'occupation': 'UX Designer', 'nat_language': 'russian', 'old': False}
# {'name': 'Karl', 'age': 32, 'country': 'Germany', 'occupation': 'Technical Coach', 'nat_language': 'german', 'old': False}

# (9) -->

# {'name': 'Julia', 'age': 66, 'country': 'United Kingdom', 'occupation': 'Human Resources Manager', 'nat_language': 'english', 'old': True}

# (10) -->

# Julia

# (11) -->

# {'name': 'Juan', 'age': 25, 'country': 'Colombia', 'occupation': 'Backend Developer', 'nat_language': 'spanish'}
# {'name': 'Astrid', 'age': 18, 'country': 'Norway', 'occupation': 'Backend Developer', 'nat_language': 'norwegian'}
# {'name': 'Martina', 'age': 19, 'country': 'Argentina', 'occupation': 'Backend Developer', 'nat_language': 'spanish'}

# (12) -->

# Juan
# Astrid
# Martina

# (13) -->

# Zuri
# Anders
# Jim
# Lars

# (14) -->

# Juan
# Zuri
# Astrid
# Karoline
# Anders
# Jim
# Julia
# Luis
# Valentina
# Madhur
# Logan
# Antonella
# Polina
# Urassaya
# Irina
# Miguel
# Martina
# Lars
# Eloïse
# Henry
# Maria
# Karl