from apworld.toontown import locations

from toontown.hood import ZoneUtil
from toontown.toonbase import ToontownGlobals


# Given cog code (bf, nc, etc) return the AP location counterpart
# if not a valid cog, just returns an empty string
def cog_code_to_ap_location(cog_code: str) -> str:

    return {
        'cc': (locations.COLD_CALLER_DEFEATED_LOCATION, locations.COLD_CALLER_MAXED_LOCATION),
        'tm': (locations.TELEMARKETER_DEFEATED_LOCATION, locations.TELEMARKETER_MAXED_LOCATION),
        'nd': (locations.NAME_DROPPER_DEFEATED_LOCATION, locations.NAME_DROPPER_MAXED_LOCATION),
        'gh': (locations.GLAD_HANDER_DEFEATED_LOCATION, locations.GLAD_HANDER_MAXED_LOCATION),
        'ms': (locations.MOVER_AND_SHAKER_DEFEATED_LOCATION, locations.MOVER_AND_SHAKER_MAXED_LOCATION),
        'tf': (locations.TWO_FACE_DEFEATED_LOCATION, locations.TWO_FACE_MAXED_LOCATION),
        'm': (locations.MINGLER_DEFEATED_LOCATION, locations.MINGLER_MAXED_LOCATION),
        'mh': (locations.MR_HOLLYWOOD_DEFEATED_LOCATION, locations.MR_HOLLYWOOD_MAXED_LOCATION),

        'sc': (locations.SHORT_CHANGE_DEFEATED_LOCATION, locations.SHORT_CHANGE_MAXED_LOCATION),
        'pp': (locations.PENNY_PINCHER_DEFEATED_LOCATION, locations.PENNY_PINCHER_MAXED_LOCATION),
        'tw': (locations.TIGHTWAD_DEFEATED_LOCATION, locations.TIGHTWAD_MAXED_LOCATION),
        'bc': (locations.BEAN_COUNTER_DEFEATED_LOCATION, locations.BEAN_COUNTER_MAXED_LOCATION),
        'nc': (locations.NUMBER_CRUNCHER_DEFEATED_LOCATION, locations.NUMBER_CRUNCHER_MAXED_LOCATION),
        'mb': (locations.MONEY_BAGS_DEFEATED_LOCATION, locations.MONEY_BAGS_MAXED_LOCATION),
        'ls': (locations.LOAN_SHARK_DEFEATED_LOCATION, locations.LOAN_SHARK_MAXED_LOCATION),
        'rb': (locations.ROBBER_BARRON_DEFEATED_LOCATION, locations.ROBBER_BARRON_MAXED_LOCATION),

        'bf': (locations.BOTTOM_FEEDER_DEFEATED_LOCATION, locations.BOTTOM_FEEDER_MAXED_LOCATION),
        'b': (locations.BLOODSUCKER_DEFEATED_LOCATION, locations.BLOODSUCKER_MAXED_LOCATION),
        'dt': (locations.DOUBLE_TALKER_DEFEATED_LOCATION, locations.DOUBLE_TALKER_MAXED_LOCATION),
        'ac': (locations.AMBULANCE_CHASER_DEFEATED_LOCATION, locations.AMBULANCE_CHASER_MAXED_LOCATION),
        'bs': (locations.BACKSTABBER_DEFEATED_LOCATION, locations.BACKSTABBER_MAXED_LOCATION),
        'sd': (locations.SPIN_DOCTOR_DEFEATED_LOCATION, locations.SPIN_DOCTOR_MAXED_LOCATION),
        'le': (locations.LEGAL_EAGLE_DEFEATED_LOCATION, locations.LEGAL_EAGLE_MAXED_LOCATION),
        'bw': (locations.BIG_WIG_DEFEATED_LOCATION, locations.BIG_WIG_MAXED_LOCATION),

        'f': (locations.FLUNKY_DEFEATED_LOCATION, locations.FLUNKY_MAXED_LOCATION),
        'p': (locations.PENCIL_PUSHER_DEFEATED_LOCATION, locations.PENCIL_PUSHER_MAXED_LOCATION),
        'ym': (locations.YESMAN_DEFEATED_LOCATION, locations.YESMAN_MAXED_LOCATION),
        'mm': (locations.MICROMANAGER_DEFEATED_LOCATION, locations.MICROMANAGER_MAXED_LOCATION),
        'ds': (locations.DOWNSIZER_DEFEATED_LOCATION, locations.DOWNSIZER_MAXED_LOCATION),
        'hh': (locations.HEAD_HUNTER_DEFEATED_LOCATION, locations.HEAD_HUNTER_MAXED_LOCATION),
        'cr': (locations.CORPORATE_RAIDER_DEFEATED_LOCATION, locations.CORPORATE_RAIDER_MAXED_LOCATION),
        'tbc': (locations.BIG_CHEESE_DEFEATED_LOCATION, locations.BIG_CHEESE_MAXED_LOCATION)

    }.get(cog_code, '')


