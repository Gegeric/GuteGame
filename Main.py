from typing import List, Any

import pygame
import random
import copy


# init pygame
pygame.init()
# create screen
screen = pygame.display.set_mode((1200, 760))

# Title and Icon
pygame.display.set_caption("Älschgame")
icon = pygame.image.load("C:/Users/Eric/PycharmProjects/lel/resources/images/moose.png")
pygame.display.set_icon(icon)

ImgNeutral = list(range(6))
ImgNeutral[0] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/empty.png")
ImgNeutral[1] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/black.png")
ImgNeutral[2] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/emptyNext.png")
ImgNeutral[3] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/emptyBack.png")
ImgNeutral[4] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/en.png")
ImgNeutral[5] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/de.png")

Img_building = list(range(8))
Img_building[0] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerBlue/baseBlue.png")
Img_building[1] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerBlue/barrackBlue.png")
Img_building[2] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerPurple/basePurple.png")
Img_building[3] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerPurple/barrackPurple.png")
Img_building[4] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerOrange/baseOrange.png")
Img_building[5] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerOrange/barrackOrange.png")
Img_building[6] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerGreen/baseGreen.png")
Img_building[7] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerGreen/barrackGreen.png")

Img_laser = list(range(20))
Img_laser[0] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/laser0.png")
Img_laser[1] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/laser90.png")
Img_laser[2] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/laser180.png")
Img_laser[3] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/laser270.png")
Img_laser[4] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerBlue/laserB0.png")
Img_laser[5] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerBlue/laserB90.png")
Img_laser[6] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerBlue/laserB180.png")
Img_laser[7] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerBlue/laserB270.png")
Img_laser[8] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerPurple/laserP0.png")
Img_laser[9] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerPurple/laserP90.png")
Img_laser[10] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerPurple/laserP180.png")
Img_laser[11] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerPurple/laserP270.png")
Img_laser[12] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerOrange/laserO0.png")
Img_laser[13] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerOrange/laserO90.png")
Img_laser[14] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerOrange/laserO180.png")
Img_laser[15] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerOrange/laserO270.png")
Img_laser[16] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerGreen/laserG0.png")
Img_laser[17] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerGreen/laserG90.png")
Img_laser[18] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerGreen/laserG180.png")
Img_laser[19] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerGreen/laserG270.png")

Img_tower = list(range(5))
Img_tower[0] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/tower.png")
Img_tower[1] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerBlue/towerBlue.png")
Img_tower[2] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerPurple/towerPurple.png")
Img_tower[3] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerOrange/towerOrange.png")
Img_tower[4] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerGreen/towerGreen.png")

Img_boy = list(range(4))
Img_boy[0] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerBlue/boyBlue.png")
Img_boy[1] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerPurple/boyPurple.png")
Img_boy[2] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerOrange/boyOrange.png")
Img_boy[3] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerGreen/boyGreen.png")

Img_archer = list(range(4))
Img_archer[0] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerBlue/bogiBlue.png")
Img_archer[1] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerPurple/bogiPurple.png")
Img_archer[2] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerOrange/bogiOrange.png")
Img_archer[3] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerGreen/bogiGreen.png")

Img_knight = list(range(4))
Img_knight[0] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerBlue/knightBlue.png")
Img_knight[1] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerPurple/knightPurple.png")
Img_knight[2] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerOrange/knightOrange.png")
Img_knight[3] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerGreen/knightGreen.png")

Img_info = list(range(15))
Img_info[0] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/info/enBase.png")
Img_info[1] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/info/deBase.png")
Img_info[2] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/info/enBarrack.png")
Img_info[3] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/info/deBarrack.png")
Img_info[4] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/info/enBoy.png")
Img_info[5] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/info/deBoy.png")
Img_info[6] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/info/enArcher.png")
Img_info[7] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/info/deArcher.png")
Img_info[8] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/info/enKnight.png")
Img_info[9] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/info/deKnight.png")
Img_info[10] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/info/enLaser.png")
Img_info[11] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/info/deLaser.png")
Img_info[12] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/info/enTower.png")
Img_info[13] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/info/deTower.png")
Img_info[14] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/info/black.png")


class All:
    owner = 0
    combine = False
    img_en = pygame.image.tostring(Img_info[14], "RGBA")
    img_de = pygame.image.tostring(Img_info[14], "RGBA")


class Neutral(All):
    name = "Neutral"
    name_ger = name

    def __init__(self, img_select):
        if img_select == 0:
            self.name = "Empty"
        self.img = pygame.image.tostring(ImgNeutral[img_select].convert(), "RGBA")


class Building(All):

    def __init__(self, img_select, player):
        self.owner = player
        if img_select == 0:  # Base
            self.img = pygame.image.tostring(Img_building[player * 2 - 2], "RGBA")
            self.health = 3
            self.name = "Base"
            self.name_ger = "Basis"
            self.img_en = pygame.image.tostring(Img_info[0], "RGBA")
            self.img_de = pygame.image.tostring(Img_info[1], "RGBA")
        if img_select == 1:  # Barrack
            self.img = pygame.image.tostring(Img_building[player * 2 - 1], "RGBA")
            self.health = 2
            self.name = "Barrack"
            self.name_ger = "Kaserne"
            self.img_en = pygame.image.tostring(Img_info[2], "RGBA")
            self.img_de = pygame.image.tostring(Img_info[3], "RGBA")
            self.combine = True


