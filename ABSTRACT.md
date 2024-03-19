The authors present **Sea Turtle ID 2022 Dataset**, the inaugural public dataset comprising sea turtle photographs taken in their natural habitat. This extensive dataset consists of 8,729 images capturing 438 distinct individuals over a remarkable span of 13 years, marking it as the most extensive animal re-identification dataset to date. Each photograph comes with comprehensive annotations, including identity markers, encounter timestamps, and segmentation masks outlining different body parts.

## Motivation

Recognizing individual animals through image-based re-identification is crucial for various wildlife studies, including population monitoring, behavioral analysis, and wildlife management. With the expansion of photo databases spanning multiple years, there's a growing need for automated methods to streamline the labor-intensive process of individual animal identification. In response, numerous automatic re-identification methods have emerged in recent years. These methods are assessed using benchmark databases that cover various animal groups, such as mammals, reptiles, and smaller organisms. Typically, these databases are divided into a reference set, containing images with known individual identities, and a query set, containing images where identities need to be matched with the reference set. In deep learning, these sets are commonly referred to as training and test sets. The quality of these datasets significantly influences the evaluation of re-identification methods. Hence, it's crucial for the dataset and its division to mimic real-world scenarios. This entails ensuring that images in the query and reference sets originate from different encounters, such as burst mode in camera traps or consecutive video frames. Additionally, incorporating images with unknown identities, different locations, varied capture conditions, and images depicting changes in animal appearances over time are essential factors to consider.

<img src="https://github.com/dataset-ninja/sea-turtle-2022/assets/120389559/edab12a2-d340-4429-bd5f-3dfeda1a3d36" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">The long-span difference in visual appearance of one individual sea turtle. The shapes of the facial scales remain the same, but other features, e.g., coloration, pigmentation, shape, and scratches, change over time.</span>

During a single encounter, images typically share common characteristics as the encounter occurs within a short timeframe. To differentiate between various encounters and factors within a dataset effectively, including capture date and time in the metadata, known as timestamps, is crucial. Without timestamp information, datasets are often divided into reference and query sets purely at random. However, this random split can lead to issues, as images in the training and test sets may originate from the same encounter or observation, resulting in unintended data leakage between training and testing phases. This can potentially cause overfitting to the specific factors of a particular encounter rather than learning a generalized representation of each individual. Implicitly, a random split assumes encountering the same factors in the future, which is highly unrealistic. In contrast, utilizing timestamps allows for time-aware splits, where images from a specific time period are grouped together in either the reference or the query set. This approach reflects a more realistic scenario, where new factors may be encountered in future observations.

## Dataset description

The authors introduce a novel dataset with photographs of loggerhead sea turtles (Caretta caretta) – the SeaTurtleID2022. The dataset was collected over 13 years and consists of 8729 high-resolution photographs of 438 unique individuals. Each photograph includes various annotations, e.g., identities, encounter timestamps, and body parts segmentation masks. The SeaTurtleID2022 is the longest-spanned public wild animal image dataset and the only public dataset of sea turtles with photographs captured in the wild. In contrast to existing datasets, the SeaTurtleID2022 allows for two realistic and ecologically motivated splits instead of a ”random” split:

* **time-aware closed-set:** with reference images belonging to different encounters than query ones,
* **time-aware open-set:** with new unknown individuals (i.e., newly introduced to population) in test and validation sets (common in ecology).

While the primary purpose of the SeaTurtleID2022 dataset is animal re-identification, it also serves as a valuable resource for evaluating various fundamental computer vision tasks, including:

* Object detection
* Instance segmentation
* Fully and weakly supervised semantic segmentation
* 3D reconstruction
* Concept drift analysis

It's worth noting that SeaTurtleID2022 mitigates common limitations found in other human re-identification datasets. For instance, datasets focusing on human faces often suffer from low-resolution images, restricted pose variations, limited time spans, and privacy concerns arising from either artificial generation or web crawling for data collection.

## Location and species

