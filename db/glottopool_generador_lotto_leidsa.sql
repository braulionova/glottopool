CREATE DATABASE  IF NOT EXISTS `glottopool` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */;
USE `glottopool`;
-- MySQL dump 10.13  Distrib 8.0.12, for Win64 (x86_64)
--
-- Host: localhost    Database: glottopool
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `generador_lotto_leidsa`
--

DROP TABLE IF EXISTS `generador_lotto_leidsa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
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
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `generador_lotto_leidsa`
--

LOCK TABLES `generador_lotto_leidsa` WRITE;
/*!40000 ALTER TABLE `generador_lotto_leidsa` DISABLE KEYS */;
INSERT INTO `generador_lotto_leidsa` VALUES (1,'2020-03-24','02','03','04','05','06','07','01','09','RD$ 304 MM',0),(2,'2020-03-26','1','3','5','7','9','11','2','4','RD$ 305 MM (RD$21 MM + RD$ 84 MM + RD$ 200 MM)',0),(3,'2020-03-26','12','3','5','7','9','11','2','4','RD$ 305 MM (RD$21 MM + RD$ 84 MM + RD$ 200 MM)',0),(4,'2020-03-26','13','3','5','7','9','11','2','4','RD$ 305 MM (RD$21 MM + RD$ 84 MM + RD$ 200 MM)',0),(5,'2020-03-26','14','3','5','7','9','11','2','4','RD$ 305 MM (RD$21 MM + RD$ 84 MM + RD$ 200 MM)',0),(6,'2020-03-26','1','3','5','7','9','11','2','4','RD$ 305 MM (RD$21 MM + RD$ 84 MM + RD$ 200 MM)',0),(7,'2020-03-26','12','3','5','7','9','11','2','4','RD$ 305 MM (RD$21 MM + RD$ 84 MM + RD$ 200 MM)',0),(8,'2020-03-26','13','3','5','7','9','11','2','4','RD$ 305 MM (RD$21 MM + RD$ 84 MM + RD$ 200 MM)',0),(9,'2020-03-26','14','3','5','7','9','11','2','4','RD$ 305 MM (RD$21 MM + RD$ 84 MM + RD$ 200 MM)',0),(10,'2020-03-26','1','3','5','7','9','11','2','4','RD$ 305 MM (RD$21 MM + RD$ 84 MM + RD$ 200 MM)',0),(11,'2020-03-26','12','3','5','7','9','11','2','4','RD$ 305 MM (RD$21 MM + RD$ 84 MM + RD$ 200 MM)',0),(12,'2020-03-26','13','3','5','7','9','11','2','4','RD$ 305 MM (RD$21 MM + RD$ 84 MM + RD$ 200 MM)',0),(13,'2020-03-26','14','3','5','7','9','11','2','4','RD$ 305 MM (RD$21 MM + RD$ 84 MM + RD$ 200 MM)',0);
/*!40000 ALTER TABLE `generador_lotto_leidsa` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-26 14:03:44
