import random
import sys
import time
import json
from ast import literal_eval
from math import dist
from typing import List, Type
from utils.components import Posx1x2y1y2, UiElement

import chaos_const
from utils.gamehelper import Entity, Poe2Bot

# readabilty
poe_bot: Poe2Bot

default_config = {
    "REMOTE_IP": "127.0.0.1",  # z2
    "unique_id": "poe_2_test_chaos",
    "build": "InfernalistMinion",
    "max_lvl": 101,
    "chromatics_recipe": True,
    "force_reset_temp": False,
}

try:
    i = sys.argv[1]
    print(i)
    parsed_config = literal_eval(i)
    print("successfully parsed cli config")
    print(f"parsed_config: {parsed_config}")
except:
    print("cannot parse config from cli, using default\dev one")
    notebook_dev = True
    parsed_config = default_config

config = {}

for key in default_config.keys():
    config[key] = parsed_config.get(key, default_config[key])

print(f"config to run {config}")

REMOTE_IP = config["REMOTE_IP"]  # REMOTE_IP
UNIQUE_ID = config["unique_id"]  # unique id
MAX_LVL = config.get("max_lvl")
CHROMATICS_RECIPE = config["chromatics_recipe"]
BUILD_NAME = config["build"]  # build_name
force_reset_temp = config["force_reset_temp"]
print(
    f"running aqueduct using: REMOTE_IP: {REMOTE_IP} unique_id: {UNIQUE_ID} max_lvl: {MAX_LVL} chromatics_recipe: {CHROMATICS_RECIPE} force_reset_temp: {force_reset_temp}"
)

# In[ ]:


poe_bot = Poe2Bot(unique_id=UNIQUE_ID, remote_ip=REMOTE_IP)
from utils.combat import InfernalistMinion
poe_bot.combat_module.build = InfernalistMinion(poe_bot)
# panel = poe_bot.backend.getChaosPanel()
# panel = poe_bot.backend.getItemsOnGround()
# panel11 = poe_bot.backend.getUltimatumNextWaveUi()
# panel = poe_bot.backend.getVisibleUi()
# print(f'pppp===={panel}')
poe_bot.refreshAll()

# poe_bot.game_data.terrain.getCurrentlyPassableArea()
# TODO move it to poe_bot.refreshAll() refreshed_data["c_t"] ## "c_t":0 - mouse || "c_t":1 - wasd
poe_bot.mover.setMoveType("wasd")


# open portal and enter it
def openWaypoint():
    poe_bot.bot_controls.releaseAll()
    # 去入口对我
    poe_bot.refreshInstanceData()
    waypoint5_entity = next((e for e in poe_bot.game_data.entities.all_entities if e.render_name == "Waypoint 5"))
    poe_bot.mover.goToEntitysPoint(waypoint5_entity, release_mouse_on_end=False)

    pos_x = waypoint5_entity.location_on_screen.x
    pos_y = waypoint5_entity.location_on_screen.y
    pos_x, pos_y = poe_bot.convertPosXY(pos_x, pos_y, safe=False)
    # 点击
    poe_bot.bot_controls.mouse.setPosSmooth(pos_x, pos_y)
    time.sleep(random.randint(40, 80) / 100)
    poe_bot.bot_controls.mouse.click()
    time.sleep(random.randint(30, 60) / 100)


def find_text_open(obj, text):
    results = []
    if isinstance(obj, dict):  # 处理字典
        if text in obj.get("text"):
            results.append(obj)
        for key in obj:
            results.extend(find_text_open(obj[key], text))

    elif isinstance(obj, list):  # 处理列表
        for item in obj:
            results.extend(find_text_open(item, text))

    return results


def clickTheChaosBtn():
    visibleUiJson = poe_bot.backend.getVisibleUi()
    text_open = find_text_open(visibleUiJson, "close")
    if text_open:
        open_objects = text_open[0]
        time.sleep(random.randint(1, 3))
        pos_x, pos_y = open_objects["gp"][0], open_objects["gp"][1]
        screen_pos_x, screen_pos_y = poe_bot.convertPosXY(pos_x, pos_y, safe=False)
        time.sleep(random.randint(1, 3))
        poe_bot.bot_controls.mouse.setPosSmooth(int(screen_pos_x), int(screen_pos_y), mouse_speed_mult=1)
        time.sleep(random.randint(1, 3))
        poe_bot.bot_controls.mouse.click()

        time.sleep(random.randint(2, 4))
        poe_bot.bot_controls.mouse.click()
        # sz_ = open_objects["v_b_sz"]
        # time.sleep(random.randint(1, 3))
        # UiElement(poe_bot, Posx1x2y1y2(*sz_)).click()
        return True
    else:
        openText = find_text_open(visibleUiJson, "open")
        if openText:
            open_objects = openText[0]
            time.sleep(random.randint(1, 3))
            pos_x, pos_y = open_objects["gp"][0], open_objects["gp"][1]
            screen_pos_x, screen_pos_y = poe_bot.convertPosXY(pos_x, pos_y, safe=False)
            time.sleep(random.randint(1, 3))
            poe_bot.bot_controls.mouse.setPosSmooth(int(screen_pos_x), int(screen_pos_y), mouse_speed_mult=1)
            time.sleep(random.randint(1, 3))
            poe_bot.bot_controls.mouse.click()
            return True
    return False


