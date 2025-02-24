import random
import sys
import time
from ast import literal_eval
from math import dist
from typing import List, Type

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
# panel = poe_bot.backend.getChaosPanel()
panel = poe_bot.backend.getVisibleUi()
print(f'pppp===={panel}')
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


def openChaosEntren():
    poe_bot.bot_controls.releaseAll()
    # 去入口对我
    # "Metadata/Terrain/Gallows/Act3/3_10/Objects/UltimatumEntrancePedestal"
    waypoint5_entity = next((e for e in poe_bot.game_data.entities.all_entities if e.path == "Metadata/Terrain/Gallows/Act3/3_10/Objects/UltimatumEntrancePedestal"))

    if waypoint5_entity:
        poe_bot.mover.goToEntitysPoint(waypoint5_entity, release_mouse_on_end=True)
        pos_x = waypoint5_entity.location_on_screen.x
        pos_y = waypoint5_entity.location_on_screen.y
        pos_x, pos_y = poe_bot.convertPosXY(pos_x, pos_y, safe=False)
        # 点击dw
        poe_bot.bot_controls.mouse.setPosSmooth(pos_x, pos_y)
        time.sleep(random.randint(40, 80) / 100)
        poe_bot.bot_controls.mouse.click()
        time.sleep(random.randint(30, 60) / 100)
        time.sleep(random.randint(2, 3) )

        poe_bot.ui.inventory.update()
        simulacrum_item = next((i for i in poe_bot.ui.inventory.items if i.name == "Simulacrum"), None)
        if simulacrum_item is None:
            poe_bot.ui.closeAll()
            # self.cache.reset()
            raise Exception("no simulacrums in inventory during map activation")
            poe_bot.raiseLongSleepException("no simulacrums in inventory")

        simulacrum_item.click(hold_ctrl=True)
        time.sleep(random.randint(1,3))



# 打开传送
# openWaypoint()
#
# poe_bot.refreshInstanceData()
#
openChaosEntren()




test_entity = next(
    (
        e
        for e in poe_bot.game_data.entities.all_entities
        if
        e.path =='Metadata/NPC/League/Ultimatum/UltimatumNPC'
    ),
    None,
)
# 'Metadata/Terrain/Gallows/Act3/3_10/Objects/LiftButton'
# 'Metadata/MiscellaneousObjects/WorldItem'
if test_entity:
    poe_bot.mover.goToEntitysPoint(test_entity, min_distance=10)
    print('DONE')
time.sleep(10)