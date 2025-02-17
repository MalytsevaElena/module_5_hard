import time

class User:
    def __init__(self, nickname,  password, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __eq__(self, other):
        return other.nickname == self.nickname

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, adult_mode= False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = 0

    def __repr__(self):
        return self.title

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname: str,  password: int, age: int):
        new_user = User(nickname, password, age)
        if new_user in self.users:
            print(f'"Пользователь {nickname} уже существует"')
        else:
            self.users.append(new_user)
            self.current_user = new_user

    def log_in(self, nickname: str,  password: int):
        for user in self.users:
            if (nickname, password) == (user.nickname, user.password):
                self.current_user = user
                return user

    def log_out(self):
        current_user = None

    def add(self, *video: Video):
        for vid in video:
            if vid.title not in self.videos:
                self.videos.append(vid)

    def get_videos(self, str_):
        titles = []
        for video in self.videos:
            if str_.lower() in str(video).lower():
                titles.append(video)
        return titles

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if title == video.title:
                if video.adult_mode and self.current_user.age >= 18:
                    while video.time_now < video.duration:
                        video.time_now += 1
                        print(video.time_now, end=' ')
                        time.sleep(1)
                    video.time_now = 0
                    print("Конец видео")
                else:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    break

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









