import sys
import enum
import array

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
        for i in range(0, 3) :
            self.me.append(i)
        for i in range(4, 7) :
            self.enemy.append(i)
        print('serperateMeEnemyCard Done')
    
    def checkMeEnemyCount(self) :
        if self.me.count == 0 or self.enemy.count == 0 :
            return False
        else :
            return True
    
    def rule_Check(self) :
        if self.rule_High_Card() == RuleResult.HIGH_CARD :
            return
        elif self.rule_One_Pair() == RuleResult.ONE_PAIR :
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
        else :
            print('rule_Check None')

    def rule_High_Card(self) :
        if self.checkMeEnemyCount() :
            return RuleResult.HIGH_CARD
        else :
            return RuleResult.ERROR

    def rule_One_Pair(self) :
        if self.checkMeEnemyCount() :
            return RuleResult.ONE_PAIR
        else :
            return RuleResult.ERROR

    def rule_Two_Pair(self) :
        if self.checkMeEnemyCount() :
            return RuleResult.TWO_PAIR
        else :
            return RuleResult.ERROR

    def rule_Three_Card(self) :
        if self.checkMeEnemyCount() :
            return RuleResult.THREE_CARD
        else :
            return RuleResult.ERROR

    def rule_Straight(self) :
        if self.checkMeEnemyCount() :
            return RuleResult.STRAIGHT
        else :
            return RuleResult.ERROR

    def rule_Flush(self) :
        if self.checkMeEnemyCount() :
            return RuleResult.FLUSH
        else :
            return RuleResult.ERROR

    def rule_Full_House(self) :
        if self.checkMeEnemyCount() :
            return RuleResult.FULL_HOUSE
        else :
            return RuleResult.ERROR

    def rule_FourCard(self) :
        if self.checkMeEnemyCount() :
            return RuleResult.FOUR_CARD
        else :
            return RuleResult.ERROR

    def rule_Straight_Flush(self) :
        if self.checkMeEnemyCount() :
            return RuleResult.STRAIGHT_FLUSH
        else :
            return RuleResult.ERROR

    def getResult(self) :
        print('')

class Card :
    def __init__(self, name) :
        self.name = name
        self.number = name[0:1]
        self.type = name[1:2]
        print('>>>>>>>>>>>>>>> '+self.number)
        print('>>>>>>>>>>>>>>> '+self.type)

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

rule.rule_Check()

rule.getResult()