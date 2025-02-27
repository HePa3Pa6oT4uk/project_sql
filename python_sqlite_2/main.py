from db.models import User, Profile, Project, Task
from db import Session
import sys
def main():
    '''
    main
    '''
    print("Welcome to the Job System. Type 'help' for available commands.")
    session = Session()
    while True:
        user_input = input("Enter command: ")
        args = user_input.split()

        if not args:
            continue

        match args[0]:
            case 'help':
                print("Доступные команды:")
                print("all_users - выводит список всех пользователей.")
                print("create_user [username] [email] - создает нового пользователя с заданным именем пользователя и электронной почтой.")
                print("update_email [user_id] [new_email] - обновляет электронную почту пользователя с заданным ID.")
                print("delete_user [user_id] - удаляет пользователя по заданному ID.")
                print("all_profiles - выводит список всех профилей.")
                print("create_profile [id] [bio] [phone] - создает новый профиль с заданным ID, био и телефоном.")
                print("update_bio [profile_id] [new_bio] - обновляет био профиля с заданным ID.")
                print("delete_profile [profile_id] - удаляет профиль по заданному ID.")
                print("all_projects - выводит список всех проектов.")
                print("create_project <id> <title> <description> <user1> <user2> ... - Создает новый проект с указанным идентификатором, заголовком, описанием и участниками.")
                print("update_description <project_id> <new_description> - Обновляет описание существующего проекта по идентификатору проекта.")
                print("delete_project <project_id> - Удаляет проект по указанному идентификатору.")
                print("all_tasks - Показывает все задачи с их идентификаторами, заголовками, статусами и идентификаторами проектов.")
                print("create_task <id> <title> <status> <project_id> - Создает новую задачу с указанным идентификатором, заголовком, статусом и идентификатором проекта.")
                print("update_status <task_id> <new_status> - Обновляет статус существующей задачи по ее идентификатору.")
                print("delete_task <task_id> - Удаляет задачу по указанному идентификатору.")
                print("exit - Выход из программы.")
            case 'all_users':
                info = session.query(User).all()
                for i in info:
                    print(i)
            case 'create_user':
                user = User()
                user.username = args[1]
                user.email = args[2]
                session.add(user)
            case 'update_email':
                user = session.query(User).filter_by(id=int(args[1]))
                user.email = args[2]
            case 'delete_user':
                user = session.query(User).filter_by(id=int(args[1]))
                user.delete()
            case 'all_profiles':
                info = session.query(Profile).all()
                print(f"ID: {info[0]}, Bio: {info[1]}, Phone: {info[2]}, User_ID: {info[3:]}")
            case 'create_profile':
                profile = Profile()
                profile.id = args[1]
                profile.bio = args[2]
                profile.phone = args[3]
                session.add(profile)
            case 'update_bio':
                profile = session.query(Profile).filter_by(id=int(args[1]))
                profile.bio = args[2]
            case 'delete_profile':
                profile = session.query(Profile).where(id=int(args[1]))
                profile.delete()
            case 'all_projects':
                info = session.query(Project).all()
                print(f"ID: {info[0]}, Title: {info[1]}, Description: {info[2]}, Users: {info[3:]}")
            case 'create_project':
                project = Project()
                project.id = args[1]
                project.title = args[2]
                project.description = args[3]
                project.users = args[4:]
                session.add(project)
            case 'update_description':
                project = session.query(Project).filter_by(id=int(args[1]))
                project.description = args[2:]
            case 'delete_project':
                project = session.query(Project).filter_by(id=int(args[1]))
                project.delete()
            case 'all_tasks':
                info = session.query(Task).all()
                print(f"ID: {info[0]}, Title: {info[1]}, Status: {info[2]}, Project_ID: {info[3]}")
            case 'create_task':
                task = Task()
                task.id = args[1]
                task.title = args[2]
                task.status = args[3]
                task.project_id = args[4]
                session.add(task)
            case 'update_status':
                task = session.query(Task).filter_by(id=int(args[1]))
                task.status = args[2:]
            case 'delete_task':
                task = session.query(Task).filter_by(id=int(args[1]))
                task.delete()
            case 'exit':
                print("Exiting the program.")
                sys.exit()
        session.commit()

if __name__ == "__main__":
    main()