class Laser(All):
    atk = 3
    atkRange = 6
    name_ger = "Laser"
    img_en = pygame.image.tostring(Img_info[10], "RGBA")
    img_de = pygame.image.tostring(Img_info[11], "RGBA")

    def __init__(self, rotation, player, base):
        self.img = pygame.image.tostring(Img_laser[(player*4) + rotation], "RGBA")
        self.owner = player
        self.rotation = rotation
        if base:
            self.name = "BaseLaser"
        else:
            self.name = "Laser"
            self.health = 0
            if player == 0:
                self.combine = True
            else:
                self.health = 3


class Tower(All):
    name = "Tower"
    name_ger = "Turm"
    atk = 2
    health = 0
    atkRange = 4
    img_en = pygame.image.tostring(Img_info[12], "RGBA")
    img_de = pygame.image.tostring(Img_info[13], "RGBA")

    def __init__(self, player):
        self.img = pygame.image.tostring(Img_tower[player], "RGBA")
        self.owner = player
        if player == 0:
            self.combine = True
        else:
            self.health = 3


class MidTower(All):
    name = "MidTower"
    name_ger = "MittelTurm"
    atk = 3
    atkRange = 4

    def __init__(self, player):
        self.img = pygame.image.tostring(Img_tower[player], "RGBA")
        self.owner = player


class Boy(All):
    name = "Boy"
    name_ger = name
    health = 1
    runRange = 4
    atk = 1
    atkRange = 1

    def __init__(self, player):
        self.img = pygame.image.tostring(Img_boy[player-1], "RGBA")
        self.owner = player
        self.img_en = pygame.image.tostring(Img_info[4], "RGBA")
        self.img_de = pygame.image.tostring(Img_info[5], "RGBA")
        self.combine = True


class Archer(All):
    name = "Archer"
    name_ger = "Schütze"
    health = 1
    runRange = 2
    atk = 2
    atkRange = 4

    def __init__(self, player):
        self.img = pygame.image.tostring(Img_archer[player-1], "RGBA")
        self.owner = player
        self.img_en = pygame.image.tostring(Img_info[6], "RGBA")
        self.img_de = pygame.image.tostring(Img_info[7], "RGBA")


class Knight(All):
    name = "Knight"
    name_ger = "Ritter"
    health = 4
    runRange = 3
    atk = 3
    atkRange = 1

    def __init__(self, player):
        self.img = pygame.image.tostring(Img_knight[player - 1], "RGBA")
        self.owner = player
        self.img_en = pygame.image.tostring(Img_info[8], "RGBA")
        self.img_de = pygame.image.tostring(Img_info[9], "RGBA")


SelectionImg = list(range(8))
SelectionMode = 0
Selection = 0
Next = 0

PlayerTurn = 0
PlayerActions = 3
English = True
Info = False
Lost = [False, False, False, False]

Field = []
Fieldclones = list(range(10))
Black = Neutral(1)
AllLasers = list(range(20))
AllTowers = list(range(5))
Pos = list(range(8))


SelectionImg[0] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/selection/selection.png")
SelectionImg[1] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/selection/selectionAttack.png")
SelectionImg[2] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/selection/selectionRun.png")
SelectionImg[3] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/selection/selectionSpecial.png")
SelectionImg[4] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/selection/selectionInfo.png")
SelectionImg[5] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/selection/selection2.png")
SelectionImg[6] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/selection/selection2Archer.png")
SelectionImg[7] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/selection/selection2Knight.png")

NextImg = list(range(5))
NextImg[0] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/emptyNext.png")
NextImg[1] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerBlue/nextBlue.png")
NextImg[2] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerPurple/nextPurple.png")
NextImg[3] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerOrange/nextOrange.png")
NextImg[4] = pygame.image.load("C:/Users/Eric/PycharmProjects/gute/images/playerGreen/nextGreen.png")

Colors = list(range(8))
Colors[0] = (255, 255, 255)
Colors[1] = (0, 126, 232)
Colors[2] = (163, 73, 164)
Colors[3] = (255, 127, 39)
Colors[4] = (34, 177, 76)
Colors[5] = (0, 0, 0)
Colors[6] = (224, 224, 224)
Colors[7] = (225, 225, 51)
font = pygame.font.Font('freesansbold.ttf', 32)
selectionfont = pygame.font.Font('freesansbold.ttf', 20)
Textselect = list(range(5))
Selectrect = list(range(5))
Texts = list(range(7))
TextRect = list(range(7))
StrTurn = str(PlayerTurn)
StrMoves = str(PlayerActions)
CommentText = ""


def difff(x, y):
    if x > y:
        return x - y
    else:
        return y - x


