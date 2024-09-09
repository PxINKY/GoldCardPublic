from random import random, shuffle
import discord
import os
from datetime import date
from switchcase import switch
from discord.ext import commands
from MaxEmbeds import EmbedBuilder
import time
import shutil
import cassiopeia as cass

# Opens the file and reads it for token
f = open("Token", "r")
TOKEN = (f.read())
f.close()

# Read the Key from the file
with open('Key', 'r') as f:
    key = f.read()
cass.set_riot_api_key(key=key)
f.close()

intents = discord.Intents.default()
intents.members = True
Bot = discord.Bot(intents=intents)


@Bot.event
async def on_ready():
    await Bot.change_presence(status=discord.Status.online, activity=discord.Game('UPDATED TO SLASH COMMANDS!'))
    print(f'{Bot.user} has connected to Discord!')
    for guild in Bot.guilds:
        print(f'{guild.name} - {guild.id}')
    print(f'\n{len(Bot.guilds)} Servers in total!:\nRandom Roll Master Loaded!')

#for filename in os.listdir("./cogs"):
#    if filename.endswith(".py"):
#        Bot.get_cog(f'cogs.{filename[: - 3]}')

# ----------------------
# - Champion Name List -
# ----------------------
ChampionName = []
with open('resources/RuleSets/ChampionNames.txt') as f:
    lines = f.readlines()
    ChampionName += lines
# ----------------------
# - Champion Quip List -
# ----------------------
ChampionQuip = []
with open('resources/RuleSets/ChampionQuips.txt') as f:
    lines = f.readlines()
    ChampionQuip += lines
# --------------
# - Boots List -
# --------------
NormBoots = ["Berserker's Greaves", "Mobility Boots", "Plated Steelcaps", "Boots of Swiftnes",
             "Ionian Boots of Lucidity", "Sorcerer's Shoes", "Mercury's Treads"]
# -----------------------
# - Summoner Spell List -
# -----------------------
arrSum = os.listdir("resources/Summoner")
arrSum.sort()
# --------------------
# - Mythic Item List -
# --------------------
Mythics = []
with open('resources/RuleSets/Mythics.txt') as f:
    lines = f.readlines()
    for n in lines:
        if n == "\n":
            lines.remove("\n")
    Mythics += lines
# --------------------
# - Normal Item List -
# --------------------
normalItems = []
with open('resources/RuleSets/Legendarys.txt') as f:
    lines = f.readlines()
    normalItems += lines
# makes the directory for image icon files so it can be called later without randomchampion[]
# since some files are odd named compaired to champion names ex: velkoz : vel'koz
arr = os.listdir("resources/Icons")
ChampionFiles = []
ChampionFiles += arr
ChampionFiles.sort()
# same as above but for rune IIcons
arr2 = os.listdir("resources/Runes/Icons")
RuneFiles = []
RuneFiles += arr2
RuneFiles.sort()
# SupportItems = ["Black Mist Scythe", "Shard of True Ice", "Pauldrons of Whiterock", "Bulwark of the Mountain"]
# --Champion RND--
min = 0
max = len(ChampionName) - 1 # length of the list champion which is ever expanding
ChampionNumber = int(random() * (max - min + 1) + min)
# --Boots RND--
BootsMin = 0
BootsMax = len(NormBoots)
SelectBoots = int(random() * (BootsMax - BootsMin + 1) + BootsMin)
# --Mythic RND--
MythicMin = 0
MythicMax = len(Mythics)
SelectMythic = int(random() * (MythicMax - MythicMin + 1) + MythicMin)
# --Items RND--
ItemsMin = 0
ItemsMax = len(normalItems) - 1
SelectItems = int(random() * (ItemsMax - ItemsMin + 1) + ItemsMin)

