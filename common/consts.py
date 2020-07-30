import os


def parent_path():
    path = os.getcwd()
    elements = path.split('/')

    p_path = ''
    for i in range(len(elements) - 1):
        p_path += elements[i] + '/'

    return p_path


_particles: list = [
    -999,  # 0 is used for padding

    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    4000001,
    4000002,
    4000011,
    4000012,
    21,
    22,
    23,
    24,
    25,
    32,
    33,
    34,
    35,
    36,
    37,
    1103,
    2101,
    2103,
    2203,
    3101,
    3103,
    3201,
    3203,
    3303,
    4101,
    4103,
    4201,
    4203,
    4301,
    4303,
    4403,
    5101,
    5103,
    5201,
    5203,
    5301,
    5303,
    5401,
    5403,
    5503,
    3000111,
    3000211,
    3000221,
    3100221,
    3000113,
    3000213,
    3000223,
    3100021,
    3060111,
    3160111,
    3130113,
    3140113,
    3150113,
    3160113,
    1000993,
    1009113,
    1009213,
    1009223,
    1009313,
    1009323,
    1009333,
    1091114,
    1092114,
    1092214,
    1092224,
    1093114,
    1093214,
    1093224,
    1093314,
    1093324,
    1093334,
    1000612,
    1000622,
    1000632,
    1000642,
    1000652,
    1006113,
    1006211,
    1006213,
    1006223,
    1006311,
    1006313,
    1006321,
    1006323,
    1006333,
    1000001,
    1000002,
    1000003,
    1000004,
    1000005,
    1000006,
    1000011,
    1000012,
    1000013,
    1000014,
    1000015,
    1000016,
    2000001,
    2000002,
    2000003,
    2000004,
    2000005,
    2000006,
    2000011,
    2000013,
    2000015,
    1000021,
    1000022,
    1000023,
    1000024,
    1000025,
    1000035,
    1000037,
    1000039,
    39,
    41,
    42,
    110,
    990,
    9990,
    111,
    211,
    9000111,
    9000211,
    100111,
    100211,
    10111,
    10211,
    9010111,
    9010211,
    113,
    213,
    10113,
    10213,
    20113,
    20213,
    9000113,
    9000213,
    100113,
    100213,
    9010113,
    9010213,
    9020113,
    9020213,
    30113,
    30213,
    9030113,
    9030213,
    9040113,
    9040213,
    115,
    215,
    10115,
    10215,
    9000115,
    9000215,
    9010115,
    9010215,
    117,
    217,
    9000117,
    9000217,
    9010117,
    9010217,
    119,
    219,
    221,
    331,
    9000221,
    9010221,
    100221,
    10221,
    9020221,
    100331,
    9030221,
    10331,
    9040221,
    9050221,
    9060221,
    9070221,
    9080221,
    223,
    333,
    10223,
    20223,
    10333,
    20333,
    100223,
    9000223,
    9010223,
    30223,
    100333,
    225,
    9000225,
    335,
    9010225,
    9020225,
    10225,
    9030225,
    10335,
    9040225,
    9050225,
    9060225,
    9070225,
    9080225,
    9090225,
    227,
    337,
    229,
    9000229,
    9010229,
    130,
    310,
    311,
    321,
    9000311,
    9000321,
    10311,
    10321,
    100311,
    100321,
    9010311,
    9010321,
    9020311,
    9020321,
    313,
    323,
    10313,
    10323,
    20313,
    20323,
    100313,
    100323,
    9000313,
    9000323,
    30313,
    30323,
    315,
    325,
    9000315,
    9000325,
    10315,
    10325,
    20315,
    20325,
    9010315,
    9010325,
    9020315,
    9020325,
    317,
    327,
    9010317,
    9010327,
    319,
    329,
    9000319,
    9000329,
    411,
    421,
    10411,
    10421,
    413,
    423,
    10413,
    10423,
    20413,
    20423,
    415,
    425,
    431,
    10431,
    433,
    10433,
    20433,
    435,
    511,
    521,
    10511,
    10521,
    513,
    523,
    10513,
    10523,
    20513,
    20523,
    515,
    525,
    531,
    10531,
    533,
    10533,
    20533,
    535,
    541,
    10541,
    543,
    10543,
    20543,
    545,
    441,
    10441,
    100441,
    443,
    10443,
    20443,
    100443,
    30443,
    9000443,
    9010443,
    9020443,
    445,
    100445,
    551,
    10551,
    100551,
    110551,
    200551,
    210551,
    553,
    10553,
    20553,
    30553,
    100553,
    110553,
    120553,
    130553,
    200553,
    210553,
    220553,
    300553,
    9000553,
    9010553,
    555,
    10555,
    20555,
    100555,
    110555,
    120555,
    200555,
    557,
    100557,
    2212,
    2112,
    2224,
    2214,
    2114,
    1114,
    3122,
    3222,
    3212,
    3112,
    3224,
    3214,
    3114,
    3322,
    3312,
    3324,
    3314,
    3334,
    4122,
    4222,
    4212,
    4112,
    4224,
    4214,
    4114,
    4232,
    4132,
    4322,
    4312,
    4324,
    4314,
    4332,
    4334,
    4412,
    4422,
    4414,
    4424,
    4432,
    4434,
    4444,
    9221132,
    9331122,
    5122,
    5112,
    5212,
    5222,
    5114,
    5214,
    5224,
    5132,
    5232,
    5312,
    5322,
    5314,
    5324,
    5332,
    5334,
    5142,
    5242,
    5412,
    5422,
    5414,
    5424,
    5342,
    5432,
    5434,
    5442,
    5444,
    5512,
    5522,
    5514,
    5524,
    5532,
    5534,
    5542,
    5544,
    5554,
]


def particles():
    parts = []
    for part in _particles:
        parts.append(int(part))
        parts.append(int(-1 * part))

    return parts


def particle_idxs():
    parts = []
    for i in range(len(particles())):
        parts.append(i)

    return parts


PARTICLE_COUNT = 2 * len(_particles)
PARTICLE_DIM = 52

PDG_EMB_CNT = PARTICLE_COUNT
PDG_EMB_DIM = PARTICLE_DIM
STAT_CODE_EMB_CNT = 2
STAT_CODE_EMB_DIM = 1

#PART_REFER_EMB_CNT = 1400
#PART_REFER_EMB_DIM = 72

HIST_POINTS = 100
BATCH_SIZE = 128  # 256
CONT_FEATURES = 10
#CAT_FEATURES = 6
CAT_FEATURES = 2
# EMB_FEATURES = CONT_FEATURES + PDG_EMB_DIM + STAT_CODE_EMB_DIM + 4 * PART_REFER_EMB_DIM
EMB_FEATURES = CONT_FEATURES + PDG_EMB_DIM + STAT_CODE_EMB_DIM
FEATURES = CONT_FEATURES + CAT_FEATURES
INP_RAND_SIZE = 128

MOUNT_PATH = os.getcwd()
