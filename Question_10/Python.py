import sys
import enum
import array
import re

# 2H 3D 5S 9C KD 2C 3H 4S 8C AH
# 2H 4S 4C 2D 4H 2S 8S AS QS 3C

class RuleResult(enum.Enum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_CARD = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_CARD = 7
    STRAIGHT_FLUSH = 8
    NONE = 998
    ERROR = 999

class Rule : 

    def __init__(self) :
        self.cards = []
        self.result = RuleResult.NONE

    def addCard(self, card) :
        self.cards.append(card)
        print('addCard Done')

    def serperateMeEnemyCard(self) :
        self.me = []
        self.enemy = []
        for i in range(0, 5) :
            self.me.append(self.cards[i])
        for i in range(5, 10) :
            self.enemy.append(self.cards[i])
        print('serperateMeEnemyCard Done')

    def sortCards(self) :
        self.me.sort(reverse=True)
        self.enemy.sort(reverse=True)
        for i in self.me :
            print('>>>>>>>>>>>> me '+i.number)
        for i in self.enemy :
            print('>>>>>>>>>>>> enemy : '+i.number)
    
    def checkMeEnemyCount(self) :
        if self.me.count == 0 or self.enemy.count == 0 :
            return False
        else :
            return True
    
    def rule_Check(self) :
        
        if self.rule_One_Pair() == RuleResult.ONE_PAIR :
            return
        elif self.rule_Two_Pair() == RuleResult.TWO_PAIR :
            return
        elif self.rule_Three_Card() == RuleResult.THREE_CARD :
            return
        elif self.rule_Straight() == RuleResult.STRAIGHT :
            return
        elif self.rule_Flush() == RuleResult.FLUSH :
            return
        elif self.rule_Full_House() == RuleResult.FULL_HOUSE :
            return
        elif self.rule_FourCard() == RuleResult.FOUR_CARD :
            return
        elif self.rule_Straight_Flush() == RuleResult.STRAIGHT_FLUSH :
            return
        elif self.rule_High_Card() == RuleResult.HIGH_CARD :
            return
        else :
            print('rule_Check None')

    def rule_High_Card(self) :
        print('rule_High_Card start')
        if self.checkMeEnemyCount() :
            for i in range(0, 5) :
                for j in range(0, 5) :
                    if self.me[i] > self.enemy[j] :
                        return RuleResult.HIGH_CARD
                    elif self.me[i] < self.enemy[j] :
                        return RuleResult.HIGH_CARD
            return RuleResult.NONE
        else :
            return RuleResult.ERROR

    def list_duplicates(self, seq):
        seen = set()
        seen_add = seen.add
        seen_twice = set( x for x in seq if x in seen or seen_add(x) )
        return list(seen_twice)

    def rule_One_Pair(self) :
        print('rule_One_Pair start')
        if self.checkMeEnemyCount() :
            me_same_card = self.list_duplicates(self.me)
            enemy_same_card = self.list_duplicates(self.enemy)
            ms_count = len(me_same_card)
            es_count = len(enemy_same_card)
            print('ms_count >>>>>>>>>>>>>>>>> '+str(ms_count))
            print('es_count >>>>>>>>>>>>>>>>> '+str(es_count))
            if ms_count == 1 or es_count == 1 :
                if ms_count == 1 :
                    return RuleResult.ONE_PAIR
                elif es_count == 1 :
                    return RuleResult.ONE_PAIR
                else :
                    return RuleResult.NONE
            elif ms_count == 1 and es_count == 1 :
                if me_same_card[0] > me_same_card[0] :
                        return RuleResult.ONE_PAIR
                elif me_same_card[0] < me_same_card[0] :
                    return RuleResult.ONE_PAIR
                else :
                    me_same_card = list(set(self.me) - set(self.me_same_card))
                    enemy_same_card = list(set(self.enemy) - set(self.enemy_same_card))
                    if len(me_same_card) > 1 and len(enemy_same_card) > 1 :
                        for i in range(0, 3) :
                            for j in range(0, 3) :
                                if me_same_card[i] > me_same_card[j] :
                                    return RuleResult.TWO_PAIR
                                elif me_same_card[i] < me_same_card[j] :
                                    return RuleResult.TWO_PAIR               
            else :
                return RuleResult.NONE
        else :
            return RuleResult.ERROR

    def rule_Two_Pair(self) :
        print('rule_Two_Pair start')
        if self.checkMeEnemyCount() :
            me_same_card = self.list_duplicates(self.me)
            enemy_same_card = self.list_duplicates(self.enemy)
            ms_count = len(me_same_card)
            es_count = len(enemy_same_card)
            print('ms_count >>>>>>>>>>>>>>>>> '+str(ms_count))
            print('es_count >>>>>>>>>>>>>>>>> '+str(es_count))
            if  ms_count == 2 or es_count == 2 :
                if ms_count == 2 :
                    return RuleResult.ONE_PAIR
                elif es_count == 2 :
                    return RuleResult.ONE_PAIR
                else :
                    return RuleResult.NONE
            elif ms_count == 2 and es_count == 2 :
                me_same_card.sort(reverse=True)
                enemy_same_card.sort(reverse=True)
                if me_same_card[0] > me_same_card[0] :
                    return RuleResult.ONE_PAIR
                elif me_same_card[0] < me_same_card[0] :
                    return RuleResult.ONE_PAIR
                else :
                    me_same_card = list(set(self.me) - set(self.me_same_card))
                    enemy_same_card = list(set(self.enemy) - set(self.enemy_same_card))
                    for i in range(0, 1) :
                        for j in range(0, 1) :
                            if me_same_card[i] > me_same_card[j] :
                                return RuleResult.TWO_PAIR
                            elif me_same_card[i] < me_same_card[j] :
                                return RuleResult.TWO_PAIR
                    return RuleResult.NONE
            else :
                return RuleResult.NONE
        else :
            return RuleResult.ERROR

    def sub_Check_Three_Same_Card(self, arg) :
        print('')

    def rule_Three_Card(self) :
        print('rule_Three_Card start')
        if self.checkMeEnemyCount() :
            me_same_card = self.list_duplicates(self.me)
            enemy_same_card = self.list_duplicates(self.enemy)
            ms_count = len(me_same_card)
            es_count = len(enemy_same_card)
            if ms_count > 0 and ms_count <= 2 or es_count > 0 and es_count <= 2:
                if ms_count > 0 and ms_count <= 2 :
                    return RuleResult.THREE_CARD
                elif es_count > 0 and es_count <= 2 :
                    return RuleResult.THREE_CARD
                else :
                    return RuleResult.NONE
            elif ms_count > 0 and ms_count <= 2 and es_count > 0 and es_count <= 2:
                print('ms_count >>>>>>>>>>>>>>>>> '+str(ms_count))
                print('es_count >>>>>>>>>>>>>>>>> '+str(es_count))
                ms_count = self.sub_Check_Three_Same_Card(me_same_card)
                es_count = self.sub_Check_Three_Same_Card(enemy_same_card)
                if ms_count == 3 and es_count == 3 :
                    me_same_card.sort(reverse=True)
                    enemy_same_card.sort(reverse=True)
                    if me_same_card[0] > me_same_card[0] :
                        return RuleResult.ONE_PAIR
                    elif me_same_card[0] < me_same_card[0] :
                        return RuleResult.ONE_PAIR
                    else :
                        me_same_card = list(set(self.me) - set(self.me_same_card))
                        enemy_same_card = list(set(self.enemy) - set(self.enemy_same_card))
                        for i in range(0, 3) :
                            for j in range(0, 3) :
                                if me_same_card[i] > me_same_card[j] :
                                    return RuleResult.TWO_PAIR
                                elif me_same_card[i] < me_same_card[j] :
                                    return RuleResult.TWO_PAIR
                        return RuleResult.NONE
                else :
                    return RuleResult.NONE
        else :
            return RuleResult.ERROR

    def rule_Straight(self) :
        print('rule_Straight start')
        if self.checkMeEnemyCount() :
            index = 0
            for i in self.me :
                if i.number.isdigit() and index == 0 :
                    index = int(i.number)
                elif i.number.isdigit() and index+1 == int(i.number) :
                    index = int(i.number)
                else :
                    return RuleResult.NONE
            index = 0
            for j in self.enemy :
                if index == 0 :
                    index = int(j.number)
                elif i.number.isdigit() and index+1 == int(j.number) :
                    index = int(j.number)
                else :
                    return RuleResult.NONE
            for i in range(0, 5) :
                for j in range(0, 5) :
                    if self.me[i] > self.enemy[j] :
                        return RuleResult.STRAIGHT
                    elif self.me[i] < self.enemy[j] :
                        return RuleResult.STRAIGHT
            return RuleResult.STRAIGHT
        else :
            return RuleResult.ERROR

    def rule_Flush(self) :
        print('rule_Flush start')
        if self.checkMeEnemyCount() :
            index = ""
            for i in self.me :
                if index == "" :
                    index = i.type
                elif index == i.type :
                    index = i.type
                else :
                    return RuleResult.NONE
            index = ""
            for j in self.enemy :
                if index == "" :
                    index = i.type
                elif index == i.type :
                    index = i.type
                else :
                    return RuleResult.NONE
            for i in range(0, 5) :
                for j in range(0, 5) :
                    if self.me[i] > self.enemy[j] :
                        return RuleResult.STRAIGHT
                    elif self.me[i] < self.enemy[j] :
                        return RuleResult.STRAIGHT
        else :
            return RuleResult.ERROR

    def rule_Full_House(self) :
        print('rule_Full_House start')
        if self.checkMeEnemyCount() :
            me_same_card = list(set(self.me).intersection(self.me))
            enemy_same_card = list(set(self.enemy).intersection(self.enemy))
            if me_same_card.count == 3 and enemy_same_card.count == 3 :
                me_same_card.sort(reverse=True)
                enemy_same_card.sort(reverse=True)
                for i in range(0, 3) :
                    for j in range(0, 3) :
                        if me_same_card[i] > me_same_card[j] :
                            return RuleResult.THREE_CARD
                        elif me_same_card[i] < me_same_card[j] :
                            return RuleResult.THREE_CARD
            else :
                return RuleResult.NONE
        else :
            return RuleResult.ERROR

    def rule_FourCard(self) :
        print('rule_FourCard start')
        if self.checkMeEnemyCount() :
            me_same_card = list(set(self.me).intersection(self.me))
            enemy_same_card = list(set(self.enemy).intersection(self.enemy))
            me_count = len(set(me_same_card) - set(self.me))
            enemy_count = len(set(enemy_same_card) - set(self.enemy))
            if me_count == 4 and enemy_count == 4 :
                me_same_card.sort(reverse=True)
                enemy_same_card.sort(reverse=True)
                if me_same_card[0] > me_same_card[0] :
                    return RuleResult.ONE_PAIR
                elif me_same_card[0] < me_same_card[0] :
                    return RuleResult.ONE_PAIR
                else :
                    me_same_card = list(set(self.me) - set(self.me_same_card))
                    enemy_same_card = list(set(self.enemy) - set(self.enemy_same_card))
                    for i in range(0, 3) :
                        for j in range(0, 3) :
                            if me_same_card[i] > me_same_card[j] :
                                return RuleResult.FOUR_CARD
                            elif me_same_card[i] < me_same_card[j] :
                                return RuleResult.FOUR_CARD
                    return RuleResult.NONE
            else :
                return RuleResult.NONE
        else :
            return RuleResult.ERROR

    def rule_Straight_Flush(self) :
        print('rule_Straight_Flush start')
        if self.checkMeEnemyCount() :
            if self.rule_Flush() == RuleResult.FLUSH and self.rule_Straight() == RuleResult.STRAIGHT :
                for i in range(0, 5) :
                    for j in range(0, 5) :
                        if self.me[i] > self.enemy[j] :
                            return RuleResult.STRAIGHT_FLUSH
                        elif self.me[i] < self.enemy[j] :
                            return RuleResult.STRAIGHT_FLUSH
                return RuleResult.NONE
            else :
                return RuleResult.NONE
        else :
            return RuleResult.ERROR

    def getResult(self) :
        print('')

class Card(object) :
    def __init__(self, name) :
        self.name = name        
        self.number = self.name[0:1]
        self.type = self.name[1:2]
        # print('>>>>>>>>>>>>>>> '+self.number)
        # print('>>>>>>>>>>>>>>> '+self.type)
    def __hash__(self):
        return hash(self.number)
    def __eq__(self, other) :
        return self.number == other.number
    def __lt__(self, other) :
        if self.number.isalpha() and other.number.isalpha() : 
            return self.cardConvertInt(self.number) < self.cardConvertInt(other.number)
        else : 
            return self.number < other.number
    def __gt__(self, other) :
        if self.number.isalpha() and other.number.isalpha() : 
            return self.cardConvertInt(self.number) > self.cardConvertInt(other.number)
        else : 
            return self.number < other.number
    def cardConvertInt(self, arg) :
        if arg == 'A' :
            return 14
        elif arg == 'K' :
            return 13
        elif arg == 'Q' :
            return 12
        elif arg == 'J' :
            return 11
        elif arg == 'T' :
            return 10
        else :
            return 0

inputArray = []
while (True) :
    i = input(">")
    if i == 'X' : 
        break
    else :
        inputArray.append(i)

rule = Rule()

for commands in inputArray :
    seperatecommand = commands.split(' ')
    for subcommand in seperatecommand :
        rule.addCard(Card(subcommand))

rule.serperateMeEnemyCard()

rule.sortCards()

rule.rule_Check()

rule.getResult()