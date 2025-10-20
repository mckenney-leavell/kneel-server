CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` TEXT(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` TEXT(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carats` NUMERIC(3,2) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Orders`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal_id` INTEGER NOT NULL,
    `style_id` INTEGER NOT NULL,
    `size_id` INTEGER NOT NULL,
    FOREIGN KEY(`metal_id`) REFERENCES `Metals`(`id`),
    FOREIGN KEY(`style_id`) REFERENCES `Styles`(`id`),
    FOREIGN KEY(`size_id`) REFERENCES `Sizes`(`id`)
);

INSERT INTO `Metals` VALUES (null, "Sterling Silver", 12.42);
INSERT INTO `Metals` VALUES (null, "14K Gold", 736.4);
INSERT INTO `Metals` VALUES (null, "24K Gold", 1235);

INSERT INTO `Styles` VALUES (null, "Classic", 500);
INSERT INTO `Styles` VALUES (null, "Modern", 710);
INSERT INTO `Styles` VALUES (null, "Vintage", 965);

INSERT INTO `Sizes` VALUES (null, ".5", 405);
INSERT INTO `Sizes` VALUES (null, ".75", 782);
INSERT INTO `Sizes` VALUES (null, "1", 1470);

INSERT INTO `Orders` VALUES (null, 2, 1, 3);
INSERT INTO `Orders` VALUES (null, 1, 2, 1);
INSERT INTO `Orders` VALUES (null, 3, 3, 2);

DELETE FROM `Metals` WHERE `id` = 4;
DELETE FROM `Metals` WHERE `id` = 5;
DELETE FROM `Metals` WHERE `id` = 6;

DELETE FROM `Sizes` WHERE `id` = 4;
DELETE FROM `Sizes` WHERE `id` = 5;
DELETE FROM `Sizes` WHERE `id` = 6;

DELETE FROM `Styles` WHERE `id` = 4;
DELETE FROM `Styles` WHERE `id` = 5;
DELETE FROM `Styles` WHERE `id` = 6;