def openChaosEntren():
    poe_bot.bot_controls.releaseAll()
    # 去入口对我
    # "Metadata/Terrain/Gallows/Act3/3_10/Objects/UltimatumEntrancePedestal"
    waypoint5_entity = next((e for e in poe_bot.game_data.entities.all_entities if
                             e.path == "Metadata/Terrain/Gallows/Act3/3_10/Objects/UltimatumEntrancePedestal"))
    if waypoint5_entity:
        poe_bot.mover.goToEntitysPoint(waypoint5_entity, release_mouse_on_end=True)
        pos_x = waypoint5_entity.location_on_screen.x
        pos_y = waypoint5_entity.location_on_screen.y
        pos_x, pos_y = poe_bot.convertPosXY(pos_x, pos_y, safe=False)
        # 点击dw
        poe_bot.bot_controls.mouse.setPosSmooth(pos_x, pos_y)
        time.sleep(random.randint(40, 80) / 100)
        poe_bot.bot_controls.mouse.click()
        time.sleep(random.randint(2, 3))

        poe_bot.ui.inventory.update()
        simulacrum_item = next((i for i in poe_bot.ui.inventory.items if i.name == "Inscribed Ultimatum"), None)
        if simulacrum_item is None:
            poe_bot.ui.closeAll()
            # self.cache.reset()
            raise Exception("no Ultimatum in inventory during map activation")
            poe_bot.raiseLongSleepException("no simulacrums in inventory")
        time.sleep(random.randint(1, 2))
        simulacrum_item.click(hold_ctrl=True)
        time.sleep(random.randint(1, 2))
        # 点击按钮
        btnOk = clickTheChaosBtn()
        if not btnOk:
            raise Exception("clickTheChaosBtn failed")
        time.sleep(random.randint(1, 3))
        #开门后进去
        poe_bot.refreshInstanceData()
        ultimatumEntrance_entity = next((e for e in poe_bot.game_data.entities.all_entities if
                                 e.path == "Metadata/Terrain/Gallows/Act3/3_10/Objects/UltimatumEntrance"))
        if ultimatumEntrance_entity:
            poe_bot.bot_controls.releaseAll()
            poe_bot.mover.goToEntitysPoint(ultimatumEntrance_entity, release_mouse_on_end=True)
            pos_x = ultimatumEntrance_entity.location_on_screen.x
            pos_y = ultimatumEntrance_entity.location_on_screen.y
            pos_x, pos_y = poe_bot.convertPosXY(pos_x, pos_y, safe=False)
            # 点击dw
            poe_bot.bot_controls.mouse.setPosSmooth(pos_x, pos_y)
            time.sleep(random.randint(40, 80) / 100)
            poe_bot.bot_controls.mouse.click()
            time.sleep(random.randint(2, 3))
        else:
            raise Exception("ultimatumEntrance_entity failed")

def GoAndClick(path ,click):
    waypoint5_entity = next((e for e in poe_bot.game_data.entities.all_entities if
                             e.path == path), None)
    if waypoint5_entity:
        poe_bot.mover.goToEntitysPoint(waypoint5_entity,min_distance=5, release_mouse_on_end=True)
        if click:
            pos_x = waypoint5_entity.location_on_screen.x
            pos_y = waypoint5_entity.location_on_screen.y
            pos_x, pos_y = poe_bot.convertPosXY(pos_x, pos_y, safe=False)
            # 点击dw
            poe_bot.bot_controls.mouse.setPosSmooth(pos_x, pos_y)
            time.sleep(random.randint(3, 5) )
            poe_bot.bot_controls.mouse.click()
            time.sleep(random.randint(2, 3))
    else:
        raise Exception("GoAndClick failed")
def findNpc():
    poe_bot.refreshInstanceData()
    ultimatumSelector_entity = next((e for e in poe_bot.game_data.entities.all_entities if
                                     e.path == chaos_const.UltimatumNPC),None)
    if ultimatumSelector_entity:
        poe_bot.bot_controls.releaseAll()
        poe_bot.mover.goToEntitysPoint(ultimatumSelector_entity, release_mouse_on_end=True)
        # pos_x = ultimatumSelector_entity.location_on_screen.x
        # pos_y = ultimatumSelector_entity.location_on_screen.y
        # pos_x, pos_y = poe_bot.convertPosXY(pos_x, pos_y, safe=False)
        # # 点击dw
        # poe_bot.bot_controls.mouse.setPosSmooth(pos_x, pos_y)
        # time.sleep(random.randint(40, 80) / 100)
        # poe_bot.bot_controls.mouse.click()
        time.sleep(random.randint(2, 3))


    else:
        raise Exception("ultimatumSelector_entity failed")
    pass

