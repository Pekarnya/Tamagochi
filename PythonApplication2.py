

from ast import Continue, main
from warnings import WarningMessage
from random import randrange
import test_player as player
from os import name
from abc import ABC, abstractmethod


class Cat_Director:
    __builder = None
    def set_builder(self, builder):
        self.__builder = builder


    def get_cat (self):
        cat = Cat()

        #Имя

        name = self.__builder.get_name()
        cat.set_name(name)

        #Тело и его состояние

        
        body = self.__builder.get_body()
        cat.set_body(body)

        #Здоровье

        health = self.__builder.get_health()
        cat.set_health(health)

        #Настроение

        mood = self.__builder.get_mood()
        cat.set_mood(mood)

        #Голод

        hungry = self.__builder.get_hungry()
        cat.set_hungry(hungry)

        #Усталость

        tireLvl = self.__builder.get_tireLvl()
        cat.set_tireLvl(tireLvl)

        #Лапки


        paws = self.__builder.get_paws()
        cat.attach_paws(paws)

        return cat

    #Персонаж

class Cat:
    def __init__(self):
        self.__paws = str
        self.__mood = None
        self.__body = None
        self.__health = int
        self.__tireLvl = int
        self.__hungry = int
        self.__name = str

    def set_name (self, name):
        self.__name = name

    def set_body (self, body):
        self.__body = body

    def attach_paws (self, paws):
        self.__paws = paws

    def set_health(self, health):
        self.__health = health

    def set_mood (self, mood):
        self.__mood = mood

    def set_hungry (self, hungry):
        self.__hungry = hungry

    def set_tireLvl (self, tireLvl):
        self.__tireLvl = tireLvl

    def cat_status (self):

        print ("Имя вашего питомца: % s " % self.__name.nick_name)

        #Здоровье тела производная случайных событий * голод

        print ("Состояние здоровья тела: % s " % self.__body.desiese) #Не забыть описать

        #Голод как производная времени + 10% времени проведенного на улице

        print ("Уровень голода: % s " % self.__hungry.hungry_lvl)

        print ("Количество HP: % d " % self.__health.HP) #Хп как производная здоровья тела

        # Настроение как производная ХП и последних событий + 10% усталости + 5% времени проведенного дома без игры +10% уровня голода

        print ("Настроение: % s " % self.__mood.lvl_mood)


        #Усталость производная времени без сна + 10 % времени проведенного на улице

        print ("Уровень усталости: % s " % self.__tireLvl.tirenes)

        # Одежду выбирает пользователь

        print ("На лапки надеты: % s" % self.__paws.shoes) #Описать обувь (будет смена локаций)


class Cat_builder:

    abstractmethod

    def get_name (self):
        pass
    def get_paws (self):
        pass

    abstractmethod

    def get_body (self):
        pass

    abstractmethod

    def get_health (self):
        pass

    abstractmethod

    def get_hungry (self):
        pass

    abstractmethod

    def get_mood (self):
        pass

    abstractmethod

    def get_tireLvl (self):
        pass

class New_player (Cat_builder):

    def get_name(self):
        name = Name()
        name.nick_name = name.set_nickname()
        return name

    abstractmethod

    def get_paws(self):
        paws = Paws()
        print (player.Messages.footwear_message(self))
        paws.shoes = paws.get_paws()
        return paws

    def get_body(self):   
        body = Body()
        body.desiese = body.determ_desiese()
        return body

    def get_health (self):
        health = Health()
        health.HP = health.set_HP()
        return health

    def get_mood(self):
        mood = Mood()
        mood.lvl_mood = "превосходное настроение "
        return mood

    def get_tireLvl(self):
        tireLvl = TireLvl()
        tireLvl.tirenes = "Бодрствование"
        return tireLvl

    def get_hungry(self):
        hungry = Hungry()
        hungry.hungry_lvl = "Не голоден"
        return hungry

#Второй строитель для расчета показателей питомца

class Continue_pet(Cat_builder):

    def get_paws(self):
        paws = Paws()
        New_player.get_paws()
        paws.shoes = paws.get_paws
        return paws

    def get_body(self):
        body = Body()
        varyav = Continue_pet.get_health(self)

        if varyav < 70:
            body.desiese = "Ухудшается состояние "

        if varyav < 30:
            body.desiese = "Критическое состояние состояние "

        if varyav < 70:
            body.desiese = "Ухудшается состояние "

        if varyav == 0:
            player.Messages.end_game()
            Scene.main()

        if varyav > 70:
            body.desiese = "Полностью здоров "

            return body

    def get_health (self):
        health = Health()
        health.HP = health.set_HP(self)

        return health


    def get_mood(self):
        mood = Mood()
        mood.lvl_mood = "превосходное настроение "
        return mood

    def get_tireLvl(self):
        tireLvl = TireLvl()
        tireLvl.tirenes = "Бодрствование"
        return tireLvl

    def get_hungry(self):
        hungry = Hungry()
        hungry.hungry_lvl = "Не голоден"
        return hungry






#Классы различных показателей

class Name():

    nick_name = None

    def set_nickname(self):
        nick_name = Name.nick_name = input ("Введите имя вашего питомца ")
        
        return nick_name

class Paws():

    shoes = None

    def get_paws(self):
        home_shoes = "домашняя обувь"
        winter_shoes = "зимняя обувь"
        summer_shoes = "летняя обувь"
        autmn_shoes = "демисезонная обувь"
        shoes_choice = input ("1)" + home_shoes + "\n 2)" + winter_shoes + "\n 3)" + summer_shoes + "\n 4" + autmn_shoes + " " )
        try:

            if shoes_choice == "1":
               shoes = home_shoes
                

            elif shoes_choice == "2":
                shoes = winter_shoes

            elif shoes_choice == "3":
                shoes = summer_shoes

            elif shoes_choice == "4":
                shoes = autmn_shoes

        except:
            print ("Вводите только числа указанные в меню")
        return shoes




class Health():

    HP = 100

    def set_HP(self):
        HP_tic = self.HP - 10
        return HP_tic

class Body():

    desiese = None

    def determ_desiese(self):

        health = Health()

        if health.HP >= 70:

            desiese = str(player.Desiese_describe.HP_optimum(self))

        if health.HP < 70:
            #Такой подход позволяет отделить логику игры от содержимого

            desiese = str(player.Desiese_describe.HP_lower_70(self))

        if health.HP < 30:

            desiese = str(player.Desiese_describe.HP_lower_30(self))

        if health.HP <= 0:
            print (player.Messages.end_game())

        return desiese

class Mood():

    lvl_mood = None

class TireLvl():

    tirenes = None

class Hungry():

    hungry_lvl = None


class Scene:

    def main():
        new_person = New_player() #Инициализируем класс
        cat_director = Cat_Director()
        #Для теста
        cat_director.set_builder(new_person)
        cat = cat_director.get_cat()
        cat.cat_status()
        #Scene.continue_scene()


    def continue_scene():

        print ("Выберите ваши действия нажмите enter")
        new_person = Continue_pet() #Инициализируем класс
        cat_director = Cat_Director()
        cat_director.set_builder(new_person)
        cat = cat_director.get_cat()
        stats = cat.cat_status()
        Scene.continue_scene()
        return stats


if __name__ == "__main__":
    text = input("Начать новую игру? y/n ")
    if text == "y":
        Scene.main()
