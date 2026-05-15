# Домашнее задание №5 Тема: Декораторы в Python
import time
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

def is_admin_decorator(funk):
    def wrapper(user):
        if user.role == 'admin':
            funk(user)
        else:
            print('У вас нет доступа')
    return wrapper

@is_admin_decorator
def delete_video(user):
    print('Видео удалено')


admin = User("Ardager", "admin")
user = User("Bek", "user")

delete_video(admin)
delete_video(user)

def timer_decorator(funk):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = funk(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения: {end_time - start_time:.1f} секунд")
        return result
    return wrapper

@timer_decorator
def download_video():
    time.sleep(2)
    print("Видео загружено")

download_video()