def select(field_X, field_Y):
    global SelectionMode
    global Pos
    global PlayerActions
    global Info
    global Next

    if field_X == field_Y == 18 and SelectionMode != 2 and SelectionMode != 4:
        next_turn()
    if field_X == 16 and field_Y == 18 and SelectionMode != 2 and SelectionMode != 4:
        language()
    if fieldX == 17 and fieldY == 18 and SelectionMode != 2 and SelectionMode != 4:
        load()

    if SelectionMode == 0:
        if Field[field_Y][field_X].owner == PlayerTurn:
            Pos[0] = field_X
            Pos[1] = field_Y
            SelectionMode = 1

    elif SelectionMode == 1:
        if Selection == 0:
            SelectionMode = 0
        elif Selection == 1:
            if hasattr(Field[Pos[1]][Pos[0]], 'atkRange'):
                SelectionMode = 2
                comment(" Select Target", " Ziel wählen")
                if hasattr(Field[Pos[1]][Pos[0]], 'rotation'):
                    laser(Pos[0], Pos[1], mark)
                else:
                    range_indicator_atk(mark)
            else:
                comment(" Can not attack", " Kann nicht angreifen")
                SelectionMode = 0
        elif Selection == 2:
            if hasattr(Field[Pos[1]][Pos[0]], 'runRange'):
                SelectionMode = 2
                comment(" Select Position", " Ziel wählen")
                range_indicator(mark)
            else:
                comment(" Can not run", " Kann nicht laufen")
                SelectionMode = 0
        elif Selection == 3:
            special()
        elif Selection == 4:
            Info = True
        else:
            SelectionMode = 2

    elif SelectionMode == 2:
        if Selection == 1:
            if hasattr(Field[Pos[1]][Pos[0]], 'rotation'):
                laser(Pos[0], Pos[1], demark)
                laser(Pos[0], Pos[1], attack)
            else:
                range_indicator_atk(demark)
                attack(field_X, field_Y)
        elif Selection == 2:
            range_indicator(demark)
            run(field_X, field_Y)

    elif SelectionMode == 3:
        if Selection == 5:
            SelectionMode = 0
            comment("", "")
        else:
            around(Pos[2], Pos[3], is_empty, mark)
            comment(" Select Position", " Ziel wählen")
            SelectionMode = 4

    elif SelectionMode == 4:
        around(Pos[2], Pos[3], is_empty, demark)
        if field_X == Pos[2] and (field_Y == Pos[3] + 1 or field_Y == Pos[3] - 1) or field_Y == Pos[3] and (
                field_X == Pos[2] + 1 or field_X == Pos[2] - 1):
            if Field[field_Y][field_X].name == "Empty":
                if Selection == 6:
                    archer = Archer(Field[Pos[1]][Pos[0]].owner)
                    Field[field_Y][field_X] = archer
                    empty = Neutral(0)
                    Field[Pos[1]][Pos[0]] = empty
                if Selection == 7:
                    knight = Knight(Field[Pos[1]][Pos[0]].owner)
                    Field[field_Y][field_X] = knight
                    empty = Neutral(0)
                    Field[Pos[1]][Pos[0]] = empty
                SelectionMode = 0
                Next = 1
            else:
                comment(" Can not spawn here", " Kein guter Platz")
        else:
            comment(" Can not spawn here", " Kein guter Platz")
        SelectionMode = 0


def in_range(x_me, y_me, x_him, y_him, ran_ge):
    if ran_ge <= 0:
        return False
    if difff(x_me, x_him) + difff(y_me, y_him) > ran_ge:
        return False
    if x_me > x_him:
        if y_me > y_him:
            if in_range_help(x_me - 1, y_me, x_him, y_him, ran_ge) or in_range_help(x_me, y_me - 1, x_him, y_him, ran_ge):
                return True
            else:
                return False
        elif y_me < y_him:
            if in_range_help(x_me - 1, y_me, x_him, y_him, ran_ge) or in_range_help(x_me, y_me + 1, x_him, y_him, ran_ge):
                return True
            else:
                return False
        elif y_me == y_him:
            if in_range_help(x_me - 1, y_me, x_him, y_him, ran_ge) or in_range_help(x_me, y_me - 1, x_him, y_him, ran_ge) \
                    or in_range_help(x_me, y_me + 1, x_him, y_him, ran_ge):
                return True
            else:
                return False
    elif x_me < x_him:
        if y_me > y_him:
            if in_range_help(x_me + 1, y_me, x_him, y_him, ran_ge) or in_range_help(x_me, y_me - 1, x_him, y_him, ran_ge):
                return True
            else:
                return False
        elif y_me < y_him:
            if in_range_help(x_me + 1, y_me, x_him, y_him, ran_ge) or in_range_help(x_me, y_me + 1, x_him, y_him, ran_ge):
                return True
            else:
                return False
        elif y_me == y_him:
            if in_range_help(x_me + 1, y_me, x_him, y_him, ran_ge) or in_range_help(x_me, y_me - 1, x_him, y_him, ran_ge) \
                    or in_range_help(x_me, y_me + 1, x_him, y_him, ran_ge):
                return True
            else:
                return False
    elif x_me == x_him:
        if y_me > y_him:
            if in_range_help(x_me, y_me - 1, x_him, y_him, ran_ge) or in_range_help(x_me - 1, y_me, x_him, y_him, ran_ge) \
                    or in_range_help(x_me + 1, y_me, x_him, y_him, ran_ge):
                return True
            else:
                return False
        elif y_me < y_him:
            if in_range_help(x_me, y_me + 1, x_him, y_him, ran_ge) or in_range_help(x_me - 1, y_me, x_him, y_him, ran_ge) \
                    or in_range_help(x_me + 1, y_me, x_him, y_him, ran_ge):
                return True
            else:
                return False
        elif y_me == y_him:
            return False