All photographs in the dataset were captured in Laganas Bay, located on Zakynthos Island, Greece, at coordinates 37°43′N, 20°52′E, spanning from 2010 to 2022, during the months of May to October. Laganas Bay serves as a primary breeding ground for Mediterranean loggerhead sea turtles. Annually, approximately 300 female turtles undertake migratory journeys to the island for breeding purposes, returning every 2 to 3 years. However, some individuals establish residency on the island and can be observed in consecutive breeding seasons. Loggerhead sea turtles exhibit long lifespans, with some individuals retaining reproductive capability for over three decades, resulting in extensive image recordings spanning multiple years for certain individuals. Sea turtles are well-suited for photo-identification due to their distinctive scale patterns. Specifically, the polygonal scales present on the lateral (side) and dorsal (top) surfaces of their heads are unique to each individual and remain consistent throughout their lifetimes. It is noteworthy that the scale patterns on the left and right sides of a turtle's head differ, further enhancing their identification potential.

## Photographic procedure

All underwater photographs were captured during snorkeling surveys, taken from varying distances ranging from 7 meters to just a few centimeters. Three different cameras were employed throughout the survey periods:

1) From 2010 to 2013, a Canon IXUS 105 digital compact camera was utilized, housed within a Canon underwater housing.
2) In the years 2014 to 2017, a Canon 6D full-frame DSLR camera was employed, paired with a Sigma 15mm fisheye lens and encased in an Ikelite underwater housing.
3) From 2018 to 2022, the same Canon 6D camera setup was used, with the addition of an INON Z330 external flash.
The resolutions of the photographs varied, ranging from 4000×3000 pixels for the Canon IXUS camera to 5472×3648 pixels for the Canon 6D, with an average resolution of 5269×3564 pixels. The water depth during photography sessions fluctuated between 1 to 8 meters, with the majority of photographs taken at depths less than 5 meters.

Images captured from 2014 to 2022 generally exhibit higher quality due to the utilization of a more advanced camera setup and shorter camera-to-subject distances. However, the use of fisheye lenses may introduce barrel-shaped distortion, particularly noticeable in close-up shots. Additionally, the incorporation of an external flash resulted in more natural color reproduction in the images.

<img src="https://github.com/dataset-ninja/sea-turtle-2022/assets/120389559/101f3c5d-4a95-4fe9-9120-57dfe74c0190" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">Selected individual turtle (t023) from the SeaTurtleID2022 database, photographed with three different camera set-ups. Photographs taken with the DSLR camera are of higher quality, and the additional use of flash recovers the natural colouration of the animal.
All the photographs were cropped for illustration purposes.</span>

Containing 8729 photographs capturing 438 individual sea turtles, this dataset stands as the most comprehensive publicly available resource for sea turtle identification in their natural habitat. These images are presented in their original resolution and showcase a variety of backgrounds. Around 90% of the photographs boast dimensions of 5472×3648 pixels, with an average size of 5269×3564 pixels. On average, the dimensions dedicated to the turtle's head occupy approximately 635×554 pixels within each image.

<img src="https://github.com/dataset-ninja/sea-turtle-2022/assets/120389559/470d3cf2-9457-4ba0-b797-7b12c77e7b26" alt="image" width="600">

<span style="font-size: smaller; font-style: italic;">Number of photographs for each of the 438 turtles. The orange line corresponds to 10 photographs.</span>

The dataset contains photographs continuously captured over 13 years from 2010 to 2022. In contrast to most existing animal datasets that are usually collected in controlled environments and/or over a short time span.

<img src="https://github.com/dataset-ninja/sea-turtle-2022/assets/120389559/a4197583-ca90-404e-9808-c849409fa8ad" alt="image" width="600">

<span style="font-size: smaller; font-style: italic;">Time-related statistics within the SeaTurtleID2022 dataset: number of encounters per year (left), distribution of all individuals to the total number of observation years, i.e., recurrence of individuals (middle), and number of newly observed identities in each year (right).</span>

## Segmentation masks and bounding boxes

