from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    # app.run()


def test():
    session = db_session.create_session()

    user = User()
    user.name = 'Ridley'
    user.surname = 'Scott'
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'
    session.add(user)

    user = User()
    user.name = 'Tom'
    user.surname = 'Canon'
    user.age = 24
    user.position = 'driver'
    user.speciality = 'technical engineer'
    user.address = 'module_2'
    user.email = 'tom_driver@mars.org'
    session.add(user)

    user = User()
    user.name = 'Max'
    user.surname = 'Carricker'
    user.age = 28
    user.position = 'medic'
    user.speciality = 'biologist'
    user.address = 'module_3'
    user.email = 'max_medic@mars.org'
    session.add(user)

    session.commit()

if __name__ == '__main__':
    main()
    test()
