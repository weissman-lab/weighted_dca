# clean data
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

# get ssh connection to Grace to read data from data/nlst/participant.data.d100517.csv
data_raw = pd.read_csv("/data/nlst/participant.data.d100517.csv", low_memory=False)
# only required features
data = data_raw[
    [
        "pid",
        "educat",
        "rndgroup",
        "age",
        "ethnic",
        "gender",
        "race",
        "weight",
        "cigar",
        "pkyr",
        "smokeage",
        "smokeyr",
        "can_scr",
        "resasbe",
        "resbaki",
        "resbutc",
        "reschem",
        "rescoal",
        "rescott",
        "resfarm",
        "resfire",
        "resflou",
        "resfoun",
        "reshard",
        "respain",
        "ressand",
        "resweld",
        "wrkasbe",
        "wrkbaki",
        "wrkbutc",
        "wrkchem",
        "wrkcoal",
        "wrkcott",
        "wrkfarm",
        "wrkfire",
        "wrkflou",
        "wrkfoun",
        "wrkhard",
        "wrkpain",
        "wrksand",
        "wrkweld",
        "diagadas",
        "diagasbe",
        "diagbron",
        "diagchas",
        "diagchro",
        "diagcopd",
        "diagdiab",
        "diagemph",
        "diagfibr",
        "diaghear",
        "diaghype",
        "diagpneu",
        "diagsarc",
        "diagsili",
        "diagstro",
        "diagtube",
        "cancblad",
        "cancbrea",
        "canccerv",
        "canccolo",
        "cancesop",
        "canckidn",
        "canclary",
        "canclung",
        "cancnasa",
        "cancoral",
        "cancpanc",
        "cancphar",
        "cancstom",
        "cancthyr",
        "canctran",
        "fambrother",
        "famchild",
        "famfather",
        "fammother",
        "famsister",
        "scr_res0",
        "scr_res1",
        "scr_res2",
    ]
]
print(data.dtypes)
# create family_hist feature
data["family_hist"] = np.where(
    (data["fambrother"] == 1.0)
    | (data["famchild"] == 1.0)
    | (data["famfather"] == 1.0)
    | (data["fammother"] == 1.0)
    | (data["famsister"] == 1.0),
    1,
    0,
)
data.drop(
    ["fambrother", "famchild", "famfather", "fammother", "famsister"],
    axis=1,
    inplace=True,
)
# create cancer_hist feature

data["cancer_hist"] = np.where(
    (data["cancblad"] == 1.0)
    | (data["cancbrea"] == 1.0)
    | (data["canccerv"] == 1.0)
    | (data["canccolo"] == 1.0)
    | (data["cancesop"] == 1.0)
    | (data["canckidn"] == 1.0)
    | (data["canclary"] == 1.0)
    | (data["canclung"] == 1.0)
    | (data["cancnasa"] == 1.0)
    | (data["cancoral"] == 1.0)
    | (data["cancpanc"] == 1.0)
    | (data["cancphar"] == 1.0)
    | (data["cancstom"] == 1.0)
    | (data["cancthyr"] == 1.0)
    | (data["canctran"] == 1.0),
    1,
    0,
)
data.drop(
    [
        "cancblad",
        "cancbrea",
        "canccerv",
        "canccolo",
        "cancesop",
        "canckidn",
        "canclary",
        "canclung",
        "cancnasa",
        "cancoral",
        "cancpanc",
        "cancphar",
        "cancstom",
        "cancthyr",
        "canctran",
    ],
    axis=1,
    inplace=True,
)
# create work_hist feature

data["work_hist"] = np.where(
    (np.in1d(data["resasbe"], [2.0, 0.0]))
    | (np.in1d(data["resbaki"], [2.0, 0.0]))
    | (np.in1d(data["resbutc"], [2.0, 0.0]))
    | (np.in1d(data["reschem"], [2.0, 0.0]))
    | (np.in1d(data["rescoal"], [2.0, 0.0]))
    | (np.in1d(data["rescott"], [2.0, 0.0]))
    | (np.in1d(data["resfarm"], [2.0, 0.0]))
    | (np.in1d(data["resfire"], [2.0, 0.0]))
    | (np.in1d(data["resflou"], [2.0, 0.0]))
    | (np.in1d(data["resfoun"], [2.0, 0.0]))
    | (np.in1d(data["reshard"], [2.0, 0.0]))
    | (np.in1d(data["respain"], [2.0, 0.0]))
    | (np.in1d(data["ressand"], [2.0, 0.0]))
    | (np.in1d(data["resweld"], [2.0, 0.0])),
    1,
    0,
)
data.drop_duplicates
data["cancer"] = np.where(data["can_scr"] == 0, 0, 1)
data.drop(
    [
        "resasbe",
        "resbaki",
        "resbutc",
        "reschem",
        "rescoal",
        "rescott",
        "resfarm",
        "resfire",
        "resflou",
        "resfoun",
        "reshard",
        "respain",
        "ressand",
        "resweld",
        "wrkasbe",
        "wrkbaki",
        "wrkbutc",
        "wrkchem",
        "wrkcoal",
        "wrkcott",
        "wrkfarm",
        "wrkfire",
        "wrkflou",
        "wrkfoun",
        "wrkhard",
        "wrkpain",
        "wrksand",
        "wrkweld",
        "can_scr",
    ],
    axis=1,
    inplace=True,
)
# create disease_hist feature

data["disease_hist"] = np.where(
    (data["diagadas"] == 1.0)
    | (data["diagasbe"] == 1.0)
    | (data["diagbron"] == 1.0)
    | (data["diagchas"] == 1.0)
    | (data["diagchro"] == 1.0)
    | (data["diagcopd"] == 1.0)
    | (data["diagdiab"] == 1.0)
    | (data["diagemph"] == 1.0)
    | (data["diagfibr"] == 1.0)
    | (data["diaghear"] == 1.0)
    | (data["diaghype"] == 1.0)
    | (data["diagpneu"] == 1.0)
    | (data["diagsarc"] == 1.0)
    | (data["diagsili"] == 1.0)
    | (data["diagstro"] == 1.0)
    | (data["diagtube"] == 1.0),
    1,
    0,
)
data.drop(
    [
        "diagadas",
        "diagasbe",
        "diagbron",
        "diagchas",
        "diagchro",
        "diagcopd",
        "diagdiab",
        "diagemph",
        "diagfibr",
        "diaghear",
        "diaghype",
        "diagpneu",
        "diagsarc",
        "diagsili",
        "diagstro",
        "diagtube",
    ],
    axis=1,
    inplace=True,
)

# add scerrning features
data["scr_res_0"] = np.where(
    data["scr_res0"].isin([1, 2, 3]),
    "negative",
    np.where(data["scr_res0"].isin([4, 5, 6]), "positive", "other"),
)
data["scr_res_1"] = np.where(
    data["scr_res1"].isin([1, 2, 3]),
    "negative",
    np.where(data["scr_res1"].isin([4, 5, 6]), "positive", "other"),
)
data["scr_res_2"] = np.where(
    data["scr_res2"].isin([1, 2, 3]),
    "negative",
    np.where(data["scr_res2"].isin([4, 5, 6]), "positive", "other"),
)
data.drop(["scr_res0", "scr_res1", "scr_res2"], axis=1, inplace=True)

# check the nulls if any
print((data.isnull().sum()) / 53542)
print(data.isnull().sum())

# push data for modeling
data.to_csv("data/data_ready_binary.csv", index=False)
