from __future__ import annotations
from datetime import timedelta

from settings import static_url, PROD

# https://medium.com/quick-code/python-type-hinting-eliminating-importerror-due-to-circular-imports-265dfb0580f8
TYPE_CHECKING = False

DASH = "–"
ANON_PREFIX = "Anon" + DASH

NONE_USER = "None" + DASH + "User"

SCHEDULE_MAX_DAYS = 7
TOURNAMENT_SPOTLIGHTS_MAX = 3

# Max notify documents TTL (time to live) weeks
NOTIFY_EXPIRE_WEEKS = timedelta(weeks=4)
NOTIFY_PAGE_SIZE = 7

# Max corr seek documents TTL (time to live) weeks
CORR_SEEK_EXPIRE_WEEKS = timedelta(weeks=2)

# Max number of lobby chat lines (deque limit)
MAX_CHAT_LINES = 100

# Minimum number of rated games needed
HIGHSCORE_MIN_GAMES = 10

MAX_HIGHSCORE_ITEM_LIMIT = 50

# Show the number of spectators only after this limit
MAX_NAMED_SPECTATORS = 20

# tournament status
T_CREATED, T_STARTED, T_ABORTED, T_FINISHED, T_ARCHIVED = range(5)

# tournament frequency
HOURLY, DAILY, WEEKLY, MONTHLY, YEARLY, MARATHON, SHIELD = "h", "d", "w", "m", "y", "a", "s"

# tournament pairing
ARENA, RR, SWISS = range(3)

# translations
LANGUAGES = [
    "de",
    "en",
    "es",
    "gl_ES",
    "fr",
    "hu",
    "it",
    "ja",
    "ko",
    "nl",
    "pl",
    "pt",
    "ru",
    "th",
    "tr",
    "vi",
    "zh_CN",
    "zh_TW",
]

# fishnet work types
MOVE, ANALYSIS = 0, 1

# game types
CASUAL, RATED, IMPORTED = 0, 1, 2

# game status
(
    CREATED,
    STARTED,
    ABORTED,
    MATE,
    RESIGN,
    STALEMATE,
    TIMEOUT,
    DRAW,
    FLAG,
    ABANDON,
    CHEAT,
    BYEGAME,
    INVALIDMOVE,
    UNKNOWNFINISH,
    VARIANTEND,
    CLAIM,
) = range(-2, 14)

LOSERS = {
    "abandon": ABANDON,
    "abort": ABORTED,
    "resign": RESIGN,
    "flag": FLAG,
}

GRANDS = ("xiangqi", "manchu", "grand", "grandhouse", "shako", "janggi",
          "omega10", "tencubed", "wildebeest", "reformedcourier")

CONSERVATIVE_CAPA_FEN = "arnbqkbnrc/pppppppppp/10/10/10/10/PPPPPPPPPP/ARNBQKBNRC w KQkq - 0 1"