def in_range_help(x_me, y_me, x_him, y_him, ran_ge):
    if x_me < 0 or y_me < 0 or x_me > 18 or y_me > 18:
        return False
    if x_me == x_him and y_me == y_him and (Field[y_me][x_me].name == "Empty" \
                                            or Field[Pos[1]][Pos[0]].name == "Boy" and Field[y_me][x_me].combine
                                            and (Field[y_me][x_me].owner == 0 or Field[y_me][x_me].owner == Field[Pos[1]][Pos[0]].owner)):
        if ran_ge >= 0:
            return True
        else:
            return False
    elif Field[y_me][x_me].name == "Empty":
        if in_range(x_me, y_me, x_him, y_him, ran_ge - 1):
            return True
        else:
            return False
    else:
        return False


def range_indicator(funk):
    if Field[Pos[1]][Pos[0]].name == "Barrack":
        rrange = 1
    else:
        rrange = Field[Pos[1]][Pos[0]].runRange
    for a in range(rrange + rrange + 1):
        for b in range(rrange + rrange + 1):
            if in_range(Pos[0], Pos[1], Pos[0] + rrange - b, Pos[1] + rrange - a, rrange):
                funk(Pos[0] + rrange - b, Pos[1] + rrange - a)


def range_indicator_atk(funk):
    rrange = Field[Pos[1]][Pos[0]].atkRange
    for a in range(rrange + rrange + 1):
        for b in range(rrange + rrange + 1):
            if difff(Pos[1] + rrange - a, Pos[1]) + difff(Pos[0] + rrange - b, Pos[0]) <= rrange:
                if 0 <= Pos[1] + rrange - a <= 18 and 0 <= Pos[0] + rrange - b <= 18:
                    owner = Field[Pos[1] + rrange - a][Pos[0] + rrange - b].owner
                    if Field[Pos[1] + rrange - a][
                        Pos[0] + rrange - b].name == "Empty" or owner != PlayerTurn and owner != 0 \
                            and hasattr(Field[Pos[1] + rrange - a][Pos[0] + rrange - b], 'health'):
                        funk(Pos[0] + rrange - b, Pos[1] + rrange - a)


def laser_heal(x, y):
    if hasattr(Field[y][x], 'health'):
        Field[y][x].health += 1


def laser_self_dmg(x, y):
    if hasattr(Field[y][x], 'health'):
        Field[y][x].health -= 1
        if Field[y][x].health <= 0:
            die(x, y)


def laser(x, y, funk):
    for i in range(1,7):
        if Field[Pos[1]][Pos[0]].rotation == 0:
            funk(x, y - i)
        elif Field[Pos[1]][Pos[0]].rotation == 1:
            funk(x + i, y)
        elif Field[Pos[1]][Pos[0]].rotation == 2:
            funk(x, y + i)
        elif Field[Pos[1]][Pos[0]].rotation == 3:
            funk(x - i, y)


def in_range_laser(x, y):
    if Field[Pos[1]][Pos[0]].rotation == 0:
        if x == Pos[0] and Pos[1] > y >= Pos[1] - 6:
            return True
        else:
            return False
    if Field[Pos[1]][Pos[0]].rotation == 1:
        if y == Pos[1] and Pos[0] < x <= Pos[0] + 6:
            return True
        else:
            return False
    if Field[Pos[1]][Pos[0]].rotation == 2:
        if x == Pos[0] and Pos[1] < y <= Pos[1] + 6:
            return True
        else:
            return False
    if Field[Pos[1]][Pos[0]].rotation == 3:
        if y == Pos[1] and Pos[0] > x >= Pos[0] - 6:
            return True
        else:
            return False


def around(x, y, funk1, funk2):
    if funk1(x, y + 1):
        funk2(x, y + 1)
    if funk1(x, y - 1):
        funk2(x, y - 1)
    if funk1(x + 1, y):
        funk2(x + 1, y)
    if funk1(x - 1, y):
        funk2(x - 1, y)


def is_empty(x, y):
    if Field[y][x].name == "Empty":
        return True
    else:
        return False


def attack(x, y):
    global PlayerActions
    global Pos
    global SelectionMode
    global Next
    if attackable(x, y):
        atkRange = Field[Pos[1]][Pos[0]].atkRange
        if hasattr(Field[Pos[1]][Pos[0]], 'rotation'):
            if in_range_laser(x, y):
                Field[y][x].health -= Field[Pos[1]][Pos[0]].atk
                if Field[y][x].health <= 0:
                    die(x, y)
                if difff(y, Pos[1]) == 6 or difff(x, Pos[0]) == 6:
                    Next = 1
            else:
                comment(" Not in Range", " Nicht in Reichweite")

        elif difff(Pos[0], x) + difff(Pos[1], y) <= atkRange:
            Field[y][x].health -= Field[Pos[1]][Pos[0]].atk
            if Field[y][x].health <= 0:
                if Field[y][x].name == "Laser":
                    laser = Laser(Field[y][x].rotation, 0, False)
                    Field[y][x] = laser
                elif Field[y][x].name == "Tower":
                    tower = Tower(0)
                    Field[y][x] = tower
                else:
                    die(x, y)
            Next = 1

        else:
            comment(" Not in Range", " Nicht in Reichweite")
    else:
        comment(" No enemy", " Kein Gegner")
    SelectionMode = 0