@Bot.slash_command(aliases=['RR', 'randomroll'], help='randomly rolls a generated build for League of Legends\nValid Inputs: [rr] [RR] [randomroll]')
async def rr(ctx: discord.Interaction):
    RunesRND = int(random() * (5 - 0 + 0) + 0) # Picks primary
    PRPD = int(random() * (4 - 0 + 0) + 0)  # for precision / domination
    PRR = int(random() * (3 - 0 + 0) + 0)  # for the rest
    Slot1 = int(random() * (3 - 0 + 0) + 0)  # Slot one runes
    Slot2 = int(random() * (3 - 0 + 0) + 0)  # Slot two runes
    Slot3D = int(random() * (4 - 0 + 0) + 0)  # Slot three Domination
    Slot3R = int(random() * (3 - 0 + 0) + 0)  # Slot three rest
    for case in switch(RunesRND):
        if case(0):  # Domination Primary
            PrimaryTitle = "Domination"
            for case in switch(PRPD):
                if case(0):  # Electrocute
                    Primary = "<:Electrocute_rune:841365343486476349> Electrocute"
                    break
                if case(1):  # Predator
                    Primary = "<:Predator_rune:841365430135554078> Predator"
                    break
                if case(2):  # Dark Harvest
                    Primary = "<:Dark_Harvest_rune:841365336615944283> Dark Harvest"
                    break
                if case(3):  # Hail of Blades
                    Primary = "<:Hail_of_Blades_rune:841365373278355477> Hail of Blades"
                    break
            # Slot One
            for case in switch(Slot1):
                if case(0): # Cheap Shot
                    SubOne = "<:Cheap_Shot_rune:841365328285138974> Cheap Shot"
                    break
                if case(1): # Taste of Blood
                    SubOne = "<:Taste_of_Blood_rune:841365462201663558> Taste of Blood"
                    break
                if case(2): # Sudden Impact
                    SubOne = "<:Sudden_Impact_rune:841365393602904185> Sudden Impact"
                    break
            # Slot Two
            for case in switch(Slot2):
                if case(0): # Zombie Ward
                    SubTwo = "<:Zombie_Ward_rune:841365440135168031> Zombie Ward"
                    break
                if case(1): # Ghost Poro
                    SubTwo = "<:Ghost_Poro_rune:841365380190306346> Ghost Poro"
                    break
                if case(2): # Eyeball Collection
                    SubTwo = "<:Eyeball_Collection_rune:841365350524125204> Eyeball Collection"
                    break
            # Slot Three
            for case in switch(Slot3D):
                if case(0): # Treasure Hunter
                    SubThree = "<:Treasure_Hunter_rune:970518723251290172> Treasure Hunter"
                    break
                if case(1): # Ingenious Hunter
                    SubThree = "<:Ingenious_Hunter_rune:841365361114218536> Ingenious Hunter"
                    break
                if case(2): # Relentless Hunter
                    SubThree = "<:Relentless_Hunter_rune:841365406929256488> Relentless Hunter"
                    break
                if case(3): # Ultimate Hunter
                    SubThree = "<:Ultimate_Hunter_rune:841365451477221396> Ultimate Hunter"
                    break
            break
        if case(1):  # Precision Primary
            PrimaryTitle = "Precision"
            for case in switch(PRPD):
                if case(0): # Press the Attack
                    Primary = "<:Press_the_Attack_rune:841365840367714364> Press the Attack"
                    break
                if case(1): # Lethal Tempo
                    Primary = "<:Lethal_Tempo_rune:841365861184045067>  Lethal Tempo"
                    break
                if case(2): # Fleet Footwork
                    Primary = "<:Fleet_Footwork_rune:841365803122294804> Fleet Footwork"
                    break
                if case(3): # Conqueror
                    Primary = "<:Conqueror_rune:841365777793548349> Conqueror"
                    break
            # Slot One
            for case in switch(Slot1):
                if case(0): # Overheal
                    SubOne = "<:Overheal_rune:841365854515625994> Overheal"
                    break
                if case(1): # Triumph
                    SubOne = "<:Triumph_rune:841365868096913418> Triumph"
                    break
                if case(2): # Presence of Mind
                    SubOne = "<:Presence_of_Mind_rune:841365847935287307> Presence of Mind"
                    break
            # Slot Two
            for case in switch(Slot2):
                if case(0): # Legend: Alacrity
                    SubTwo = "<:Legend_Alacrity_rune:841365818079051847> Legend: Alacrity"
                    break
                if case(1): # Legend: Tenacity
                    SubTwo = "<:Legend_Tenacity_rune:841365834206674994> Legend: Tenacity"
                    break
                if case(2): # Legend: Bloodline
                    SubTwo = "<:Legend_Bloodline_rune:841365824866746388> Legend: Bloodline"
                    break
            # Slot Three
            for case in switch(Slot3R):
                if case(0): # Coup de Grace
                    SubThree = "<:Coup_de_Grace_rune:841365786362249226> Coup de Grace"
                    break
                if case(1): # Cut Down
                    SubThree = "<:Cut_Down_rune:841365797682413608> Cut Down"
                    break
                if case(2): # Last Stand
                    SubThree = "<:Last_Stand_rune:841365809930829884> Last Stand"
                    break
            break
        if case(2):  # Resolve
            PrimaryTitle = "Resolve"
            for case in switch(PRR):
                if case(0): # Grasp of the Undying
                    Primary = "<:Grasp_of_the_Undying_rune:841365593424920579> Grasp of the Undying"
                    break
                if case(1): # Aftershock
                    Primary = "<:Aftershock_rune:841365499107475556> Aftershock"
                    break
                if case(2): # Guardian
                    Primary = "<:Guardian_rune:841365600802177031> Guardian"
                    break
            # Slot One
            for case in switch(Slot1):
                if case(0): # Demolish
                    SubOne = "<:Demolish_rune:841365576914960386> Demolish"
                    break
                if case(1): # Font of Life
                    SubOne = "<:Font_of_Life_rune:841365586134564886> Font of Life"
                    break
                if case(2): # Shield Bash
                    SubOne = "<:Shield_Bash_rune:841365629234839604> Shield Bash"
                    break
            # Slot Two
            for case in switch(Slot2):
                if case(0): # Conditioning
                    SubTwo = "<:Conditioning_rune:841365569831305236> Conditioning"
                    break
                if case(1): # Second Wind
                    SubTwo = "<:Second_Wind_rune:841365621782609950> Second Wind"
                    break
                if case(2): # Bone Plating
                    SubTwo = "<:Bone_Plating_rune:841365508950982676> Bone Plating"
                    break
            # Slot Three
            for case in switch(Slot3R):
                if case(0): # Overgrowth
                    SubThree = "<:Overgrowth_rune:841365607307149343> Overgrown"
                    break
                if case(1): # Revitalize
                    SubThree = "<:Revitalize_rune:841365614697381919> Revitalize"
                    break
                if case(2): # Unflinching
                    SubThree = "<:Unflinching_rune:841365636055040096> Unflinching"
                    break
            break
        if case(3):  # Sorcery
            PrimaryTitle = "Sorcery"
            for case in switch(PRR):
                if case(0): # Summon Aery
                    Primary = "<:Summon_Aery_rune:841366127161376829> Summon Aery"
                    break
                if case(1): # Arcane Comet
                    Primary = "<:Arcane_Comet_rune:841366061253394442> Arcane Comet"
                    break
                if case(2): # Phase Rush
                    Primary = "<:Phase_Rush_rune:841366084804411412> Phase Rush"
                    break
            # Slot One
            for case in switch(Slot1):
                if case(0): # Nullifying Orb
                    SubOne = "<:Nullifying_Orb_rune:841366090177183765> Nullifying Orb"
                    break
                if case(1): # ManaFlow Band
                    SubOne = "<:Manaflow_Band_rune:841366106475069519> ManaFlow Band"
                    break
                if case(2): # Nimbus Cloak
                    SubOne = "<:Nimbus_Cloak_rune:841366098247155719> Nimbus Cloak"
                    break
            # Slot Two
            for case in switch(Slot2):
                if case(0): # Transcendence
                    SubTwo = "<:Transcendence_rune:841366120065531905> Transcendence"
                    break
                if case(1): # Celerity
                    SubTwo = "<:Celerity_rune:841366070917070919> Celerity"
                    break
                if case(2): # Absolute Focus
                    SubTwo = "<:Absolute_Focus_rune:841366053346344961> Absolute Focus"
                    break
            # Slot Three
            for case in switch(Slot3R):
                if case(0): # Scorch
                    SubThree = "<:Scorch_rune:841366133889957960> Scorch"
                    break
                if case(1): # Waterwalking
                    SubThree = "<:Waterwalking_rune:841366114520793098> Waterwalking"
                    break
                if case(2): # Gathering Storm
                    SubThree = "<:Gathering_Storm_rune:841366078067310652> Gathering Storm"
                    break
            break
        if case(4):  # Inspiration
            PrimaryTitle = "Inspiration"
            for case in switch(PRR):
                if case(0): # Glacial Augment
                    Primary = "<:Glacial_Augment_rune:841365992189460522> Glacial Augment"
                    break
                if case(1): # Unsealed Spellbook
                    Primary = "<:Unsealed_Spellbook_rune:841365960404762675> Unsealed Spellbook"
                    break
                if case(2): # First Strike
                    Primary = "<:First_Strike_rune:911828146637144104> First Strike"
                    break
            # Slot One
            for case in switch(Slot1):
                if case(0): # Hextech Flashtraption
                    SubOne = "<:Hextech_Flashtraption_rune:841365980227829810> Hextech Flashtraption"
                    break
                if case(1): # Magical Footwear
                    SubOne = "<:Magical_Footwear_rune:841365973604237383> Magical Footwear"
                    break
                if case(2): # Perfect Timing
                    SubOne = "<:Perfect_Timing_rune:841365999877226547> Perfect Timing"
                    break
            # Slot Two
            for case in switch(Slot2):
                if case(0): # Future's Market
                    SubTwo = "<:Futures_Market_rune:841365949705617449> Future's Market"
                    break
                if case(1): # Celerity
                    SubTwo = "<:Minion_Dematerializer_rune:841365955203432478> Minion Dematerializer"
                    break
                if case(2): # Absolute Focus
                    SubTwo = "<:Biscuit_Delivery_rune:841365935830466561> Biscuit Delivery"
                    break
            for case in switch(Slot3R):
                if case(0): # Cosmic Insight
                    SubThree = "<:Cosmic_Insight_rune:841365941900410880> Cosmic Insight"
                    break
                if case(1): # Approach Velocity
                    SubThree = "<:Approach_Velocity_rune:841365929047883827> Approach Velocity"
                    break
                if case(2): # Time Warp Tonic
                    SubThree = "<:Time_Warp_Tonic_rune:841365965559300097> Time Warp Tonic"
                    break
            break
