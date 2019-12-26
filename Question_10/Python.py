import sys
import enum
import array
import re

# 2H 3D 5S 9C KD 2C 3H 4S 8C AH
# 2H 4S 4C 2D 4H 2S 8S AS QS 3C
# 2H 3D 5S 9C KD 2C 3H 4S 8C KH
# 2H 3D 5S 9C KD 2D 3H 5C 9S KH

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
    
    def rule_Check(self, arg) :
        if self.rule_Straight_Flush(arg) == RuleResult.STRAIGHT_FLUSH :
            return 8
        elif self.rule_FourCard(arg) == RuleResult.FOUR_CARD :
            return 7
        elif self.rule_Full_House(arg) == RuleResult.FULL_HOUSE :
            return 6
        elif self.rule_Flush(arg) == RuleResult.FLUSH :
            return 5
        elif self.rule_Straight(arg) == RuleResult.STRAIGHT :
            return 4
        elif self.rule_Three_Card(arg) == RuleResult.THREE_CARD :
            return 3
        elif self.rule_Two_Pair(arg) == RuleResult.TWO_PAIR :
            return 2
        elif self.rule_One_Pair(arg) == RuleResult.ONE_PAIR :
            return 1
        elif self.rule_High_Card(arg) == RuleResult.HIGH_CARD :
            return 0
        else :
            return -1

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

    def rule_High_Card(self, arg) :
        print('rule_High_Card start')
        if self.checkMeEnemyCount() :
            index = 0
            for i in arg :
                if i.number.isdigit() and index == 0 :
                    index = int(i.number)
                elif i.number.isdigit() and index+1 == int(i.number) :
                    index = int(i.number)
                else :
                    return RuleResult.NONE
            return RuleResult.HIGH_CARD
        else :
            return RuleResult.ERROR

    def list_duplicates(self, seq):
        seen = set()
        seen_add = seen.add
        seen_twice = set( x for x in seq if x in seen or seen_add(x) )
        return list(seen_twice)

    def rule_One_Pair(self, arg) :
        print('rule_One_Pair start')
        if self.checkMeEnemyCount() :
            same_card = self.list_duplicates(arg)
            count = len(same_card)
            if count == 1 :
                return RuleResult.ONE_PAIR
            else :
                return RuleResult.NONE
        else :
            return RuleResult.ERROR

    def rule_Two_Pair(self, arg) :
        print('rule_Two_Pair start')
        if self.checkMeEnemyCount() :
            same_card = self.list_duplicates(arg)
            count = len(same_card)
            if count == 2 :
                return RuleResult.TWO_PAIR
            else :
                return RuleResult.NONE
        else :
            return RuleResult.ERROR

    def rule_Three_Card(self, arg) :
        print('rule_Three_Card start')
        if self.checkMeEnemyCount() :
            same_card = self.list_duplicates(arg)
            for i in same_card :
                if self.countX(arg, i.number) == 3 :
                    return RuleResult.THREE_CARD
            return RuleResult.NONE
        else :
            return RuleResult.NONE

    def countX(self, lst, x): 
        count = 0
        for ele in lst: 
            if (ele.number == x): 
                count = count + 1
        return count

    def rule_Straight(self, arg) :
        print('rule_Straight start')
        if self.checkMeEnemyCount() :
            index = 0
            for i in arg :
                if i.number.isdigit() and index == 0 :
                    index = int(i.number)
                elif i.number.isdigit() and index+1 == int(i.number) :
                    index = int(i.number)
                else :
                    return RuleResult.NONE
            return RuleResult.STRAIGHT
        else :
            return RuleResult.ERROR

    def rule_Flush(self, arg) :
        print('rule_Flush start')
        if self.checkMeEnemyCount() :
            index = ""
            for i in arg :
                if index == "" :
                    index = i.type
                elif index == i.type :
                    index = i.type
                else :
                    return RuleResult.NONE
            return RuleResult.FLUSH
        else :
            return RuleResult.ERROR

    def rule_Full_House(self, arg) :
        print('rule_Full_House start')
        if self.checkMeEnemyCount() :
            same_card = self.list_duplicates(arg)
            if len(same_card) == 2 : 
                i = self.countX(arg, same_card[0].number)
                j = self.countX(arg, same_card[1].number)
                print('rule_Full_House i : '+str(i))
                print('rule_Full_House i : '+str(j))
                if (i+j) == 5 : 
                    return RuleResult.FULL_HOUSE
                else : 
                    return RuleResult.NONE
            else : 
                return RuleResult.NONE
        else :
            return RuleResult.ERROR

    def rule_FourCard(self, arg) :
        print('rule_FourCard start')
        if self.checkMeEnemyCount() :
            same_card = self.list_duplicates(arg)
            for i in same_card :
                if self.countX(arg, i.number) == 4 :
                    return RuleResult.FOUR_CARD
            return RuleResult.NONE
        else :
            return RuleResult.NONE

    def rule_Straight_Flush(self, arg) :
        print('rule_Straight_Flush start')
        if self.checkMeEnemyCount() :
            index1 = ""
            for i in arg :
                if index1 == "" :
                    index1 = i.type
                elif index1 == i.type :
                    index1 = i.type
                else :
                    return RuleResult.NONE
            index2 = 0
            for i in arg :
                if i.number.isdigit() and index2 == 0 :
                    index = int(i.number)
                elif i.number.isdigit() and index2+1 == int(i.number) :
                    index2 = int(i.number)
                else :
                    return RuleResult.NONE
            return RuleResult.STRAIGHT_FLUSH
        else :
            return RuleResult.ERROR

    def getResult(self) :
        me_result = self.rule_Check(self.me)
        print('me_result >>>>>>>>> '+str(me_result))
        enemy_result = self.rule_Check(self.enemy)
        print('enemy_result >>>>>>>>> '+str(enemy_result))
        if me_result > enemy_result :
            print('Black Win')
        elif me_result < enemy_result :
            print('White Win')
        else : 
            for i in range(0, 5) :
                if not self.me[i].number.isdigit() :
                    me = self.cardConvertInt(self.me[i].number)
                else :
                    me = int(self.me[i].number)
                if not self.enemy[i].number.isdigit() :
                    enemy = self.cardConvertInt(self.enemy[i].number)
                else :
                    enemy = int(self.enemy[i].number)
                if me > enemy :
                    print('Black Win')
                    return
                elif me < enemy :
                    print('White Win')
                    return
            print('Tie')

                

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

rule.getResult()