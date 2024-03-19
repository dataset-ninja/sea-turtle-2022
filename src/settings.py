from typing import Dict, List, Literal, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "Sea Turtle 2022"
PROJECT_NAME_FULL: str = "Sea Turtle ID 2022 Dataset"
HIDE_DATASET = True  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.Custom(
    source_url="https://www.kaggle.com/datasets/wildlifedatasets/seaturtleid2022?select=license.txt"
)
APPLICATIONS: List[Union[Industry, Domain, Research]] = [
    Research.Environmental(),
    Industry.Fishery(),
]
CATEGORY: Category = Category.Environmental(extra=[Category.Livestock()])

CV_TASKS: List[CVTask] = [
    CVTask.InstanceSegmentation(),
    CVTask.SemanticSegmentation(),
    CVTask.ObjectDetection(),
    CVTask.Localization(),
]
ANNOTATION_TYPES: List[AnnotationType] = [
    AnnotationType.InstanceSegmentation(),
    AnnotationType.ObjectDetection(),
]

RELEASE_DATE: Optional[str] = None  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = 2022

HOMEPAGE_URL: str = "https://www.kaggle.com/datasets/wildlifedatasets/seaturtleid2022"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 16200774
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/sea-turtle-2022"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = (
    "https://www.kaggle.com/datasets/wildlifedatasets/seaturtleid2022/download?datasetVersionNumber=3"
)
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]] or Literal["predefined"]] = {
    "turtle": [230, 25, 75],
    "flipper": [60, 180, 75],
    "head": [255, 225, 25],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

# If you have more than the one paper, put the most relatable link as the first element of the list
# Use dict key to specify name for a button
PAPER: Optional[Union[str, List[str], Dict[str, str]]] = (
    "https://openaccess.thecvf.com/content/WACV2024/html/Adam_SeaTurtleID2022_A_Long-Span_Dataset_for_Reliable_Sea_Turtle_Re-Identification_WACV_2024_paper.html"
)
BLOGPOST: Optional[Union[str, List[str], Dict[str, str]]] = None
REPOSITORY: Optional[Union[str, List[str], Dict[str, str]]] = None

CITATION_URL: Optional[str] = None
AUTHORS: Optional[List[str]] = [
    "Lukas Adam",
    "Vojtech Cermak",
    "Kostas Papafitsoros",
    "Lukas Picek",
]
AUTHORS_CONTACTS: Optional[List[str]] = [
    "lukas.adam.cr@gmail.com",
    "cermavo3@fel.cvut.cz",
    "k.papafitsoros@qmul.ac.uk",
    "picekl@kky.zcu.cz",
    "lpicek@inria.cz",
]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = [
    "Czech Technical University, Czech",
    "Queen Mary University of London, UK",
]
ORGANIZATION_URL: Optional[Union[str, List[str]]] = [
    "https://www.cvut.cz/en",
    "https://www.qmul.ac.uk/",
]

# Set '__PRETEXT__' or '__POSTTEXT__' as a key with string value to add custom text. e.g. SLYTAGSPLIT = {'__POSTTEXT__':'some text}
SLYTAGSPLIT: Optional[Dict[str, Union[List[str], str]]] = {
    "closed splits": ["split closed train", "split closed val", "split closed test"],
    "random closed splits": [
        "split closed random train",
        "split closed random val",
        "split closed random test",
    ],
    "__POSTTEXT__": "Additionally, every image marked with its ***identity***, ***date*** tags. Labels marked with its ***orientation*** and ***occluded***. Explore it in Supervisely labelling tool",
}
TAGS: Optional[
    List[
        Literal[
            "multi-view",
            "synthetic",
            "simulation",
            "multi-camera",
            "multi-modal",
            "multi-object-tracking",
            "keypoints",
            "egocentric",
        ]
    ]
] = None


SECTION_EXPLORE_CUSTOM_DATASETS: Optional[List[str]] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "project_name_full": PROJECT_NAME_FULL or PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["blog"] = BLOGPOST
    settings["repository"] = REPOSITORY
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    settings["explore_datasets"] = SECTION_EXPLORE_CUSTOM_DATASETS

    return settings
