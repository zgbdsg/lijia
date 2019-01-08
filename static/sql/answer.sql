/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50721
Source Host           : localhost:3306
Source Database       : todo

Target Server Type    : MYSQL
Target Server Version : 50721
File Encoding         : 65001

Date: 2018-03-09 22:51:04
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for question
-- ----------------------------
DROP TABLE IF EXISTS `answer`;
CREATE TABLE `answer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL,
  `vid` int(11) NOT NULL,
  `btnId` int(11) NOT NULL,
  `a2Q1` varchar(255) DEFAULT NULL,
  `a2Q2` varchar(255) DEFAULT NULL,
  `a2Q3` varchar(255) DEFAULT NULL,
  `a2Q4` varchar(255) DEFAULT NULL,
  `a2Q5` varchar(255) DEFAULT NULL,
  `a2Q6` varchar(255) DEFAULT NULL,
  `a2Q7` varchar(255) DEFAULT NULL,
  `a2Q8` varchar(255) DEFAULT NULL,
  `a2Q9` varchar(255) DEFAULT NULL,
  `a2Q10` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