def attackable(x, y):
    if Field[y][x].owner != PlayerTurn and Field[y][x].owner != 0 and hasattr(Field[y][x], 'health'):
        return True
    else:
        return False


def run(x, y):
    global PlayerActions
    global Pos
    global SelectionMode
    global Selection
    global Next
    rRange = Field[Pos[1]][Pos[0]].runRange
    if in_range(Pos[0], Pos[1], x, y, rRange):
        if is_empty(x, y):
            Field[y][x] = Field[Pos[1]][Pos[0]]
            die(Pos[0], Pos[1])
            SelectionMode = 0
            Next = 1
        else:
            try_combine(x, y)
    else:
        comment(" Not in range", " Nicht in Reichweite")
    if SelectionMode != 3:
        SelectionMode = 0


def try_combine(x, y):
    global Pos
    global SelectionMode
    global Selection
    global PlayerActions
    global Next
    if Field[Pos[1]][Pos[0]].name == "Boy":
        if Field[Pos[1]][Pos[0]].owner == Field[y][x].owner:
            if Field[y][x].name == "Boy":
                barrack = Building(1, Field[y][x].owner)
                Field[y][x] = barrack
                die(Pos[0], Pos[1])
                SelectionMode = 0
                Next = 1
            elif Field[y][x].name == "Barrack":
                Pos[2] = x
                Pos[3] = y
                SelectionMode = 3
                Selection = 5
            else:
                comment(" Can not go there", " Kein guter Ort")
        elif Field[y][x].name == "Tower" and Field[y][x].owner == 0:
            tower = Tower(Field[Pos[1]][Pos[0]].owner)
            tower.health = 3
            Field[y][x] = tower
            die(Pos[0], Pos[1])
            SelectionMode = 0
            Next = 1
        elif Field[y][x].name == "Laser" and Field[y][x].owner == 0:
            laser = Laser(Field[y][x].rotation, Field[Pos[1]][Pos[0]].owner, False)
            laser.health = 3
            Field[y][x] = laser
            die(Pos[0], Pos[1])
            SelectionMode = 0
            Next = 1
        else:
            comment(" Can not go there", " Kein guter Ort")
    else:
        comment(" Can not go there", " Kein guter Ort")
    if SelectionMode != 3:
        SelectionMode = 0


def special():
    global SelectionMode
    global PlayerActions
    global Next
    rand = random.randint(1, 6)

    if Field[Pos[1]][Pos[0]].name == "Boy":
        if rand == 6:
            Field[Pos[1]][Pos[0]].atk = 6
            range_indicator_atk(attack)
            Field[Pos[1]][Pos[0]].atk = 1
            comment(" Bäääääääm", " Bäääääääm")
        else:
            comment(" He just died...", " Ein weiterer sinnloser Tod")
        die(Pos[0], Pos[1])

    elif Field[Pos[1]][Pos[0]].name == "Barrack":
        if rand < 4:
            knight = Knight(Field[Pos[1]][Pos[0]].owner)
            Field[Pos[1]][Pos[0]] = knight
            comment(" It's a Knight", " Ein Ritter")
        else:
            archer = Archer(Field[Pos[1]][Pos[0]].owner)
            Field[Pos[1]][Pos[0]] = archer

    elif Field[Pos[1]][Pos[0]].name == "Base":
        comment(" Nothing Spezial", " Kann nix")
        PlayerActions += 1

    elif Field[Pos[1]][Pos[0]].name == "BaseLaser" or Field[Pos[1]][Pos[0]].name == "Laser":
        if rand < 5:
            laser(Pos[0], Pos[1], laser_heal)
            comment(" Good Laser", " Guter Laser")
        else:
            laser(Pos[0], Pos[1], laser_self_dmg)
            comment(" Bad Laser", " Böser Laser")

    elif Field[Pos[1]][Pos[0]].name == "Tower":
        comment(" Nothing Spezial", " Kann nix")
        PlayerActions += 1

    elif Field[Pos[1]][Pos[0]].name == "Archer":
        if rand == 1:
            Field[Pos[1]][Pos[0]].atk = rand
            comment(" Less demage, less good", " Weniger Schaden, weniger gut")
        elif 1 < rand < 4:
            Field[Pos[1]][Pos[0]].atk = rand + 1
            comment(" More demage", " Mehr Schaden")
        elif rand == 4:
            Field[Pos[1]][Pos[0]].atkRange = 3
            comment(" Less range, less good", " Weniger Reichweite, weniger gut")
        else:
            Field[Pos[1]][Pos[0]].atkRange = rand
            comment(" More range", " Mehr Reichweite")

    elif Field[Pos[1]][Pos[0]].name == "Knight":
        if rand < 3:
            Field[Pos[1]][Pos[0]].health += rand
            comment(" More health", " Mehr Leben")
        elif rand == 3:
            Field[Pos[1]][Pos[0]].health -= 1
            comment(" Less health, less good", " Weniger Leben, weniger gut")
        else:
            range_indicator_atk(attack)
            comment(" 1 Spin, 1 Win", " 1 Spin, 1 Win")
    Next = 2
    SelectionMode = 0


def info():
    if Pos[6] < 19:
        obj = Field[Pos[7]][Pos[6]]
    else:
        obj = Field[Pos[7]][18]
    if English:
        screen.blit(pygame.image.frombuffer(obj.img_en, (320, 320), "RGBA"), (800, 400))
    else:
        screen.blit(pygame.image.frombuffer(obj.img_de, (320, 320), "RGBA"), (800, 400))