# ----------------------------------------------------------------------------------------------------------
    RunesSecondaryRND = int(random() * (5 - 0 + 0) + 0) # Picks Secondary
    while RunesRND == RunesSecondaryRND:
        RunesSecondaryRND = int(random() * (5 - 0 + 0) + 0)  # Picks Secondary
    sSubOneOne = int(random() * (2 + 1) + 0)
    sSubTwoOne = int(random() * (2 + 1) + 0)
    sPrimaryTreeOne = int(random() * (3 + 1) + 0)
    sSubThreeThree = int(random() * (2 + 1) + 0)
    sSubOne = ""
    sSubTwo = ""
    sSubThree = ""
    for case in switch(RunesSecondaryRND):
        if case(0): # Domination Secondary
            SecondaryTitle = "Domination"
            # SubOne
            for case in switch(sSubOneOne):
                if case(0): # Cheap Shot
                    sSubOne = "<:Cheap_Shot_rune:841365328285138974> Cheap Shot"
                    break
                if case(1): # Taste of Blood
                    sSubOne = "<:Taste_of_Blood_rune:841365462201663558> Taste of Blood"
                    break
                if case(2): # Sudden Impact
                    sSubOne = "<:Sudden_Impact_rune:841365393602904185> Sudden Impact"
                    break
            # SubTwo
            for case in switch(sSubTwoOne):
                if case(0): # Zombie Ward
                    sSubTwo = "<:Zombie_Ward_rune:841365440135168031> Zombie Ward"
                    break
                if case(1): # Ghost Poro
                    sSubTwo = "<:Ghost_Poro_rune:841365380190306346> Ghost Poro"
                    break
                if case(2): # Eyeball Collection
                    sSubTwo = "<:Eyeball_Collection_rune:841365350524125204> Eyeball Collection"
                    break
            # SubThree
            for case in switch(sPrimaryTreeOne):
                if case(0): # Treasure Hunter
                    sSubThree = "<:Treasure_Hunter_rune:970518723251290172> Treasure Hunter"
                    break
                if case(1): # Ingenious Hunter
                    sSubThree = "<:Ingenious_Hunter_rune:841365361114218536> Ingenious Hunter"
                    break
                if case(2): # Relentless Hunter
                    sSubThree = "<:Relentless_Hunter_rune:841365406929256488> Relentless Hunter"
                    break
                if case(3): #Ultimate Hunter
                    sSubThree = "<:Ultimate_Hunter_rune:841365451477221396> Ultimate Hunter"
                    break
            break
        if case(1): # Precision
            SecondaryTitle = "Precision"
            # SubOne
            for case in switch(sSubOneOne):
                if case(0): # Overheal
                    sSubOne = "<:Overheal_rune:841365854515625994> Overheal"
                    break
                if case(1): # Triumph
                    sSubOne = "<:Triumph_rune:841365868096913418> Triumph"
                    break
                if case(2): # Presence of Mind
                    sSubOne = "<:Presence_of_Mind_rune:841365847935287307> Presence of Mind"
                    break
            # SubTwo
            for case in switch(sSubTwoOne):
                if case(0): # Legend: Alacrity
                    sSubTwo = "<:Legend_Alacrity_rune:841365818079051847> Legend: Alacrity"
                    break
                if case(1): # Legend: Tenacity
                    sSubTwo = "<:Legend_Tenacity_rune:841365834206674994> Legend: Tenacity"
                    break
                if case(2): # Legend: Bloodline
                    sSubTwo = "<:Legend_Bloodline_rune:841365824866746388> Legend: Bloodline"
                    break
            # SubThree
            for case in switch(sSubThreeThree):
                if case(0): # Coup de Grace
                    sSubThree = "<:Coup_de_Grace_rune:841365786362249226> Coup de Grace"
                    break
                if case(1): # Cut Down
                    sSubThree = "<:Cut_Down_rune:841365797682413608> Cut Down"
                    break
                if case(2): # Last Stand
                    sSubThree = "<:Last_Stand_rune:841365809930829884> Last Stand"
                    break
            break
        if case(2):  # Resolve
            SecondaryTitle = "Resolve"
            # SubOne
            for case in switch(sSubOneOne):
                if case(0): # Demolish
                    sSubOne = "<:Demolish_rune:841365576914960386> Demolish"
                    break
                if case(1): # Font of Life
                    sSubOne = "<:Font_of_Life_rune:841365586134564886> Font of Life"
                    break
                if case(2): # Shield Base
                    sSubOne = "<:Shield_Bash_rune:841365629234839604> Shield Bash"
                    break
            # SubTwo
            for case in switch(sSubTwoOne):
                if case(0): # Conditioning
                    sSubTwo = "<:Conditioning_rune:841365569831305236> Conditioning"
                    break
                if case(1): # Second Wind
                    sSubTwo = "<:Second_Wind_rune:841365621782609950> Second Wind"
                    break
                if case(2): # Bone Plating
                    sSubTwo = "<:Bone_Plating_rune:841365508950982676> Bone Plating"
                    break
            # SubThree
            for case in switch(sSubThreeThree):
                if case(0): # Overgrowth
                    sSubThree = "<:Overgrowth_rune:841365607307149343> Overgrown"
                    break
                if case(1): # Revitalize
                    sSubThree = "<:Revitalize_rune:841365614697381919> Revitalize"
                    break
                if case(2): # Unflinching
                    sSubThree = "<:Unflinching_rune:841365636055040096> Unflinching"
                    break
            break
        if case(3): # Sorcery
            SecondaryTitle = "Sorcery"
            # SubOne
            for case in switch(sSubOneOne):
                if case(0): # Nullifying Orb
                    sSubOne = "<:Nullifying_Orb_rune:841366090177183765> Nullifying Orb"
                    break
                if case(1): # ManaFlow Band
                    sSubOne = "<:Manaflow_Band_rune:841366106475069519> ManaFlow Band"
                    break
                if case(2): # Nimbus Cloak
                    sSubOne = "<:Nimbus_Cloak_rune:841366098247155719> Nimbus Cloak"
                    break
            # SubTwo
            for case in switch(sSubTwoOne):
                if case(0): # Transcendence
                    sSubTwo = "<:Transcendence_rune:841366120065531905> Transcendence"
                    break
                if case(1): # Celerity
                    sSubTwo = "<:Celerity_rune:841366070917070919> Celerity"
                    break
                if case(2): # Absolute Focus
                    sSubTwo = "<:Absolute_Focus_rune:841366053346344961> Absolute Focus"
                    break
            # SubThree
            for case in switch(sSubThreeThree):
                if case(0): # Scorch
                    sSubThree = "<:Scorch_rune:841366133889957960> Scorch"
                    break
                if case(1): # Waterwalking
                    sSubThree = "<:Waterwalking_rune:841366114520793098> Waterwalking"
                    break
                if case(2): # Gathering Storm
                    sSubThree = "<:Gathering_Storm_rune:841366078067310652> Gathering Storm"
                    break
            break
        if case(4): # Inspiration
            SecondaryTitle = "Inspiration"
            # SubOne
            for case in switch(sSubOneOne):
                if case(0): # Hextech Flashtraption
                    sSubOne = "<:Hextech_Flashtraption_rune:841365980227829810> Hextech Flashtraption"
                    break
                if case(1): # Magical Footwear
                    sSubOne = "<:Magical_Footwear_rune:841365973604237383> Magical Footwear"
                    break
                if case(2): # Perfect Timing
                    sSubOne = "<:Perfect_Timing_rune:841365999877226547> Perfect Timing"
                    break
            # SubTwo
            for case in switch(sSubTwoOne):
                if case(0): # Future's Market
                    sSubTwo = "<:Futures_Market_rune:841365949705617449> Future's Market"
                    break
                if case(1): # Celerity
                    sSubTwo = "<:Minion_Dematerializer_rune:841365955203432478> Minion Dematerializer"
                    break
                if case(2): # Biscuit Delivery
                    sSubTwo = "<:Biscuit_Delivery_rune:841365935830466561> Biscuit Delivery"
                    break
            # SubThree
            for case in switch(sSubThreeThree):
                if case(0): # Cosmic Insight
                    sSubThree = "<:Cosmic_Insight_rune:841365941900410880> Cosmic Insight"
                    break
                if case(1): # Approach Velocity
                    sSubThree = "<:Approach_Velocity_rune:841365929047883827> Approach Velocity"
                    break
                if case(2): # Time Warp Tonic
                    sSubThree = "<:Time_Warp_Tonic_rune:841365965559300097> Time Warp Tonic"
                    break
            break
