CREATE TABLE `score` (
  `id` int(11) NOT NULL auto_increment,
  `uid` int(11) NOT NULL,
  `vid` int(11) NOT NULL,
  `timestamp` varchar(30) NOT NULL,
  `value` varchar(30) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

