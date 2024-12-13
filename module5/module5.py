from time import sleep
import bcrypt

class User:
    """
    Класс пользователя, содержащий атрибуты:
        nickname(имя пользователя, строка),
        password(в хэшированном виде, число),
        age(возраст, число)
    """
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname

    def __contains__(self, item):
        return item == self.nickname
    def __repr__(self):
        return (f'User("{self.nickname}", "{self.password}", "{self.age}")')

    def is_password(self,password):
        return bcrypt.checkpw(password.encode(), self.password)



class Video:
    """
    Класс видео, содержащий атрибуты:
        title(заголовок, строка),
        duration(продолжительность, секунды),
        time_now(секунда остановки (изначально 0)),
        adult_mode(ограничение по возрасту, bool (False по умолчанию))
    """
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __repr__(self):
        return (f'Video("{self.title}","{self.duration}","{self.time_now}","{self.adult_mode}")')

    def __contains__(self, video):
        return video == self.title
    def __eq__(self, other):
        return str(other) == self.title
    def play(self):
        for i in range(1,self.duration+1):
            sleep(1)
            print(i, end=' ')
        print("Конец видео")

class UrTube:
    """
    Класс платформы, содержащий атрибуты:
        users(список объектов User),
        videos(список объектов Video),
        current_user(текущий пользователь, User)
    """
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
        
    def add(self, *videos):
        for v in videos:
            if (str(v) not in self.videos):
                self.videos.append(v)
    def get_videos(self, video):
        l_video = []
        for v in self.videos:
            if video.upper() in str(v).upper():
                l_video.append(str(v))
        return l_video

    def watch_video(self, video):
        b_video = False
        for v in self.videos:
            if video in v:
                b_video = True
                if self.current_user is None:
                    print('Войдите в аккаунт, чтобы смотреть видео')
                    break
                elif v.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    break
# PLAY
                v.play()
                break
        if not b_video:
            print('Видео "', video, '" не найдено')

    def register(self, nickname, password, age,):
        b_user = True
        for u in self.users:
            if nickname in u:
                b_user = False
                print(f'Пользователь {nickname} уже существует')
                break
        if b_user:
            hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            self.users.append(User(nickname, hash, age))
            self.current_user = self.users[-1]

    def log_out(self):
        self.current_user = None

    def log_in(self, nickname, password):
        b_user = False
        for u in self.users:
            if nickname in u:
                b_user =  True
                if u.is_password(password):
                    print("Удачный вход")
                    break
                else:
                    print("Неверный пароль")
                    break
        if not b_user:
            print("Пользователь не зарегистрирован")

if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

# Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')

