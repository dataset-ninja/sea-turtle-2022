import csv
import os
import shutil
from collections import defaultdict

import numpy as np
import pycocotools.mask as mask_util
import supervisely as sly
from dataset_tools.convert import unpack_if_archive
from supervisely.io.fs import (
    file_exists,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
)
from supervisely.io.json import load_json_file
from tqdm import tqdm

import src.settings as s


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # Possible structure for bbox case. Feel free to modify as you needs.

    images_path = "/home/alex/DATASETS/TODO/archive/turtles-data/data"
    batch_size = 30
    ann_json_path = "/home/alex/DATASETS/TODO/archive/turtles-data/data/annotations.json"
    split_csv_path = "/home/alex/DATASETS/TODO/archive/turtles-data/data/metadata_splits.csv"

    def convert_rle_mask_to_polygon(rle_mask_data):
        if type(rle_mask_data["counts"]) is str:
            rle_mask_data["counts"] = bytes(rle_mask_data["counts"], encoding="utf-8")
            mask = mask_util.decode(rle_mask_data)
        else:
            rle_obj = mask_util.frPyObjects(
                rle_mask_data,
                rle_mask_data["size"][0],
                rle_mask_data["size"][1],
            )
            mask = mask_util.decode(rle_obj)
        mask = np.array(mask, dtype=bool)
        return sly.Bitmap(mask).to_contours()

    def create_ann(image_path):
        labels = []
        tags = []

        image_name = get_file_name_with_ext(image_path)
        img_height = image_name_to_shape[image_name][0]
        img_wight = image_name_to_shape[image_name][1]

        identity_value = image_path.split("/")[-2]
        identity = sly.Tag(identity_meta, value=identity_value)
        tags.append(identity)

        date_value = im_name_to_date[image_name]
        date = sly.Tag(date_meta, value=date_value)
        tags.append(date)

        splits = im_name_to_splits[image_name]
        split_close = sly.Tag(val_to_meta[splits[0]])
        tags.append(split_close)

        split_close_random = sly.Tag(val_to_meta_random[splits[1]])
        tags.append(split_close_random)

        ann_data = image_name_to_ann_data[get_file_name_with_ext(image_path)]
        ann_data = list(reversed(ann_data))
        for curr_ann_data in ann_data:
            l_tags = []
            category_id = curr_ann_data[0]
            obj_class = idx_to_obj_class[category_id]

            orient_value = curr_ann_data[3].get("orientation")
            if orient_value is not None:
                orientation = sly.Tag(orientation_meta, value=orient_value)
                l_tags.append(orientation)

            if curr_ann_data[3].get("occluded"):
                occluded = sly.Tag(occluded_meta)
                l_tags.append(occluded)

            rle_mask_data = curr_ann_data[1]
            polygons = convert_rle_mask_to_polygon(rle_mask_data)
            for polygon in polygons:
                label = sly.Label(polygon, obj_class, tags=l_tags)
                labels.append(label)

            bbox_coord = curr_ann_data[2]
            rectangle = sly.Rectangle(
                top=int(bbox_coord[1]),
                left=int(bbox_coord[0]),
                bottom=int(bbox_coord[1] + bbox_coord[3]),
                right=int(bbox_coord[0] + bbox_coord[2]),
            )
            label_rectangle = sly.Label(rectangle, obj_class, tags=l_tags)
            labels.append(label_rectangle)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels, img_tags=tags)

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)

    identity_meta = sly.TagMeta("identity", sly.TagValueType.ANY_STRING)
    date_meta = sly.TagMeta("date", sly.TagValueType.ANY_STRING)
    orientation_meta = sly.TagMeta("orientation", sly.TagValueType.ANY_STRING)
    occluded_meta = sly.TagMeta("occluded", sly.TagValueType.NONE)

    splt_closed_test = sly.TagMeta("splt closed test", sly.TagValueType.NONE)
    splt_closed_val = sly.TagMeta("splt closed val", sly.TagValueType.NONE)
    splt_closed_train = sly.TagMeta("splt closed train", sly.TagValueType.NONE)

    val_to_meta = {"train": splt_closed_train, "valid": splt_closed_val, "test": splt_closed_test}

    splt_closed_test_random = sly.TagMeta("splt closed random test", sly.TagValueType.NONE)
    splt_closed_val_random = sly.TagMeta("splt closed random val", sly.TagValueType.NONE)
    splt_closed_train_random = sly.TagMeta("splt closed random train", sly.TagValueType.NONE)

    val_to_meta_random = {
        "train": splt_closed_train_random,
        "valid": splt_closed_val_random,
        "test": splt_closed_test_random,
    }

    meta = sly.ProjectMeta(
        tag_metas=[
            identity_meta,
            date_meta,
            occluded_meta,
            orientation_meta,
            splt_closed_test,
            splt_closed_val,
            splt_closed_train,
            splt_closed_test_random,
            splt_closed_val_random,
            splt_closed_train_random,
        ]
    )

    ann = load_json_file(ann_json_path)

    idx_to_obj_class = {}
    image_id_to_name = {}
    image_name_to_ann_data = defaultdict(list)
    image_name_to_shape = {}

    for curr_category in ann["categories"]:
        if idx_to_obj_class.get(curr_category["id"]) is None:
            obj_class = sly.ObjClass(curr_category["name"], sly.AnyGeometry)
            meta = meta.add_obj_class(obj_class)
            idx_to_obj_class[curr_category["id"]] = obj_class
    api.project.update_meta(project.id, meta.to_json())

    for curr_image_info in ann["images"]:
        image_id_to_name[curr_image_info["id"]] = curr_image_info["file_name"].split("/")[-1]
        image_name_to_shape[curr_image_info["file_name"].split("/")[-1]] = (
            curr_image_info["height"],
            curr_image_info["width"],
        )

    for curr_ann_data in ann["annotations"]:
        image_id = curr_ann_data["image_id"]
        image_name_to_ann_data[image_id_to_name[image_id]].append(
            [
                curr_ann_data["category_id"],
                curr_ann_data["segmentation"],
                curr_ann_data["bbox"],
                curr_ann_data["attributes"],
            ]
        )

    split_to_images = {"train": [], "valid": [], "test": []}
    im_name_to_date = {}
    im_name_to_splits = {}
    with open(split_csv_path, "r") as file:
        csvreader = csv.reader(file)
        for idx, row in enumerate(csvreader):
            if idx > 0:
                split_to_images[row[-1]].append(row[3])
                im_name_to_date[row[3].split("/")[-1]] = row[6]
                im_name_to_splits[row[3].split("/")[-1]] = (row[-3], row[-2])

    for ds_name, data_pathes in split_to_images.items():
        if ds_name == "valid":
            ds_name = "val"

        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

        images_pathes = []

        for im_data in data_pathes:
            images_pathes.append(os.path.join(images_path, im_data))

        progress = sly.Progress("Create dataset {}".format(ds_name), len(images_pathes))

        for img_pathes_batch in sly.batched(images_pathes, batch_size=batch_size):
            images_names_batch = [
                get_file_name_with_ext(image_path) for image_path in img_pathes_batch
            ]

            img_infos = api.image.upload_paths(dataset.id, images_names_batch, img_pathes_batch)
            img_ids = [im_info.id for im_info in img_infos]

            anns_batch = [create_ann(image_path) for image_path in img_pathes_batch]
            api.annotation.upload_anns(img_ids, anns_batch)

            progress.iters_done_report(len(img_pathes_batch))

    return project