VARIANTS = (
    "chess",
    "chess960",
    "bughouse",
    "bughouse960",
    "crazyhouse",
    "crazyhouse960",
    "atomic",
    "atomic960",
    "kingofthehill",
    "kingofthehill960",
    "3check",
    "3check960",
    "placement",
    "duck",
    "makruk",
    "makpong",
    "cambodian",
    "sittuyin",
    "asean",
    "shogi",
    "minishogi",
    "kyotoshogi",
    "dobutsu",
    # Gorogoro is superseded by Gorogoro Plus
    # "gorogoro",
    "gorogoroplus",
    "torishogi",
    "cannonshogi",
    "xiangqi",
    "manchu",
    "janggi",
    "minixiangqi",
    "capablanca",
    "capablanca960",
    "capahouse",
    "capahouse960",
    # We support to import/store/analyze these variants
    # but don't support to add them to leaderboard page
    # "gothic",
    # "gothhouse",
    # "embassy",
    "dragon",
    "seirawan",
    "seirawan960",
    "shouse",
    "grand",
    "grandhouse",
    "shogun",
    "shako",
    "hoppelpoppel",
    "mansindam",
    "orda",
    "khans",
    "synochess",
    # Shinobi is superseded by Shinobiplus Plus
    # "shinobi",
    "shinobiplus",
    "empire",
    "ordamirror",
    "chak",
    "chennis",
    "spartan",
    "ataxx",
    # Alternates
    "anticapablanca",
    "anticapablanca960",
    "antichess",
    "antichess960",
    "antimak",
    "atomar",
    "atomar960",
    "atomarhouse",
    "atomarhouse960",
    "atomicduck",
    "atomicgiveaway",
    "atomicgiveaway960",
    "backrank",
    "backrank960",
    "berolina",
    "berolina960",
    "cetus",
    "coffeehouse",
    "coffeehouse960",
    "coffeeshogi",
    "coffeethreecheck",
    "coffeethreecheck960",
    "coregal",
    "coregal960",
    "dragonfly",
    "extinction",
    "extinction960",
    "gethenian",
    "grasshopper",
    "grasshopperking",
    "grasshopperking960",
    "jesonmor",
    "joust",
    "judkins",
    "kamikazerooks",
    "karouk",
    "khansmirror",
    "kinglet",
    "kinglet960",
    "knightmate",
    "legan",
    "losers",
    "losers960",
    "mak3check",
    "makhill",
    "makhouse",
    "maktomic",
    "nightrider",
    "nightrider960",
    "omega10",
    "paradigm30",
    "pawnsideways",
    "pawnsideways960",
    "petrified",
    "petrified960",
    "pocketknight",
    "pocketknight960",
    "racingchess",
    "racingchess960",
    "reformedcourier",
    "schism",
    "shatranj",
    "shatranjhouse",
    "shinobiplusmirror",
    "spartanmirror",
    "tencubed",
    "torpedo",
    "torpedo960",
    "whaleshogi",
    "wildebeest",
    "yarishogi",
)

# Remove bughouse from variants on prod site until it stabilizes
if PROD:
    VARIANTS = tuple(e for e in VARIANTS if not e.startswith("bughouse"))