The dataset predominantly comprises photographs featuring visible *turtle* *head* and/or *flipper*. To facilitate detailed analysis and research, the authors have meticulously annotated these images with segmentation masks and bounding boxes for various body parts. In addition to the masks, they have included ***orientation*** details (such as left, right, top, top-right, top-left, front, or bottom) for each head mask, along with ***orientation*** (top or bottom) and location (front left/right or rear left/right) for *flipper* masks. These comprehensive annotations not only enable the enhancement and evaluation of turtle identification techniques but also pave the way for the development of innovative methods in object detection and semantic segmentation. The dataset includes multiple images from different angles and, therefore, provides a ground for the challenging task of 3D animal reconstruction.

<img src="https://github.com/dataset-ninja/sea-turtle-2022/assets/120389559/334afd09-aa87-408a-8973-0b21585d68be" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">Examples of body parts (head, carapace, flippers) segmentation masks.</span>

## Dataset splits and subsets

Traditionally, re-identification datasets are divided randomly into reference (training) and query (test) sets, a practice that can lead to unintended data leakage and artificially inflated performance metrics. Essentially, this means that images from the same observation may appear in both sets. To demonstrate this challenge, the authors present four images of a single turtle: two taken on the same day in 2011 and two on the same day in 2021. 

<img src="https://github.com/dataset-ninja/sea-turtle-2022/assets/120389559/31eeff4d-eb1d-42e2-ac0c-4b64f4ec6c00" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">Unwanted background similarities in photographs from same/similar locations or time of observations.</span>

Matching images from the same day is relatively straightforward due to consistent background and coloration. However, images from different days or years lack this similarity, making them considerably more difficult to match. To address this issue, the authors propose two ecologically motivated splits that leverage timestamps to prevent information leakage from the test set to the training set. These splits, referred to as time-aware splits, offer a more realistic representation of real-world scenarios. Additionally, the authors provide predefined training/validation/test splits for easier comparison in future research, although validation may not always be necessary.

The **time-aware closed-set** split closely resembles a standard closed-set re-identification scenario, wherein all identities present in the validation/test sets are also available for training. This scenario is particularly applicable to environments with well-controlled populations, such as zoos or wildlife reservations. In constructing this split, we organize the data based on the acquisition date and partition it in a time-aware manner. Approximately 80% of the days' worth of data are allocated to the development set (comprising both training and validation subsets), while the remaining days' data constitute the test set. For instances where an individual turtle was observed only once, it was retained for training purposes. Specifically, the authors provide 438 identities for training and 270 for testing. The development set was further subdivided into training and validation subsets using the same approach.

The **time-aware open-set** split is established based on predefined cutoff time points, which are specific years delineating different periods. In this setup, each subset (training/validation/test) encompasses all images captured within consecutive time intervals. Essentially, this split formulates an open-set problem, mirroring the inherent dynamics and growth of the natural population. During the construction process, the authors utilized data from the 2010–2018 period for training, the entirety of 2019 for validation, and the 2020–2022 period for the test set. The training set comprises 357 identities, while the test set consists of 151 identities, with 51 newly observed identities among them. A similar new-to-known identity ratio is naturally reflected in the validation set, where 38 out of 83 identities are newly encountered.

|              | Subset        | Closed-set | Open-set |
|--------------|---------------|------------|----------|
| **Training** | # of images   | 4679       | 5303     |
|              | # of identities | 438       | 357      |
| **Validation** | # of images | 1418       | 1118     |
|              | # of identities | 91        | 83       |
| **Test**     | # of images   | 2632       | 2308     |
|              | # of identities | 270       | 151      |

<span style="font-size: smaller; font-style: italic;">Provided time-aware datasets split and their statistics.</span>

**Note:** The open-set split is much closer to the real-world re-identification settings than the closed-set problem. Therefore, the open-set split should be preferred for automated method evaluation over all datasets. In case closed-set evaluation is desired, then the time-aware split must be the preferred option over the random split.

Additionally, the authors offer three subsets that encompass different body parts, including full-body, *flipper*, and *head*, by extracting crops from the original resolution. The quantity of data points varies for each body part due to the visibility of certain features. Utilizing the time-aware closed-set approach, they formulated part-based sets with the following number of training/test samples: 6139 / 2650 full *turtle* bodies, 14849 / 6237 *flipper*, and 5956 / 2583 *head*.
