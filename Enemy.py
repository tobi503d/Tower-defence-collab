from main import enemyStats, enemyList

#      --- blueprint for enemies ---
class enemy:
    def __init__(self, ID_, HP_, speed_, defense_):
        self.ID = ID_
        self.HP = HP_
        self.speed = speed_
        self.defence = defense_
    
    def __repr__(self):
        return f"Enemy(ID={self.ID}, HP={self.HP}, speed={self.speed}, defence={self.defence})"


def enemyObjectMaker(enemyType):
    
    try:
        tempID = enemyList[-1].ID +1
    except:
        tempID = 1

    tempObjekt = enemy(tempID, enemyStats[enemyType]["hp"], enemyStats[enemyType]["speed"], enemyStats[enemyType]["defence"])
    enemyList.append(tempObjekt)