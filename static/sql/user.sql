CREATE TABLE `user` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(30) NOT NULL,
  `pwd` varchar(30) NOT NULL,
  `admin` varchar(10) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

INSERT INTO `user` VALUES ('1','admin', 'admin', '1');
INSERT INTO `user` VALUES ('2','user', 'user', '0');