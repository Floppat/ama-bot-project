from copy import deepcopy
from discord import Interaction
import datetime

from pets import Enemy, Pet
from functional import db


class User:
    def __init__(self, data: tuple):
        self.user_id = data[0]
        self.pet_PK = data[1]
        if None in db.read('users',data[0],'pet_id'):
            db.new_pet(data[0],'дружок',100,100,100,100,1,2,0,5,1,1,0,0)
        self.pet = Pet(db.read('pets', db.read('users',data[0],'pet_id')[0], '*'))
        self.tag = data[2]
        self.username = data[3]
        self.nickname = data[4]
        self.status_PK = data[5]
        self.status = db.read('status_keys', data[5], 'status')
        self.coins = data[6]
        self.quiz_record = data[7]
        self.register_date = data[8]
        self.xp = data[9]
        self.right_answers = 0


    def __repr__(self) -> str:
        return (f'--- Информация об игроке {self.nickname} ---\n'
                f'    | username: {self.username}\n'
                f'    | монеты: {self.coins}\n'
                f'    | рекорд в квизе: {self.quiz_record}\n'
                f'    | впервые с амой: {self.register_date}\n'
                f'    | опыт: {self.xp}\n'
                f'    | питомец: {db.read('pets',self.pet_PK,'pet_name')[0]}\n{self.pet}')


    async def train(self, interaction: Interaction):
        if not self.pet.can_train():
            await interaction.response.send_message('сперва вашему питомцу следует восстановить силы')
            return
        self.pet.train()
        db.change('pets',self.pet_PK,'hp',int,self.pet.hp)
        db.change('pets',self.pet_PK,'sp',int,self.pet.sp)
        db.change('pets',self.pet_PK,'str',int,self.pet.str)
        db.change('pets',self.pet_PK,'xp',int,self.pet.xp)
        await interaction.response.send_message(f'питомец прошёл изнурительные тренировки\n{self.pet}')
        return


    async def feed(self, interaction: Interaction):
        if not self.pet.can_feed():
            await interaction.response.send_message('Ваш питомец не голоден')
            return
        self.pet.feed()
        db.change('pets',self.pet_PK,'hp',int,self.pet.hp)
        await interaction.response.send_message(f'питомец сытно поел\n{self.pet}')
        return


    async def attack(self, interaction: Interaction):
        if not self.pet.can_attack():
            await interaction.response.send_message('сперва вашему питомцу следует восстановить силы')
            return
        enemy = Enemy(target_pet=self.pet)
        now_enemy=deepcopy(enemy)
        self.pet.sp -= 60
        while True:
            enemy.attack(target_pet=self.pet)
            self.pet.attack(target_pet=enemy)

            if not self.pet:
                await interaction.response.send_message(f'вы проиграли!, ваш враг был:{now_enemy}\n'
                                                        f'ваши характеристики:\n{self.pet}')
                break

            if not enemy:
                self.coins += 100
                self.pet.max_str += 2
                self.pet.avg += 2
                self.pet.min_def += 1
                await interaction.response.send_message(f'вы выиграли. противник стал сильнее. ваш враг был:{now_enemy}\n'
                                'вы заработали 100 монет\n'
                                f'итого монет: {self.coins}\n'
                                f'ваши характеристики:\n{self.pet}')
                break
        db.change('pets',self.pet_PK,'hp',int,self.pet.hp)
        db.change('pets',self.pet_PK,'sp',int,self.pet.sp)
        db.change('users',self.user_id,'coins',int,self.coins)
        db.change('pets',self.pet_PK,'max_str',int,self.pet.max_str)
        db.change('pets',self.pet_PK,'avg',int,self.pet.avg)
        db.change('pets',self.pet_PK,'min_def',int,self.pet.min_def)
        return


    async def sleep(self, interaction: Interaction):
        if not self.pet.can_sleep():
            await interaction.response.send_message('Ваш питомец ещё не устал')
            return
        self.pet.sleep()
        db.change('pets',self.pet_PK,'sp',int,self.pet.sp)
        await interaction.response.send_message(f'питомец выспался\n{self.pet}')
        return


    async def shop(self, interaction: Interaction, item: str):
        shop_pets = {
            '1': Pet((self.pet_PK,self.user_id,self.pet.name,self.pet.max_hp,self.pet.hp,120,120,5,2,0,self.pet.max_str,self.pet.min_def,self.pet.avg,400,7)),
            '2': Pet((self.pet_PK,self.user_id,self.pet.name,self.pet.max_hp,self.pet.hp,140,140,10,2,0,self.pet.max_str,self.pet.min_def,self.pet.avg,800,13)),
            '3': Pet((self.pet_PK,self.user_id,self.pet.name,self.pet.max_hp,self.pet.hp,160,160,15,2,0,self.pet.max_str,self.pet.min_def,self.pet.avg,1200,19)),
            '4': Pet((self.pet_PK,self.user_id,self.pet.name,self.pet.max_hp,self.pet.hp,180,180,20,2,0,self.pet.max_str,self.pet.min_def,self.pet.avg,1600,25)),
            '5': Pet((self.pet_PK,self.user_id,self.pet.name,self.pet.max_hp,self.pet.hp,200,200,25,2,0,self.pet.max_str,self.pet.min_def,self.pet.avg,2000,31))
        }
        message_items = '\n'.join([f'{item=}; {shop_pets[item].shop()}' for item in shop_pets])

        if item not in shop_pets or item in ('?', 'help', 'items'):
            await interaction.response.send_message(f'Важно! При покупке артефактов сбрасывается опыт и сила (так как для питомца подобное снаряжение в новинку)\n'
                                                    f'Также, враги слабее не станут. игра рассчитана на убить время когда вам скучно, не торопитесь\n'
                                                    f'Доступные для покупки артефакты:\n{message_items}')
            return

        if self.coins < shop_pets[item].price:
            await interaction.response.send_message(f'Недостаточно монет: чтобы купить этот артефакт, нужно {shop_pets[item].price} монет')
            return
        elif self.pet.xp < shop_pets[item].xp_price:
            await interaction.response.send_message(f'Недостаточно опыта: чтобы купить этот артефакт, нужно {shop_pets[item].xp_price} опыта')
            return
        
        self.coins -= shop_pets[item].price
        self.pet = deepcopy(shop_pets[item])
        db.change('pets',self.pet_PK,'max_sp',int,self.pet.max_sp)
        db.change('pets',self.pet_PK,'sp',int,self.pet.sp)
        db.change('pets',self.pet_PK,'def',int,self.pet.defense)
        db.change('pets',self.pet_PK,'str',int,self.pet.str)
        db.change('pets',self.pet_PK,'xp',int,self.pet.xp)
        db.change('users',self.user_id,'coins',int,self.coins)
        await interaction.response.send_message(f'Ваш пет надел артефакт:\n{self.pet}')


    async def right_answer(self):
        self.right_answers+=1
    async def quizresult(self, interaction: Interaction):
        if self.right_answers == 5:
            job = ', хорошая работа!'
        elif self.right_answers >= 0 and self.right_answers <= 2:
            job = ', попробуйте почитать о глобальном потеплении ещё раз!'
        elif self.right_answers >= 3 and self.right_answers <= 4:
            job = ', неплохой результат, повторите теорию и попробуйте ещё раз!'
        if self.right_answers > self.quiz_record:
            self.quiz_record = self.right_answers
        await interaction.response.send_message(content=f'Вы набрали {self.right_answers}/5 очков{job}\n'
                                                        f'рекорд:{self.quiz_record}/5 очков.')
        db.change('users',self.user_id,'quiz_record',int,self.quiz_record)
        self.right_answers = 0


def registred(interaction: Interaction):
    user = db.read('users',interaction.user.id,'*')
    if not user:
        db.new_user(interaction.user.id,'NULL',interaction.user.name,interaction.user.global_name,'NULL',1,0,0,str(datetime.datetime.now()).split()[0],0)
        user = db.read('users',interaction.user.id,'*')
    return User(user)

def get_other_user(user_tag: str):
    other_user = db.read('users',db.get_PK('users','tag',user_tag,str)[0],'*')
    if not other_user:
        return 'указан неверный тег или такой пользователь не пользовался ботом'
    return User(other_user)