# ----------------------------------------------------------------------------------------------------------
    FinalRandom = int(random() * (2 + 1) + 0)
    DisplayOne = ""
    DisplayTwo = ""
    for case in switch(FinalRandom):
        if case(0):
            DisplayOne = sSubOne
            DisplayTwo = sSubTwo
            break
        if case(1):
            DisplayOne = sSubOne
            DisplayTwo = sSubThree
            break
        if case(2):
            DisplayOne = sSubTwo
            DisplayTwo = sSubThree
            break
# ----------------------------------------------------------------------------------------------------------
    ShardOne = int(random() * (2 + 1) + 0)
    ShardTwo = int(random() * (2 + 1) + 0)
    ShardThree = int(random() * (2 + 1) + 0)
    for case in switch(ShardOne):
        if case(0): # Adaptive
            ShardOneSlot = "<:Rune_shard_Adaptive_Force:841426918824869938>"
            break
        if case(1): # Attack Speed
            ShardOneSlot = "<:Rune_shard_Attack_Speed:841426940312813628>"
            break
        if case(2): # Ability Haste
            ShardOneSlot = "<:Rune_shard_Cooldown_Reduction:841426944171180123>"
            break
    for case in switch(ShardTwo):
        if case(0): # Adaptive
            ShardTwoSlot = "<:Rune_shard_Adaptive_Force:841426918824869938>"
            break
        if case(1): # Armor
            ShardTwoSlot = "<:Rune_shard_Armor:841426928338468914>"
            break
        if case(2): # Magic Resist
            ShardTwoSlot = "<:Rune_shard_Magic_Resistance:841426959039856681>"
            break
    for case in switch(ShardThree):
        if case(0): # Adaptive
            ShardThreeSlot = "<:Rune_shard_Health:841426952388476979>"
            break
        if case(1): # Armor
            ShardThreeSlot = "<:Rune_shard_Armor:841426928338468914>"
            break
        if case(2): # Magic Resist
            ShardThreeSlot = "<:Rune_shard_Magic_Resistance:841426959039856681>"
            break