VARIANT_ICONS = {
    "ataxx": "☣",
    "makruk": "Q",
    "makpong": "O",
    "sittuyin": ":",
    "shogi": "K",
    "janggi": "=",
    "xiangqi": "|",
    "chess": "M",
    "crazyhouse": "+",
    "placement": "S",
    "capablanca": "P",
    "capahouse": "&",
    "dragon": "🐉",
    "seirawan": "L",
    "seirawan960": "}",
    "shouse": "$",
    "grand": "(",
    "grandhouse": "*",
    "gothic": "P",
    "gothhouse": "&",
    "embassy": "P",
    "embassyhouse": "&",
    "minishogi": "6",
    "dobutsu": "8",
    "gorogoro": "🐱",
    "gorogoroplus": "🐱",
    "torishogi": "🐦",
    "cannonshogi": "💣",
    "cambodian": "!",
    "shako": "9",
    "minixiangqi": "7",
    "chess960": "V",
    "capablanca960": ",",
    "capahouse960": "'",
    "crazyhouse960": "%",
    "kyotoshogi": ")",
    "shogun": "-",
    "orda": "R",
    "khans": "🐎",
    "synochess": "_",
    "hoppelpoppel": "`",
    "manchu": "{",
    "atomic": "~",
    "atomic960": "\\",
    "shinobi": "🐢",
    "shinobiplus": "🐢",
    "empire": "♚",
    "ordamirror": "◩",
    "asean": "♻",
    "chak": "🐬",
    "chennis": "🎾",
    "mansindam": "⛵",
    "duck": "🦆",
    "spartan": "⍺",
    "schism": "🪓",
    "kingofthehill": "🏴",
    "kingofthehill960": "🏁",
    "3check": "☰",
    "3check960": "☷",
    "bughouse": "¢",
    "bughouse960": "⌀",
    # Alternates
    "anticapablanca": "P",
    "anticapablanca960": "P",
    "antichess": "🙃",
    "antichess960": "🙃",
    "antimak": "Q",
    "atomar": "🤯",
    "atomar960": "🤯",
    "atomarhouse": "🤯",
    "atomarhouse960": "🤯",
    "atomicduck": "🦆",
    "atomicgiveaway": "👎",
    "atomicgiveaway960": "👎",
    "backrank": "☝️",
    "backrank960": "☝️",
    "berolina": "🥨",
    "berolina960": "🥨",
    "cetus": "🐳",
    "coffeehouse": "☕",
    "coffeehouse960": "☕",
    "coffeeshogi": "K",
    "coffeethreecheck": "☕",
    "coffeethreecheck960": "☕",
    "coregal": "🧑‍🤝‍🧑",
    "coregal960": "🧑‍🤝‍🧑",
    "dragonfly": "🍃",
    "extinction": "☠️",
    "extinction960": "☠️",
    "gethenian": "✋",
    "grasshopper": "🦗",
    "grasshopperking": "🦗",
    "grasshopperking960": "🦗",
    "jesonmor": "🏇",
    "joust": "🦄",
    "judkins": "6️⃣",
    "kamikazerooks": "🏰",
    "karouk": "!",
    "khansmirror": "🐎",
    "kinglet": "🤴",
    "kinglet960": "🤴",
    "knightmate": "🪖",
    "legan": "↖️",
    "losers": "👎",
    "losers960": "👎",
    "mak3check": "Q",
    "makhill": "Q",
    "makhouse": "Q",
    "maktomic": "Q",
    "nightrider": "🌠",
    "nightrider960": "🌠",
    "omega10": "Ω",
    "paradigm30": "🐲",
    "pawnsideways": "↔️",
    "pawnsideways960": "↔️",
    "petrified": "🪨",
    "petrified960": "🪨",
    "pocketknight": "🐴",
    "pocketknight960": "🐴",
    "racingchess": "🔃",
    "racingchess960": "🔃",
    "reformedcourier": "✉️",
    "shatranj": "🐘",
    "shatranjhouse": "🐘",
    "shinobiplusmirror": "🐢",
    "spartanmirror": "⍺",
    "tencubed": "📦",
    "torpedo": "🏄",
    "torpedo960": "🏄",
    "whaleshogi": "🐋",
    "wildebeest": "🐃",
    "yarishogi": "🆙",
}

VARIANT_960_TO_PGN = {
    "bughouse": "Bughouse960",
    "chess": "Chess960",
    "capablanca": "Caparandom",
    "capahouse": "Capahouse960",
    "crazyhouse": "Crazyhouse",  # to let lichess import work
    "atomic": "Atomic",  # to let lichess import work
    "kingofthehill": "King of the Hill",  # to let lichess import work
    "3check": "Three-check",  # to let lichess import work
    "seirawan": "Seirawan960",
    # some early game is accidentally saved as 960 in mongodb
    "shogi": "Shogi",
    "sittuyin": "Sittuyin",
    "makruk": "Makruk",
    "placement": "Placement",
    "grand": "Grand",
    # Alternates
    "anticapablanca": "Anticapablanca",
    "antichess": "Antichess",
    "atomar": "Atomar",
    "atomarhouse": "Atomarhouse",
    "atomicgiveaway": "Atomic Giveaway",
    "backrank": "Backrank",
    "berolina": "Berolina",
    "coffeehouse": "Coffeehouse",
    "coffeethreecheck": "Coffee Three-check",
    "coregal": "Coregal",
    "extinction": "Extinction",
    "grassopperking": "Grasshopper King",
    "kinglet": "Kinglet",
    "losers": "Losers",
    "nightrider": "Nightrider",
    "pawnsideways": "Pawnsideways",
    "petrified": "Petrified",
    "pocketknight": "Pocket Knight",
    "racingchess": "Racing Chess",
    "torpedo": "Torpedo",
}