# Given the string representation of a location, retrieve the numeric ID
def ap_location_name_to_id(location_name: str) -> int:
    return locations.LOCATION_DEFINITIONS[location_name].unique_id


# Given a Zone ID, give the ID of an AP location award the player.
# returns -1 if this isn't a zone we have to worry about
def get_zone_discovery_id(zoneId: int) -> int:

    pgZone = ZoneUtil.getHoodId(zoneId)

    ZONE_TO_LOCATION = {
        ToontownGlobals.ToontownCentral: locations.DISCOVER_TTC,
        ToontownGlobals.DonaldsDock: locations.DISCOVER_DD,
        ToontownGlobals.DaisyGardens: locations.DISCOVER_DG,
        ToontownGlobals.MinniesMelodyland: locations.DISCOVER_MM,
        ToontownGlobals.TheBrrrgh: locations.DISCOVER_TB,
        ToontownGlobals.DonaldsDreamland: locations.DISCOVER_DDL,

        ToontownGlobals.GoofySpeedway: locations.DISCOVER_GS,
        ToontownGlobals.OutdoorZone: locations.DISCOVER_AA,

        ToontownGlobals.SellbotHQ: locations.DISCOVER_SBHQ,
        ToontownGlobals.CashbotHQ: locations.DISCOVER_CBHQ,
        ToontownGlobals.LawbotHQ: locations.DISCOVER_LBHQ,
        ToontownGlobals.BossbotHQ: locations.DISCOVER_BBHQ,
    }

    # Valid zone?
    loc = ZONE_TO_LOCATION.get(pgZone)
    if not loc:
        return -1

    # We have a location, convert it to its ID
    return ap_location_name_to_id(loc)


# Gets the AP location ID from a ToontownGlobals facility ID definition
def get_facility_id(facility_id: int) -> int:

    FACILITY_LOCATION_CHECKS = {
        ToontownGlobals.SellbotFactoryInt: locations.CLEAR_FRONT_FACTORY,
        ToontownGlobals.SellbotFactoryIntS: locations.CLEAR_SIDE_FACTORY,

        ToontownGlobals.CashbotMintIntA: locations.CLEAR_COIN_MINT,
        ToontownGlobals.CashbotMintIntB: locations.CLEAR_DOLLAR_MINT,
        ToontownGlobals.CashbotMintIntC: locations.CLEAR_BULLION_MINT,

        ToontownGlobals.LawbotStageIntA: locations.CLEAR_A_OFFICE,
        ToontownGlobals.LawbotStageIntB: locations.CLEAR_B_OFFICE,
        ToontownGlobals.LawbotStageIntC: locations.CLEAR_C_OFFICE,
        ToontownGlobals.LawbotStageIntD: locations.CLEAR_D_OFFICE,

        ToontownGlobals.BossbotCountryClubIntA: locations.CLEAR_FRONT_THREE,
        ToontownGlobals.BossbotCountryClubIntB: locations.CLEAR_MIDDLE_THREE,
        ToontownGlobals.BossbotCountryClubIntC: locations.CLEAR_BACK_THREE,
    }

    loc = FACILITY_LOCATION_CHECKS.get(facility_id)
    if not loc:
        return -1

    return ap_location_name_to_id(loc)


