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
    NONE = 999

class Rule : 

    def __init__(self) :
        self.cards = []
        self.result = RuleResult.NONE

    def addCard(self, card) :
        self.cards.append(card)

    def serperateMeEnemyCard(self) :
        print('')

    def rule_Check(self) :
        print('')

    def rule_High_Card(self) :
        return RuleResult.HIGH_CARD
    def rule_One_Pair(self) :
        return RuleResult.ONE_PAIR
    def rule_Two_Pair(self) :
        return RuleResult.TWO_PAIR
    def rule_Three_Card(self) :
        return RuleResult.THREE_CARD
    def rule_Straight(self) :
        return RuleResult.STRAIGHT
    def rule_Flush(self) :
        return RuleResult.FLUSH
    def rule_Full_House(self) :
        return RuleResult.FULL_HOUSE
    def rule_FourCard(self) :
        return RuleResult.FOUR_CARD
    def rule_Straight_Flush(self) :
        return RuleResult.STRAIGHT_FLUSH

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