def language():
    global English
    if English:
        neutral = Neutral(5)
        Field[18][16] = neutral
        English = False
    else:
        neutral = Neutral(4)
        Field[18][16] = neutral
        English = True


def next_turn():
    global PlayerTurn
    global PlayerActions
    global SelectionMode
    global Fieldclones
    for i in range(10):
        Fieldclones[i] = 0
    PlayerTurn = PlayerTurn % 4 + 1
    if Lost[PlayerTurn - 1]:
        PlayerTurn += 1
    PlayerActions = 3
    SelectionMode = 0
    Field[18][18].img = pygame.image.tostring(NextImg[0], "RGBA")

    if PlayerTurn == 1:
        if Field[8][0].owner == 0:
            blue_boy1 = Boy(PlayerTurn)
            Field[8][0] = blue_boy1
        if Field[10][0].owner == 0:
            blue_boy2 = Boy(PlayerTurn)
            Field[10][0] = blue_boy2
    if PlayerTurn == 2:
        if Field[0][8].owner == 0:
            purple_boy = Boy(PlayerTurn)
            Field[0][8] = purple_boy
        if Field[0][10].owner == 0:
            purple_boy = Boy(PlayerTurn)
            Field[0][10] = purple_boy
    if PlayerTurn == 3:
        if Field[8][18].owner == 0:
            orange_boy = Boy(PlayerTurn)
            Field[8][18] = orange_boy
        if Field[10][18].owner == 0:
            orange_boy = Boy(PlayerTurn)
            Field[10][18] = orange_boy
    if PlayerTurn == 4:
        if Field[18][8].owner == 0:
            green_boy = Boy(PlayerTurn)
            Field[18][8] = green_boy
        if Field[18][10].owner == 0:
            green_boy = Boy(PlayerTurn)
            Field[18][10] = green_boy
    safe_field(True)


def next_turn_wait():
    global SelectionMode
    #comment(" Press next round", " Nächste Runde")
    Field[18][18].img = pygame.image.tostring(NextImg[PlayerTurn], "RGBA")
    SelectionMode = -1


def next_action(safe):
    global PlayerActions
    global Fieldclones
    print_field()
    PlayerActions -= 1
    if safe:
        safe_field(True)
    else:
        safe_field(False)


def safe_field(safe):
    Fieldclones[PlayerActions] = copy.deepcopy(Field)
    if not safe:
        Fieldclones[PlayerActions + 1] = 0


def load():
    global Field
    global Selection
    global PlayerActions
    Selection = 0
    if Fieldclones[PlayerActions + 1] == 0:
        comment(" No", " Nein")
    else:
        Field = copy.deepcopy(Fieldclones[PlayerActions + 1])
        PlayerActions += 1


def lose():
    global Lost
    if not Lost[0]:
        if Field[9][0].health <= 0:
            Lost[0] = True
            cleanup(1)
    if not Lost[1]:
        if Field[0][9].health <= 0:
            Lost[1] = True
            cleanup(2)
    if not Lost[2]:
        if Field[9][18].health <= 0:
            Lost[2] = True
            cleanup(3)
    if not Lost[3]:
        if Field[18][9].health <= 0:
            Lost[3] = True
            cleanup(4)


def cleanup(owner):
    for x in range(18):
        for y in range(18):
            if Field[y][x].owner == owner:
                die(x, y)
    comment("Player " + str(owner) + " lost", "Spieler " + str(owner) + " verliert")


def die(x, y):
    lose()
    if Field[y][x].name == "Tower":
        tower = Tower(0)
        Field[y][x] = tower
    elif Field[y][x].name == "Laser":
        laser = Laser(Field[y][x].rotation, 0, False)
        Field[y][x] = laser
    else:
        empty = Neutral(0)
        Field[y][x] = empty


