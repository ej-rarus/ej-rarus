import random


class LotteryDrawer:
    def __init__(self):
        self.games = 0
        self.numberList = []

    def welcome_user(self):
        print('=' * 15, '로또 번호 추첨기', '=' * 15)

    def input_games(self):
        self.games = int(input("몇 게임을 추첨할까요?: "))
        print("")

    def draw_numbers(self):
        for x in range(self.games):
            numbers = []
            while len(numbers) != 6:
                numbers = [random.randint(1, 45) for y in range(6)]
                numbers = set(numbers)
                numbers = list(numbers)
                numbers.sort()
            self.numberList.append(numbers)

    def print_numbers(self):
        num = 1
        for x in self.numberList:
            if (num % 5) == 0:
                print(f"{num}번째 번호는", x, '\n')
                num += 1
            else:
                print(f"{num}번째 번호는", x)
                num += 1

    def ask_exit(self):
        print('')
        restart = input("번호를 다시 뽑으시겠습니까? (Y/N): ")
        while restart == 'Y' or restart == 'N':
            if restart == 'Y':
                self.numberList = []
                self.run_app()
            elif restart == 'N':
                print("프로그램을 종료합니다.")
                exit()
            else:
                restart = input("다시 입력해주세요. (Y/N): ")

    def run_app(self):
        self.input_games()
        self.draw_numbers()
        self.print_numbers()
        self.ask_exit()


if __name__ == "__main__":
    LD = LotteryDrawer()
    LD.welcome_user()
    LD.run_app()