# Given a hood ID, return a list of AP check location names present in that hood
def hood_to_task_locations(hoodId: int):
    return {
        ToontownGlobals.ToontownCentral: locations.TTC_TASK_LOCATIONS,
        ToontownGlobals.DonaldsDock: locations.DD_TASK_LOCATIONS,
        ToontownGlobals.DaisyGardens: locations.DG_TASK_LOCATIONS,
        ToontownGlobals.MinniesMelodyland: locations.MM_TASK_LOCATIONS,
        ToontownGlobals.TheBrrrgh: locations.TB_TASK_LOCATIONS,
        ToontownGlobals.DonaldsDreamland: locations.DDL_TASK_LOCATIONS,
    }.get(hoodId, [])


def track_and_level_to_location(track: int, level: int):
    trackAndLevels = (
        (locations.TOONUP_FEATHER_UNLOCKED, locations.TOONUP_MEGAPHONE_UNLOCKED, locations.TOONUP_LIPSTICK_UNLOCKED, locations.TOONUP_CANE_UNLOCKED, locations.TOONUP_PIXIE_UNLOCKED, locations.TOONUP_JUGGLING_UNLOCKED, locations.TOONUP_HIGHDIVE_UNLOCKED),
        (locations.LURE_ONEBILL_UNLOCKED, locations.LURE_SMALLMAGNET_UNLOCKED, locations.LURE_FIVEBILL_UNLOCKED, locations.LURE_BIGMAGNET_UNLOCKED, locations.LURE_TENBILL_UNLOCKED, locations.LURE_HYPNO_UNLOCKED, locations.LURE_PRESENTATION_UNLOCKED),
        (locations.TRAP_BANANA_UNLOCKED, locations.TRAP_RAKE_UNLOCKED, locations.TRAP_MARBLES_UNLOCKED, locations.TRAP_QUICKSAND_UNLOCKED, locations.TRAP_TRAPDOOR_UNLOCKED, locations.TRAP_TNT_UNLOCKED, locations.TRAP_TRAIN_UNLOCKED),
        (locations.SOUND_BIKEHORN_UNLOCKED, locations.SOUND_WHISTLE_UNLOCKED, locations.SOUND_BUGLE_UNLOCKED, locations.SOUND_AOOGAH_UNLOCKED, locations.SOUND_TRUNK_UNLOCKED, locations.SOUND_FOG_UNLOCKED, locations.SOUND_OPERA_UNLOCKED),
        (locations.THROW_CUPCAKE_UNLOCKED, locations.THROW_FRUITPIESLICE_UNLOCKED, locations.THROW_CREAMPIESLICE_UNLOCKED, locations.THROW_WHOLEFRUIT_UNLOCKED, locations.THROW_WHOLECREAM_UNLOCKED, locations.THROW_CAKE_UNLOCKED, locations.THROW_WEDDING_UNLOCKED),
        (locations.SQUIRT_SQUIRTFLOWER_UNLOCKED, locations.SQUIRT_GLASS_UNLOCKED, locations.SQUIRT_SQUIRTGUN_UNLOCKED, locations.SQUIRT_SELTZER_UNLOCKED, locations.SQUIRT_HOSE_UNLOCKED, locations.SQUIRT_CLOUD_UNLOCKED, locations.SQUIRT_GEYSER_UNLOCKED),
        (locations.DROP_FLOWERPOT_UNLOCKED, locations.DROP_SANDBAG_UNLOCKED, locations.DROP_ANVIL_UNLOCKED, locations.DROP_BIGWEIGHT_UNLOCKED, locations.DROP_SAFE_UNLOCKED, locations.DROP_PIANO_UNLOCKED, locations.DROP_BOAT_UNLOCKED),
    )
    return trackAndLevels[track][level]