# ----------------------------------------------------------------------------------------------------------
    dog = []
    items = []
    # calls for random items - set stops any duplicates
    while len(items) < 5:
        SelectItems = int(random() * (ItemsMax - ItemsMin + 1) + ItemsMin) - 1
        dog.append(normalItems[SelectItems])
        for i in dog:
            if i not in items:
                items.append(i)
        if SelectItems == 42:
            if 'Titanic Hydra\n' in items:
                items.remove('Titanic Hydra\n')
        if SelectItems == 56:
            if 'Ravenous Hydra\n' in items:
                items.remove('Ravenous Hydra\n')
    # calls rnd for each run
    SelectBoots = int(random() * (BootsMax - BootsMin + 1) + BootsMin) - 1
    SelectMythic = int(random() * (MythicMax - MythicMin + 1) + MythicMin) - 1
    ChampionNumber = int(random() * (max - min + 1) + min) - 1
    SelectMythic = int(random() * (MythicMax - MythicMin + 1) + MythicMin) - 1
# ----------------------------------------------------------------------------------------------------------
    sum1 = int(random() * len(arrSum))
    sum2 = int(random() * len(arrSum))
    abilitys = ["Q", "W", "E"]
    shuffle(abilitys)
    while sum1 == sum2:
        sum2 = int(random() * len(arrSum))
    sumoji = ["<:Barrier:917958756241899560>", "<:Cleanse:917958769575616542>", "<:Exhaust:917958778165534761>",
              "<:Flash:917958788722622524>", "<:Ghost:917958798893776967>", "<:Heal:917958808385495062>",
              "<:Ignite:917958817575223297>", "<:Smite:917958826299387964>", "<:Teleport:917958834545377420>"]
    # ------------------------------------ Champion Embed ------------------------------------
    Champion = EmbedBuilder(
        color=discord.Color.gold(),
        title=ChampionName[ChampionNumber],
        description=ChampionQuip[ChampionNumber],
        thumbnail=f"attachment://{ChampionFiles[ChampionNumber]}",
        footer=[f'Requested by {ctx.author.name}']
    ).build()
    image = discord.File(f"resources/Icons/{ChampionFiles[ChampionNumber]}")
    # ------------------------------------ Item Embed ------------------------------------
    if ChampionNumber == 18:
        Items = EmbedBuilder(
            color=discord.Color.gold(),
            title="- - - - - - - - - ITEMS - - - - - - - - -",
            description=
            f"**Mythic:**\n{Mythics[SelectMythic]}\n"
            f"\n**Items:**\n{items[0]}{items[1]}{items[2]}{items[3]}{items[4]}"
            f"\n**- - - - - - - - - - - - - - - - - - - - - - - - - - -**",
            footer=[f'Requested by {ctx.author.name}']
        ).build()
    else:
        Items = EmbedBuilder(
            color=discord.Color.gold(),
            title="- - - - - - - - - ITEMS - - - - - - - - -",
            description=
            f"**Mythic:**\n{Mythics[SelectMythic]}\n"
            f"**Boots:**\n{NormBoots[SelectBoots]}\n"
            f"\n**Items:**\n{items[0]}{items[1]}{items[2]}{items[3]}"
            f"\n**- - - - - - - - - - - - - - - - - - - - - - - - - - -**",
            footer=[f'Requested by {ctx.author.name}']
        ).build()
    # ------------------------------------ Primary rune Embed ------------------------------------
    PrimaryRunes = EmbedBuilder(
        color=discord.Color.gold(),
        title=f"Primary: {PrimaryTitle}",
        description=f"{Primary}\n{SubOne}\n{SubTwo}\n{SubThree}",
        thumbnail=f"attachment://{RuneFiles[RunesRND]}",
        footer=[f'Requested by {ctx.author.name}']
    ).build()
    image2 = discord.File(f"resources/Runes/Icons/{RuneFiles[RunesRND]}")
    # ------------------------------------ Secondary rune Embed ------------------------------------
    SecondaryRunes = EmbedBuilder(
        color=discord.Color.gold(),
        title=f"Secondary: {SecondaryTitle}",
        description=f"{DisplayOne}\n{DisplayTwo}",
        fields=[["Shards:", f"\n{ShardOneSlot}{ShardTwoSlot}{ShardThreeSlot}", True]],
        thumbnail=f"attachment://{RuneFiles[RunesSecondaryRND]}",
        footer=[f'Requested by {ctx.author.name}']
    ).build()
    image3 = discord.File(f"resources/Runes/Icons/{RuneFiles[RunesSecondaryRND]}")
    # ------------------------------------ Summoner Spells ------------------------------------
    SummonerSpells = EmbedBuilder(
        color=discord.Color.gold(),
        title=f"Level max order: {abilitys[0]} -> {abilitys[1]} -> {abilitys[2]}",
        description=f"\nSummoner Spells:\n",
        fields=[["Sum 1:", f"{sumoji[sum1]} {arrSum[sum1][: - 4]}", True], ["Sum 2:", f"{sumoji[sum2]} {arrSum[sum2][: - 4]}", True]],
        footer=[f'Requested by {ctx.author.name}']
    ).build()
    # ------------------------------------ Message to be sent ------------------------------------
    await ctx.send(
        embed=Champion,
        file=image
    )
    await ctx.send(
        embed=Items
    )
    await ctx.send(
        embed=PrimaryRunes,
        file=image2
    )
    await ctx.send(
        embed=SecondaryRunes,
        file=image3
    )
    await ctx.send(
        embed=SummonerSpells
    )
    await ctx.respond("Done!")

