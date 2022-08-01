CREATE DATABASE python_flask;
use python_flask;

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `user_name` varchar(150) DEFAULT NULL,
  `password` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `users` ADD PRIMARY KEY (`id`);

INSERT INTO `users` (`id`, `user_name`, `password`) VALUES (1, 'username', 'password');

