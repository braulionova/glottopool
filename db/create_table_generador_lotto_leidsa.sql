CREATE TABLE `generador_lotto_leidsa` (
  `id_generador_lotto_leidsa` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date DEFAULT NULL,
  `comb1` varchar(5) DEFAULT NULL,
  `comb2` varchar(5) DEFAULT NULL,
  `comb3` varchar(5) DEFAULT NULL,
  `comb4` varchar(5) DEFAULT NULL,
  `comb5` varchar(5) DEFAULT NULL,
  `comb6` varchar(5) DEFAULT NULL,
  `extra1` varchar(5) DEFAULT NULL,
  `extra2` varchar(5) DEFAULT NULL,
  `jackpotcomp` varchar(200) DEFAULT NULL,
  `activo` tinyint(4) DEFAULT '0',
  PRIMARY KEY (`id_generador_lotto_leidsa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
