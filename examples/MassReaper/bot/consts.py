from typing import Set

from sc2.ids.unit_typeid import UnitTypeId

ATTACK_TARGET_IGNORE: Set[UnitTypeId] = {
    UnitTypeId.LARVA,
    UnitTypeId.EGG,
    UnitTypeId.CHANGELING,
    UnitTypeId.CHANGELINGMARINE,
    UnitTypeId.CHANGELINGMARINESHIELD,
    UnitTypeId.CHANGELINGZEALOT,
    UnitTypeId.CHANGELINGZERGLING,
    UnitTypeId.CHANGELINGZERGLINGWINGS,
}

ALL_STRUCTURES: Set[UnitTypeId] = {
    UnitTypeId.ARMORY,
    UnitTypeId.ASSIMILATOR,
    UnitTypeId.ASSIMILATORRICH,
    UnitTypeId.AUTOTURRET,
    UnitTypeId.BANELINGNEST,
    UnitTypeId.BARRACKS,
    UnitTypeId.BARRACKSFLYING,
    UnitTypeId.BARRACKSREACTOR,
    UnitTypeId.BARRACKSTECHLAB,
    UnitTypeId.BUNKER,
    UnitTypeId.BYPASSARMORDRONE,
    UnitTypeId.COMMANDCENTER,
    UnitTypeId.COMMANDCENTERFLYING,
    UnitTypeId.CREEPTUMOR,
    UnitTypeId.CREEPTUMORBURROWED,
    UnitTypeId.CREEPTUMORQUEEN,
    UnitTypeId.CYBERNETICSCORE,
    UnitTypeId.DARKSHRINE,
    UnitTypeId.ELSECARO_COLONIST_HUT,
    UnitTypeId.ENGINEERINGBAY,
    UnitTypeId.EVOLUTIONCHAMBER,
    UnitTypeId.EXTRACTOR,
    UnitTypeId.EXTRACTORRICH,
    UnitTypeId.FACTORY,
    UnitTypeId.FACTORYFLYING,
    UnitTypeId.FACTORYREACTOR,
    UnitTypeId.FACTORYTECHLAB,
    UnitTypeId.FLEETBEACON,
    UnitTypeId.FORGE,
    UnitTypeId.FUSIONCORE,
    UnitTypeId.GATEWAY,
    UnitTypeId.GHOSTACADEMY,
    UnitTypeId.GREATERSPIRE,
    UnitTypeId.HATCHERY,
    UnitTypeId.HIVE,
    UnitTypeId.HYDRALISKDEN,
    UnitTypeId.INFESTATIONPIT,
    UnitTypeId.LAIR,
    UnitTypeId.LURKERDENMP,
    UnitTypeId.MISSILETURRET,
    UnitTypeId.NEXUS,
    UnitTypeId.NYDUSCANAL,
    UnitTypeId.NYDUSCANALATTACKER,
    UnitTypeId.NYDUSCANALCREEPER,
    UnitTypeId.NYDUSNETWORK,
    UnitTypeId.ORACLESTASISTRAP,
    UnitTypeId.ORBITALCOMMAND,
    UnitTypeId.ORBITALCOMMANDFLYING,
    UnitTypeId.PHOTONCANNON,
    UnitTypeId.PLANETARYFORTRESS,
    UnitTypeId.POINTDEFENSEDRONE,
    UnitTypeId.PYLON,
    UnitTypeId.PYLONOVERCHARGED,
    UnitTypeId.RAVENREPAIRDRONE,
    UnitTypeId.REACTOR,
    UnitTypeId.REFINERY,
    UnitTypeId.REFINERYRICH,
    UnitTypeId.RESOURCEBLOCKER,
    UnitTypeId.ROACHWARREN,
    UnitTypeId.ROBOTICSBAY,
    UnitTypeId.ROBOTICSFACILITY,
    UnitTypeId.SENSORTOWER,
    UnitTypeId.SHIELDBATTERY,
    UnitTypeId.SPAWNINGPOOL,
    UnitTypeId.SPINECRAWLER,
    UnitTypeId.SPINECRAWLERUPROOTED,
    UnitTypeId.SPIRE,
    UnitTypeId.SPORECRAWLER,
    UnitTypeId.SPORECRAWLERUPROOTED,
    UnitTypeId.STARGATE,
    UnitTypeId.STARPORT,
    UnitTypeId.STARPORTFLYING,
    UnitTypeId.STARPORTREACTOR,
    UnitTypeId.STARPORTTECHLAB,
    UnitTypeId.SUPPLYDEPOT,
    UnitTypeId.SUPPLYDEPOTLOWERED,
    UnitTypeId.TECHLAB,
    UnitTypeId.TEMPLARARCHIVE,
    UnitTypeId.TWILIGHTCOUNCIL,
    UnitTypeId.ULTRALISKCAVERN,
    UnitTypeId.WARPGATE,
}