CATEGORIES = {
    "chess": (
        "chess",
        "chess960",
        "bughouse",
        "bughouse960",
        "crazyhouse",
        "crazyhouse960",
        "placement",
        "atomic",
        "atomic960",
        "kingofthehill",
        "kingofthehill960",
        "3check",
        "3check960",
        "duck",
        # Alternates
        "antichess",
        "antichess960",
        "atomar",
        "atomar960",
        "atomarhouse",
        "atomarhouse960",
        "atomicduck",
        "atomicgiveaway",
        "atomicgiveaway960",
        "backrank",
        "backrank960",
        "berolina",
        "berolina960",
        "coffeehouse",
        "coffeehouse960",
        "coffeethreecheck",
        "coffeethreecheck960",
        "coregal",
        "coregal960",
        "dragonfly",
        "extinction",
        "extinction960",
        "kamikazerooks",
        "kinglet",
        "kinglet960",
        "knightmate",
        "legan",
        "losers",
        "losers960",
        "pawnsideways",
        "pawnsideways960",
        "petrified",
        "petrified960",
        "pocketknight",
        "pocketknight960",
        "racingchess",
        "racingchess960",
        "torpedo",
        "torpedo960",
    ),
    "fairy": (
        "capablanca",
        "capablanca960",
        "capahouse",
        "capahouse960",
        "dragon",
        "seirawan",
        "seirawan960",
        "shouse",
        "grand",
        "grandhouse",
        "shako",
        "shogun",
        "hoppelpoppel",
        "mansindam",
        "anticapablanca",
        "anticapablanca960",
        "grasshopper",
        "grasshopperking",
        "grasshopperking960",
        "nightrider",
        "nightrider960",
        "omega10",
        "paradigm30",
        "reformedcourier",
        "shatranj",
        "shatranjhouse",
        "tencubed",
        "wildebeest",
    ),
    "army": (
        "orda",
        "khans",
        "synochess",
        "empire",
        "ordamirror",
        "chak",
        "chennis",
        "shinobiplus",
        "spartan",
        "gethenian",
        "khansmirror",
        "schism",
        "shinobiplusmirror",
        "spartanmirror",
    ),
    "makruk": (
        "makruk",
        "makpong",
        "cambodian",
        "sittuyin",
        "asean",
        "antimak",
        "karouk",
        "mak3check",
        "makhill",
        "makhouse",
        "maktomic",
    ),
    "shogi": (
        "shogi",
        "minishogi",
        "kyotoshogi",
        "dobutsu",
        "gorogoroplus",
        "torishogi",
        "cannonshogi",
        "coffeeshogi",
        "judkins",
        "whaleshogi",
        "yarishogi",
    ),
    "xiangqi": (
        "xiangqi",
        "manchu",
        "janggi",
        "minixiangqi",
    ),
    "other": (
        "ataxx",
        "cetus",
        "jesonmor",
        "joust",
    ),
}

VARIANT_GROUPS = {}
for categ in CATEGORIES:
    for variant in CATEGORIES[categ]:
        VARIANT_GROUPS[variant] = categ

TROPHIES = {
    "top1": (static_url("images/trophy/Big-Gold-Cup.png"), "Champion!"),
    "top10": (static_url("images/trophy/Big-Silver-Cup.png"), "Top 10!"),
    "top50": (static_url("images/trophy/Fancy-Gold-Cup.png"), "Top 50!"),
    "top100": (static_url("images/trophy/Gold-Cup.png"), "Top 100!"),
    "shield": (static_url("images/trophy/shield-gold.png"), "Shield"),
    # some example custom trophy from lichess
    "acwc19": (static_url("images/trophy/acwc19.png"), "World Champion 2019"),
    "3wc21": (static_url("images/trophy/3wc21.png"), "World Champion 2021"),
}