@Bot.slash_command(aliases=['RC', 'randomchampion', 'RandomChampion'], help='Gives a random champion!')
async def rc(ctx):
    min = 0
    max = len(ChampionName) - 1  # length of the list champion which is ever expanding
    ChampionNumber = int(random() * (max - min + 1) + min)

    Champion = EmbedBuilder(
        color=discord.Color.gold(),
        title=f'{ChampionName[ChampionNumber]}',
        description=ChampionQuip[ChampionNumber],
        thumbnail=f"attachment://{ChampionFiles[ChampionNumber]}",
        footer=[f'Requested by {ctx.author.name}']
    ).build()
    image = discord.File(f"resources/Icons/{ChampionFiles[ChampionNumber]}")
    await ctx.send(
        embed=Champion,
        file=image
    )
    await ctx.respond("Done!")
@Bot.slash_command(name="invite",discription="sends server invite" ,help='Provide invite link and official support server invite link')
async def invite(ctx):
    embed = EmbedBuilder(
        color=discord.Color.gold(),
        title=f'Invite Link',
        description=f'[Click here to invite me to your server!](https://discord.com/api/oauth2/authorize?client_id=628685778318524426&permissions=8&scope=bot)\n'
                    f'[Click here for the official support server!](https://discord.gg/jFY3pPtm2u)',
        footer=[f'Requested by {ctx.author.name}']
    ).build()
    await ctx.send(embed=embed)
    await ctx.respond("Done!")