def killMonster():

    if len(poe_bot.game_data.entities.attackable_entities)>0:
        rares_ = poe_bot.game_data.entities.attackable_entities[0]
        point = poe_bot.mover.goToEntitysPoint(rares_,
                                               release_mouse_on_end=True)
        time.sleep(random.randint(1, 2))
    while True:
        time.sleep(random.randint(30, 50)/100)
        poe_bot.refreshInstanceData()
        mob_to_kill = next(
            (e for e in poe_bot.game_data.entities.attackable_entities if e.isOnPassableZone()), None)
        if mob_to_kill:
            res = True
            while res is not None:
                res = poe_bot.mover.goToEntitysPoint(mob_to_kill,
                                                     custom_break_function=poe_bot.loot_picker.collectLoot)
                mob_to_kill = next(
                    (e for e in poe_bot.game_data.entities.attackable_entities if
                     e.id == mob_to_kill.id and e.isOnPassableZone()), None
                )
                if mob_to_kill is None:
                    continue
            if mob_to_kill is not None:
                poe_bot.combat_module.killUsualEntity(mob_to_kill)

        else:
            time.sleep(random.randint(30, 50) / 100)
            break


def selectChoose():
    visibleUiJson = poe_bot.backend.getItemsOnGround()
    findFirst=False
    for s in chaos_const.choose_select_first:
        text_open = find_text_open(visibleUiJson, s)
        if text_open:
            open_objects = text_open[0]
            time.sleep(random.randint(1, 3))
            pos_x, pos_y = open_objects["gp"][0], open_objects["gp"][1]
            screen_pos_x, screen_pos_y = poe_bot.convertPosXY(pos_x, pos_y, safe=False)
            time.sleep(random.randint(1, 3))
            poe_bot.bot_controls.mouse.setPosSmooth(int(screen_pos_x), int(screen_pos_y), mouse_speed_mult=1)
            time.sleep(random.randint(1, 3))
            poe_bot.bot_controls.mouse.click()
            findFirst=True
            break

    for s in chaos_const.choose_select:
        text_open = find_text_open(visibleUiJson, s)
        if text_open:
            open_objects = text_open[0]
            time.sleep(random.randint(1, 3))
            pos_x, pos_y = open_objects["gp"][0], open_objects["gp"][1]
            screen_pos_x, screen_pos_y = poe_bot.convertPosXY(pos_x, pos_y, safe=False)
            time.sleep(random.randint(1, 3))
            poe_bot.bot_controls.mouse.setPosSmooth(int(screen_pos_x), int(screen_pos_y), mouse_speed_mult=1)
            time.sleep(random.randint(1, 3))
            poe_bot.bot_controls.mouse.click()
            findFirst=True
            break

    if not findFirst:
        raise Exception("chooseSelect choose failed")
    time.sleep(random.randint(1, 2))
    text_open = find_text_open(visibleUiJson, "begin")
    if text_open:
        open_objects = text_open[0]
        time.sleep(random.randint(1, 3))
        pos_x, pos_y = open_objects["gp"][0], open_objects["gp"][1]
        screen_pos_x, screen_pos_y = poe_bot.convertPosXY(pos_x, pos_y, safe=False)
        time.sleep(random.randint(1, 3))
        poe_bot.bot_controls.mouse.setPosSmooth(int(screen_pos_x), int(screen_pos_y), mouse_speed_mult=1)
        time.sleep(random.randint(1, 3))
        poe_bot.bot_controls.mouse.click()
    else:
        raise Exception("chooseSelect begin failed")
# 打开传送
#openWaypoint()
#
# poe_bot.refreshInstanceData()
#
openChaosEntren()
time.sleep(random.randint(3, 4) )
GoAndClick(chaos_const.UltimatumSelector,False)
# 选择
selectChoose()
#

# 第一关 下降台子
visibleUiJson = poe_bot.backend.getVisibleUi()
GoAndClick("Metadata/Terrain/Gallows/Act3/3_10/Objects/LiftButton",True)

killMonster()
#走到升旗平台
GoAndClick(chaos_const.LiftButton_Platform,False)
time.sleep(random.randint(30, 50) / 100)
findNpc()

raise 404






test_entity = next(
    (
        e
        for e in poe_bot.game_data.entities.all_entities
        if
        e.path == 'Metadata/NPC/League/Ultimatum/UltimatumNPC'
    ),
    None,
)
# 'Metadata/Terrain/Gallows/Act3/3_10/Objects/LiftButton'
# 'Metadata/MiscellaneousObjects/WorldItem'
if test_entity:
    poe_bot.mover.goToEntitysPoint(test_entity, min_distance=10)
    print('DONE')
time.sleep(10)