def variant_display_name(variant):
    if variant == "seirawan":
        return "S-CHESS"
    elif variant == "seirawan960":
        return "S-CHESS960"
    elif variant == "shouse":
        return "S-HOUSE"
    elif variant == "cambodian":
        return "OUK CHAKTRANG"
    elif variant == "ordamirror":
        return "ORDA MIRROR"
    elif variant == "gorogoroplus":
        return "GOROGORO+"
    elif variant == "kyotoshogi":
        return "KYOTO SHOGI"
    elif variant == "torishogi":
        return "TORI SHOGI"
    elif variant == "cannonshogi":
        return "CANNON SHOGI"
    elif variant == "duck":
        return "DUCK CHESS"
    elif variant == "kingofthehill":
        return "KING OF THE HILL"
    elif variant == "3check":
        return "THREE-CHECK"
    elif variant == "dragon":
        return "DRAGON CHESS"
    elif variant == "grasshopperking":
        return "GRASSHOPPER KING"
    else:
        return variant.upper()


#  Deferred translations!


def _(message):
    return message


TRANSLATED_PAIRING_SYSTEM_NAMES = {
    0: _("Arena"),
    1: _("Round-Robin"),
    2: _("Swiss"),
}

TRANSLATED_FREQUENCY_NAMES = {
    "h": _("Hourly"),
    "d": _("Daily"),
    "w": _("Weekly"),
    "m": _("Monthly"),
    "y": _("Yearly"),
    "a": _("Marathon"),
    "s": _("Shield"),
    "S": _("SEAturday"),
}