def write():
    info()
    if Pos[6] < 19:
        obj = Field[Pos[7]][Pos[6]]
    else:
        obj = Field[Pos[7]][18]
    if hasattr(obj, 'health'):
        str_health = str(obj.health)
    else:
        str_health = "/"
    if hasattr(obj, 'atk'):
        str_attack = str(obj.atk)
    else:
        str_attack = "/"
    if hasattr(obj, 'atkRange'):
        str_atkrange = str(obj.atkRange)
    else:
        str_atkrange = "/"
    if hasattr(obj, 'runRange'):
        str_runrange = str(obj.runRange)
    else:
        str_runrange = "/"
    if English:
        Texts[0] = font.render('Player: ' + StrTurn + '  ', True, Colors[5], Colors[PlayerTurn])
        Texts[1] = font.render('Moves: ' + StrMoves + '  ', True, Colors[5], Colors[PlayerTurn])
        Texts[2] = font.render(obj.name + '  ', True, Colors[5], Colors[obj.owner])
        Texts[3] = font.render('Health: ' + str_health + '  ', True, Colors[5], Colors[obj.owner])
        Texts[4] = font.render('Attack: ' + str_attack + '  ', True, Colors[5], Colors[obj.owner])
        Texts[5] = font.render('AtkRange: ' + str_atkrange + '  ', True, Colors[5], Colors[obj.owner])
        Texts[6] = font.render('RunRange: ' + str_runrange + '  ', True, Colors[5], Colors[obj.owner])
    else:
        Texts[0] = font.render('Spieler: ' + StrTurn + '  ', True, Colors[5], Colors[PlayerTurn])
        Texts[1] = font.render('Züge: ' + StrMoves + '  ', True, Colors[5], Colors[PlayerTurn])
        Texts[2] = font.render(obj.name_ger + '  ', True, Colors[5], Colors[obj.owner])
        Texts[3] = font.render('Leben: ' + str_health + '  ', True, Colors[5], Colors[obj.owner])
        Texts[4] = font.render('Angriff: ' + str_attack + '  ', True, Colors[5], Colors[obj.owner])
        Texts[5] = font.render('Angriffsreichweite: ' + str_atkrange + '  ', True, Colors[5], Colors[obj.owner])
        Texts[6] = font.render('Laufreichweite: ' + str_runrange + '  ', True, Colors[5], Colors[obj.owner])
    for i in range(7):
        TextRect[i] = Texts[i].get_rect()
    TextRect[0].topleft = (760, 5)
    TextRect[1].topright = (1200, 5)
    TextRect[2].topright = (1130, 100)
    TextRect[3].topright = (1190, 150)
    TextRect[4].topright = (1190, 200)
    TextRect[5].topright = (1190, 250)
    TextRect[6].topright = (1190, 300)
    for j in range(7):
        screen.blit(Texts[j], TextRect[j])
    screen.blit(pygame.image.frombuffer(obj.img, (40, 40), "RGBA"), (1150, 97))

    commentFont = font.render(CommentText, True, Colors[5], Colors[0])
    commentRect = commentFont.get_rect()
    commentRect.topleft = (760, 724)
    screen.blit(commentFont, commentRect)


def select_move(x, y, a, b, c):
    obj = Field[Pos[1]][Pos[0]]
    global Selectrect
    if English:
        Textselect[0] = selectionfont.render('   Run   ', True, Colors[PlayerTurn], Colors[6 + a])
        Textselect[1] = selectionfont.render(' Attack ', True, Colors[PlayerTurn], Colors[6 + b])
        Textselect[2] = selectionfont.render('Spezial', True, Colors[PlayerTurn], Colors[6 + c])
        Textselect[3] = selectionfont.render('Archer', True, Colors[PlayerTurn], Colors[6 + a])
        Textselect[4] = selectionfont.render('Knight', True, Colors[PlayerTurn], Colors[6 + b])
    else:
        Textselect[0] = selectionfont.render('Laufen ', True, Colors[PlayerTurn], Colors[6 + a])
        Textselect[1] = selectionfont.render('Angriff ', True, Colors[PlayerTurn], Colors[6 + b])
        Textselect[2] = selectionfont.render('Spezial', True, Colors[PlayerTurn], Colors[6 + c])
        Textselect[4] = selectionfont.render(' Ritter', True, Colors[PlayerTurn], Colors[6 + a])
        Textselect[5] = selectionfont.render('Schütze', True, Colors[PlayerTurn], Colors[6 + b])
    for i in range(5):
        Selectrect[i] = Textselect[0].get_rect()
    if SelectionMode == 1:
        run = atk = 0
        invert = 1
        if hasattr(obj, 'runRange'):
            run = 1
        if hasattr(obj, 'atkRange'):
            atk = 1
        if Pos[1] > 16:
            invert = -1

        if run == 1:
            Selectrect[0].topleft = (x, y)
            screen.blit(Textselect[0], Selectrect[0])
        if atk == 1:
            Selectrect[1].topleft = (x, y + (21 * run) * invert)
            screen.blit(Textselect[1], Selectrect[1])
        Selectrect[2].topleft = (x, y + (21 * (run + atk)) * invert)
        screen.blit(Textselect[2], Selectrect[2])
    if SelectionMode == 3:
        Selectrect[3].topleft = (x, y)
        screen.blit(Textselect[3], Selectrect[3])
        Selectrect[4].topleft = (x, y + 21)
        screen.blit(Textselect[4], Selectrect[4])


def maybe():
    global Selection
    if SelectionMode == 99:
        y_change = 0
        x_change = 0
        if SelectionMode == 1:
            multi = 2
            sel_default = 0
        else:
            multi = 1
            sel_default = 5
        if Pos[5] > 16:
            y_change = 50
        if Pos[4] > 16:
            x_change = 75
        y_change *= multi
        #selection(Selection, newMouseX - x_change, newMouseY - y_change)
        if newMouseX + 10 - x_change < mouseX < newMouseX + 75 - x_change:
            if newMouseY - y_change < mouseY < newMouseY + 50 * multi - y_change:
                diff = mouseY - (newMouseY - y_change)
                Selection = (int)((diff - (diff % 25)) / 25 + 1 + sel_default)
            else:
                Selection = sel_default
        else:
            Selection = sel_default


def comment(en, de):
    global CommentText
    if English:
        CommentText = en
    else:
        CommentText = de


def mark(x, y):
    obj = Field[y][x]
    surface = pygame.image.frombuffer(obj.img, (40, 40), "RGBA")
    w, h = surface.get_size()
    for x in range(w):
        for y in range(h):
            r = surface.get_at((x, y))[0]
            g = surface.get_at((x, y))[1]

            b = surface.get_at((x, y))[2]

            a = surface.get_at((x, y))[3]

            a -= 100
            surface.set_at((x, y), pygame.Color(r, g, b, a))


