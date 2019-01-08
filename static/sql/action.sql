CREATE TABLE `action` (
  `id` int(11) NOT NULL auto_increment,
  `uid` int(11) NOT NULL,
  `vid` int(11) NOT NULL,
  `bid` int(11) NOT NULL,
  `timestamp` varchar(30) NOT NULL,
  `action` varchar(200) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