@Bot.slash_command(name="count",discription="sends server count",help='[Current] server count')
async def count(ctx):
    county = 0
    members = []
    # go through all guilds and add each member to a list, remove any duplicates then set the list length to an int called county

    for guild in Bot.guilds:
        for member in guild.members:
            members.append(member)

    members = list(dict.fromkeys(members))
    county = len(members)


    member_count = EmbedBuilder(
        color=discord.Color.from_rgb(250, 144, 255),
        title=f'Connected to **{len(Bot.guilds)}** servers!',
        description=f'**{county}** total members!'
                    f'\nGiving an average of **{county / len(Bot.guilds)}** per server'
                    f'\n(This server has **{ctx.guild.member_count}** members)',
        footer=[f'Requested by {ctx.author.name}']).build()

    await ctx.send(embed=member_count)
    await ctx.respond("Done!")
@Bot.slash_command(name="ping", discription="sends ping", help='Sends servers latency at a given time')
async def ping(ctx):
    await ctx.send(f'Pong! {round(Bot.latency * 1000)}ms')
    await ctx.respond("Done!")

@Bot.slash_command(name="support", discription="sends how you can support me!",help='Help support me! Anything counts :D')
async def support(ctx):
    footer = f'Requested by {ctx.author.name}'
    Thank = EmbedBuilder(
        color=discord.Color.from_rgb(250, 144, 255),
        title=f"Thank You!",
        description=f"I am currently studying Computer Science in college\n"
                    f"and its quite expensive so if it isnt too much\n"
                    f"to ask i would appreciate any amount of donations.\n"
                    f"Patreon: https://www.patreon.com/PxINKY\n"
                    f"\nThanks again for using my bot and\n"
                    f"i hope you enjoy all that it offers!\n -Pinky<3"
                    f"\n\n**If you have any questions or concerns, please contact me! [PxINKY#0001]**",
        footer=[footer]
    ).build()
    # ------------------------------------ Message to be sent ------------------------------------
    await ctx.send(
        embed=Thank
    )
    await ctx.respond("Done!")


@Bot.slash_command(name="summoner", discription="summoner look up",help='Enter a valid summoner name and region to get the summoner\'s profile',aliases=['cass', 's'])
async def summoner(ctx, summoner_name, region):
    summoner = cass.get_summoner(name=summoner_name, region=(region.upper()))
    # send info in embed
    if summoner.exists:
        pfpurl = summoner.profile_icon.url
        embed = EmbedBuilder(
            title=f"{summoner.name}",
            description=f"Level: {summoner.level}",
            thumbnail=f"{pfpurl}",
            color=discord.Color.gold(),
            footer=[f"requested by {ctx.author.name}"]).build()
        await ctx.send(embed=embed)
    else:
        await ctx.send("Sorry that summoner doesn't exist!")
    await ctx.respond("Done!")


Bot.run(TOKEN)