def demark(x, y):
    obj = Field[y][x]
    surface = pygame.image.frombuffer(obj.img, (40, 40), "RGBA")
    w, h = surface.get_size()
    for x in range(w):
        for y in range(h):
            r = surface.get_at((x, y))[0]
            g = surface.get_at((x, y))[1]

            b = surface.get_at((x, y))[2]

            a = surface.get_at((x, y))[3]

            a += 100
            surface.set_at((x, y), pygame.Color(r, g, b, a))


def field_init():
    global Field
    for z in range(19):
        list_help = []
        for x in range(19):
            if (z < 5 or z > 13) and (x < 5 or x > 13) or (z < 5 and (x < 5 + z or x > 13 - z)
                                                           or (4 < z < 9 and (z - 5 < x < 5 or 13 < x < 23 - z))
                                                           or (9 < z < 14 and (13 - z < x < 5 or 13 < x < z + 5))
                                                           or (z > 13 and (4 < x < 23 - z or z - 5 < x < 14))):
                list_help += [Black]
            else:
                empty = Neutral(0)
                list_help += [empty]
        Field += [list_help]
    for i in range(4):
        AllTowers[i] = Tower(0)
    Field[5][5] = AllTowers[0]
    Field[5][13] = AllTowers[1]
    Field[13][5] = AllTowers[2]
    Field[13][13] = AllTowers[3]
    midtower = MidTower(0)
    Field[9][9] = midtower
    for j in range(5):
        for k in range(4):
            AllLasers[j * 4 + k] = Laser(k, j, False)
    Field[8][9] = AllLasers[0]
    Field[9][10] = AllLasers[1]
    Field[10][9] = AllLasers[2]
    Field[9][8] = AllLasers[3]
    # BaseLasers
    blue_laser = Laser(1, 1, True)
    Field[9][1] = blue_laser
    purple_laser = Laser(2, 2, True)
    Field[1][9] = purple_laser
    orange_laser = Laser(3, 3, True)
    Field[9][17] = orange_laser
    green_laser = Laser(0, 4, True)
    Field[17][9] = green_laser
    base_blue = Building(0, 1)
    Field[9][0] = base_blue     # base
    base_purple = Building(0, 2)
    Field[0][9] = base_purple
    base_orange = Building(0, 3)
    Field[9][18] = base_orange
    base_green = Building(0, 4)
    Field[18][9] = base_green
    next = Neutral(2)
    Field[18][18] = next
    back = Neutral(3)
    Field[18][17] = back
    neutral = Neutral(4)
    Field[18][16] = neutral


def print_field():
    for i in range(19):
        for z in range(19):
            value = Field[i][z].img
            screen.blit(pygame.image.frombuffer(value, (40, 40), "RGBA"), (z * 40, i * 40))


# Game_loop
field_init()
next_turn()
running = True

while running:
    pygame.display.update()
    # RGB = Red Green Blue
    screen.fill((0, 0, 0))  # Black background
    StrTurn = str(PlayerTurn)
    StrMoves = str(PlayerActions)
    lose()
    if PlayerActions == 0:
        next_turn_wait()

    print_field()

    mouseX, mouseY = pygame.mouse.get_pos()
    Pos[6] = (int)((mouseX - (mouseX % 40)) / 40)
    Pos[7] = (int)((mouseY - (mouseY % 40)) / 40)
    write()
    # looks for events(pressing keys, ...)
    for event in pygame.event.get():
        if Next == 1:
            next_action(True)
        elif Next == 2:
            next_action(False)
        Next = 0
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if event.button == 1:                                                   # if left Mousebutton is pressed
                comment("", "")
                Info = False
                newMouseX, newMouseY = pygame.mouse.get_pos()
                fieldX = (int)((newMouseX - (newMouseX % 40)) / 40)
                fieldY = (int)((newMouseY - (newMouseY % 40)) / 40)
                #if fieldX == fieldY == 0:
                 #   PlayerActions += 1
                if fieldX < 19 or SelectionMode == 1 or SelectionMode == 3:
                    Pos[4] = fieldX
                    Pos[5] = fieldY
                    select(fieldX, fieldY)

    if SelectionMode == 1 or SelectionMode == 3:
        a = b = c = 0
        select_move(newMouseX, newMouseY, a, b, c)
        if Selectrect[0].collidepoint(mouseX, mouseY):
            a = 1
            Selection = 2
        elif Selectrect[1].collidepoint(mouseX, mouseY):
            b = 1
            Selection = 1
        elif Selectrect[2].collidepoint(mouseX, mouseY):
            c = 1
            Selection = 3
        elif Selectrect[3].collidepoint(mouseX, mouseY):
            a = 1
            Selection = 6
        elif Selectrect[4].collidepoint(mouseX, mouseY):
            b = 1
            Selection = 7
        else:
            Selection = 0
        select_move(newMouseX, newMouseY, a, b, c)

    if Field[8][9].owner != 0 and Field[8][9].owner == Field[10][9].owner == Field[9][8].owner == Field[9][10].owner:
        tower = MidTower(Field[8][9].owner)
        Field[9][9] = tower
    else:
        tower = MidTower(0)
        Field[9][9] = tower