TRANSLATED_VARIANT_NAMES = {
    "ataxx": _("Ataxx"),
    "chess": _("Chess"),
    "chess960": _("Chess960"),
    "crazyhouse": _("Crazyhouse"),
    "crazyhouse960": _("Crazyhouse960"),
    "placement": _("Placement"),
    "atomic": _("Atomic"),
    "atomic960": _("Atomic960"),
    "duck": _("Duck Chess"),
    "makruk": _("Makruk"),
    "makpong": _("Makpong"),
    "cambodian": _("Ouk Chaktrang"),
    "sittuyin": _("Sittuyin"),
    "asean": _("ASEAN"),
    "shogi": _("Shogi"),
    "minishogi": _("Minishogi"),
    "kyotoshogi": _("Kyoto Shogi"),
    "dobutsu": _("Dobutsu"),
    "bughouse": _("Bughouse"),
    "bughouse960": _("Bughouse960"),
    # Gorogoro is superseded by Gorogoro Plus
    # "gorogoro",
    "gorogoroplus": _("Gorogoro+"),
    "torishogi": _("Tori Shogi"),
    "cannonshogi": _("Cannon Shogi"),
    "xiangqi": _("Xiangqi"),
    "manchu": _("Manchu"),
    "janggi": _("Janggi"),
    "minixiangqi": _("Minixiangqi"),
    "capablanca": _("Capablanca"),
    "capablanca960": _("Capablanca960"),
    "capahouse": _("Capahouse"),
    "capahouse960": _("Capahouse960"),
    # We support to import/store/analyze these variants
    # but don't support to add them to leaderboard page
    # "gothic",
    # "gothhouse",
    # "embassy",
    "dragon": _("Dragon Chess"),
    "seirawan": _("S-Chess"),
    "seirawan960": _("S-Chess960"),
    "shouse": _("S-House"),
    "grand": _("Grand"),
    "grandhouse": _("Grandhouse"),
    "shogun": _("Shogun"),
    "shako": _("Shako"),
    "hoppelpoppel": _("Hoppel-Poppel"),
    "orda": _("Orda Chess"),
    "khans": _("Khan's Chess"),
    "synochess": _("Synochess"),
    "shinobi": _("Shinobi"),
    "shinobiplus": _("Shinobi+"),
    "empire": _("Empire"),
    "ordamirror": _("Orda Mirror"),
    "chak": _("Chak"),
    "chennis": _("Chennis"),
    "spartan": _("Spartan"),
    "schism": _("Schism"),
    "kingofthehill": _("King of the Hill"),
    "kingofthehill960": _("King of the Hill 960"),
    "3check": _("Three check"),
    "3check960": _("Three check 960"),
    "mansindam": _("Mansindam"),
    # Alternates
    "anticapablanca": _("Anticapablanca"),
    "anticapablanca960": _("Anticapablanca 960"),
    "antichess": _("Antichess"),
    "antichess960": _("Antichess 960"),
    "antimak": _("Antimakruk"),
    "atomar": _("Atomar"),
    "atomar960": _("Atomar 960"),
    "atomarhouse": _("Atomarhouse"),
    "atomarhouse960": _("Atomarhouse 960"),
    "atomicduck": _("Atomic Duck"),
    "atomicgiveaway": _("Atomic Giveaway"),
    "atomicgiveaway960": _("Atomic Giveaway 960"),
    "backrank": _("Backrank"),
    "backrank960": _("Backrank 960"),
    "berolina": _("Berolina"),
    "berolina960": _("Berolina 960"),
    "cetus": _("Cetus"),
    "coffeehouse": _("Coffeehouse"),
    "coffeehouse960": _("Coffeehouse 960"),
    "coffeeshogi": _("Coffee Shogi"),
    "coffeethreecheck": _("Coffee 3-check"),
    "coffeethreecheck960": _("Coffee 3-check 960"),
    "coregal": _("Coregal"),
    "coregal960": _("Coregal 960"),
    "dragonfly": _("Dragonfly"),
    "extinction": _("Extinction"),
    "extinction960": _("Extinction 960"),
    "gethenian": _("Gethenian"),
    "grasshopper": _("Grasshopper"),
    "grasshopperking": _("Grasshopper King"),
    "grasshopperking960": _("Grasshopper King 960"),
    "jesonmor": _("Jeson Mor"),
    "joust": _("Joust"),
    "judkins": _("Judkins Shogi"),
    "kamikazerooks": _("Kamikaze Rooks"),
    "karouk": _("Kar Ouk"),
    "khansmirror": _("Khans Mirror"),
    "kinglet": _("Kinglet"),
    "kinglet960": _("Kinglet 960"),
    "knightmate": _("Knightmate"),
    "legan": _("Legan Chess"),
    "losers": _("Loser's Chess"),
    "losers960": _("Loser's Chess 960"),
    "mak3check": _("Makruk 3-check"),
    "makhill": _("Makruk Hill"),
    "makhouse": _("Makruk House"),
    "maktomic": _("Makruk Atomic"),
    "nightrider": _("Nightrider"),
    "nightrider960": _("Nightrider 960"),
    "omega10": _("Omega10"),
    "paradigm30": _("Paradigm Chess 30"),
    "pawnsideways": _("Pawnsidweays"),
    "pawnsideways960": _("Pawnsideways 960"),
    "petrified": _("Petrified"),
    "petrified960": _("Petrified960"),
    "pocketknight": _("Pocket Knight"),
    "pocketknight960": ("Pocket Knight 960"),
    "racingchess": _("Racing Chess"),
    "racingchess960": _("Racing Chess 960"),
    "reformedcourier": _("Reformed Courier-Spiel"),
    "shatranj": _("Shatranj"),
    "shatranjhouse": _("Shatranj House"),
    "shinobiplusmirror": _("Shinobi+ Mirror"),
    "spartanmirror": _("Spartan Mirror"),
    "tencubed": _("TenCubed"),
    "torpedo": _("Torpedo"),
    "torpedo960": _("Torpedo 960"),
    "whaleshogi": _("Whale Shogi"),
    "wildebeest": _("Wildebeest"),
    "yarishogi": _("Yari Shogi"),
}

del _
