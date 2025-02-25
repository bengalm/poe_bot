




#
UltimatumEntrancePedestal="Metadata/Terrain/Gallows/Act3/3_10/Objects/UltimatumEntrancePedestal"
# 门
DoorExit="Metadata/Terrain/Gallows/Act3/3_10/Objects/DoorExit"

#把手
LiftButton="Metadata/Terrain/Gallows/Act3/3_10/Objects/LiftButton"

# 回去的 点
LiftMovementController_EntranceDescendOnce="Metadata/Terrain/Gallows/Act3/3_10/Objects/LiftMovementController_EntranceDescendOnce"
# 下一个点
LiftMovementController_UpDisabledUntilComplete='Metadata/Terrain/Gallows/Act3/3_10/Objects/LiftMovementController_UpDisabledUntilComplete'
# npc
UltimatumNPC="Metadata/NPC/League/Ultimatum/UltimatumNPC"

# 选择
UltimatumSelector="Metadata/Terrain/Gallows/Act3/3_10/Objects/UltimatumSelector"
# 起来的平台
LiftPlatform='Metadata/Terrain/Gallows/Act3/3_10/Objects/LiftPlatform'
LiftButton_Platform='Metadata/Terrain/Gallows/Act3/3_10/Objects/LiftButton_Platform'

#
#'Metadata/Terrain/Gallows/Act3/3_10/Objects/UltimatumSelector'




choose_select=[
    'Reduced Recovery',#減少回復 #減少 40% 生命、魔力和能量護盾恢復率
    'Lessened Reach',#縮小範圍 #50% 更少效果範圍和投射物速度
    'Time Paradox',#時間悖論 #增益效果失效加快 3 倍，減益效果的消退速度減慢 3 倍
    'Damaged Defences',#受損防禦 #40% 更少防禦
    'Reduced Resistances',#減少抗性 #元素抗性 -15%，最大元素抗性 -10%
    'Drought',#乾旱 #怪物死亡後不會給予藥劑和護符充能
    'Escalating Damage Taken',#增加承受傷害 #在每個事件房間中，每秒慢慢增加 1% 承受的傷害，最多 50%
    'Monster Speed',#怪物速度 #怪物增加 20% 技能速度
    'Chaotic Monsters',#混沌怪物 #怪物獲得相當於傷害 20% 的額外混沌傷害
    'Deadly Monsters',#致命怪物 #怪物的暴擊機率增加 300%
    'Toxic Monsters',#劇毒怪物 #怪物的擊中必定造成流血和中毒
    'Resistant Monsters',#抗性怪物 #怪物 +40% 全部抗性
    'Unstoppable Monsters',#不可阻擋怪物 #怪物不能被緩速或暈眩
    'Shielding Monsters',#巨盾怪物 #怪物受能量護盾保護
    'Entangling Monsters',#糾纏怪物 #頭目造成更多傷害，承受更少傷害
    'Enraged Bosses',#狂怒頭目 #怪物受能量護盾保護
    'Lethal Rare Monsters',#致死稀有怪物 #稀有怪物會擁有 2 個額外的詞綴增加 30% 稀有怪物
    'Random Projectiles',#隨機投射物 #你的投射物以隨機方向發射怪物發射額外投射物
    'Occasional Impotence',#暫時失效 #每 8 秒你和你的召喚物有 2 秒不會造成傷害
    'Volatile Fiends',#易爆惡魔 #怪物在死亡時釋放致命的易爆物 。稀有怪物留下的易爆物更大
    'Heart Tethers',#心靈束縛 #出現會施加束縛的心臟，使你受到緩速。掙脫束縛會使你暈眩
    'Stormcaller Runes',#風暴喚者符文 #若你持續待在符文中，符文會顯現並召喚致命的閃電風暴
    'Impending Doom',#末日厄運戒指 #災厄圓環出現在地面並持續擴大，在達到最大範圍時爆炸，造成物理傷害
    'Blood Globules',#鮮血之球 #血之球體在附近顯現，對你進行追蹤。在你上方時它們會降下，造成物理傷害
    'Vaal Omnitect',#瓦爾．全能 #一台古老的瓦爾機械，會對附近的入侵者發動攻擊
    'Pyramid Beams',#金字塔光束 #錐形物體出現並投射四道旋轉的雷射，在擊中時造成腐化之血
    'Petrification Statues',#石化雕像 #挑戰區域含有數座雕像，在它們的凝視範圍中一段時間後，你會被石化
    'Blood Mist',#鮮血迷霧 #挑戰區域被鮮血迷霧覆蓋，使其中的怪物免疫傷害
    #'Stalking Shade',#潛伏暗影 #一道無敵的影子跟著你，用它的近戰擊中對你施加毀滅毀滅達到 7 層時，試煉失敗
    'Burning Turrets',#燃燒哨戒塔 #挑戰區域含有哨戒塔，週期性地向前方發射火焰投射物
    'Shocking Turrets',#感電哨戒塔 #挑戰區域含有哨戒塔，週期性地向前方發射閃電投射物
    'Temple Traps',#神殿陷阱 #挑戰區域中含有能對踩到的人造成物理傷害的尖刺
]


choose_select_first=[
        'Reduced Recovery',#減少回復 #減少 40% 生命、魔力和能量護盾恢復率
    'Lessened Reach',#縮小範圍 #50% 更少效果範圍和投射物速度
    'Time Paradox',#時間悖論 #增益效果失效加快 3 倍，減益效果的消退速度減慢 3 倍
    'Reduced Resistances',  # 減少抗性 #元素抗性 -15%，最大元素抗性 -10%
    'Drought',  # 乾旱 #怪物死亡後不會給予藥劑和護符充能
    'Monster Speed',  # 怪物速度 #怪物增加 20% 技能速度
    'Chaotic Monsters',  # 混沌怪物 #怪物獲得相當於傷害 20% 的額外混沌傷害
    'Deadly Monsters',  # 致命怪物 #怪物的暴擊機率增加 300%
    'Toxic Monsters',  # 劇毒怪物 #怪物的擊中必定造成流血和中毒
    'Resistant Monsters',  #抗性怪物 #怪物 +40% 全部抗性
    'Shielding Monsters',  # 巨盾怪物 #怪物受能量護盾保護
    'Random Projectiles',  # 隨機投射物 #你的投射物以隨機方向發射怪物發射額外投射物
    'Lethal Rare Monsters',  # 致死稀有怪物 #稀有怪物會擁有 2 個額外的詞綴增加 30% 稀有怪物
    'Entangling Monsters',  # 糾纏怪物 #頭目造成更多傷害，承受更少傷害
    'Heart Tethers',  # 心靈束縛 #出現會施加束縛的心臟，使你受到緩速。掙脫束縛會使你暈眩
    'Enraged Bosses',  # 狂怒頭目 #怪物受能量護盾保護

]