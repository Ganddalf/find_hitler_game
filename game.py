from flask import render_template
import random, wikipedia


class Level:
    counter_ID = 0

    def __init__(self, width=6, height=6, page="Википедия",
                 final_page="Гитлер, Адольф"):
        self.ID = Level.counter_ID
        Level.counter_ID += 1
        self.start_page_name = page
        self.final_page = final_page
        self.width = width
        self.height = height

        self.prev_page_name = ""
        self.page_name = ""
        self.prev_table = []
        self.table = []

        self.step = 0

    def show_state(self):
        return render_template('game.html', table=self.table,
                               page_name=self.page_name,
                               page_link=wikipedia.page(self.page_name).url,
                               step=self.step)

    def set_table(self):
        links = wikipedia.page(self.page_name).links
        random.shuffle(links)

        if self.final_page in links:
            links.remove(self.final_page)
            links[0] = self.final_page

        links = links[:self.width * self.height]
        links = list(sorted(links))

        self.table.clear()
        for i in range(self.height):
            self.table.append(links[self.width * i: self.width * (i + 1)])

    def next_state(self, page_name):
        self.step += 1

        self.prev_page_name = self.page_name
        self.page_name = page_name
        self.prev_table = self.table

        self.set_table()

        return self.show_state()

    def prev_state(self):
        self.step -= 1

        self.page_name = self.prev_page_name
        self.table = self.prev_table

        self.set_table()

        return self.show_state()

    def start_level(self):
        return self.next_state(self.start_page_name)


class Game:
    def __init__(self):
        wikipedia.set_lang("ru")
        self.current_level = None
        self.levels = []
        self.__init_levels__()

    def __init_levels__(self):
        self.levels.append(Level(3, 3, "Германия"))
        self.levels.append(Level(3, 3, "Пропаганда"))
        self.levels.append(Level(3, 3, "Право"))
        self.levels.append(Level(3, 3, "Rammstein"))
        self.levels.append(Level(3, 3, "Москва"))
        self.levels.append(Level(3, 3, "Олимпийские игры"))

        self.levels.append(Level(3, 3, "Мясо"))
        self.levels.append(Level(3, 3, "Шахматы"))
        self.levels.append(Level(3, 3, "Любовь"))
        self.levels.append(Level(3, 3, "Искусство"))
        self.levels.append(Level(3, 3, "Библия"))
        self.levels.append(Level(3, 3, "Биметалл"))

        self.levels.append(Level(3, 3, "Йога"))
        self.levels.append(Level(3, 3, "Числитель"))
        self.levels.append(Level(3, 3, "Деепричастие"))
        self.levels.append(Level(3, 3, "Коронавирусы"))
        self.levels.append(Level(3, 3, "Система управления версиями"))
        self.levels.append(Level(3, 3, "Люминисценция"))

        self.easy_medium = 6
        self.medium_hard = 12

    def start_level(self, num=0):
        self.current_level = num
        return self.levels[num].start_level()

    def next_level_state(self, page_name):
        return self.levels[ self.current_level ].next_state(page_name)

    def check_win(self, page):
        return self.levels[self.current_level].final_page == page

    def set_levels(self):
        level_names = [x.start_page_name for x in self.levels]

        easy_levels = zip(range(self.easy_medium),
                          level_names[0 : self.easy_medium])
        medium_levels = zip(range(self.easy_medium, self.medium_hard),
                            level_names[self.easy_medium : self.medium_hard])
        hard_levels = zip(range(self.medium_hard, len(self.levels)),
                          level_names[self.medium_hard : len(self.levels)])

        return render_template('select_level.html', easy_levels=easy_levels,
                               medium_levels=medium_levels,
                               hard_levels=hard_levels)

    def get_win_message(self):
        level = self.levels[self.current_level]
        start = level.start_page_name
        end = level.final_page
        steps = level.step

        return "Поздравляем, вы прошли от \'{}\' до \'{}\' " \
               "за переходов по ссылкам: {}".format(start, end, steps)

    def clear(self):
        self.current_level = None
        self.levels = []
        self.__init_levels__()
