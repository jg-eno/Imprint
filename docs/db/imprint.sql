-- MySQL dump 10.13  Distrib 8.0.39, for Linux (x86_64)
--
-- Host: localhost    Database: imprint
-- ------------------------------------------------------
-- Server version	8.0.39-0ubuntu0.24.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `CardTags`
--

DROP TABLE IF EXISTS `CardTags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CardTags` (
  `cardID` int NOT NULL,
  `tagID` int NOT NULL,
  PRIMARY KEY (`cardID`,`tagID`),
  KEY `tagID` (`tagID`),
  CONSTRAINT `CardTags_ibfk_1` FOREIGN KEY (`cardID`) REFERENCES `Cards` (`cardID`),
  CONSTRAINT `CardTags_ibfk_2` FOREIGN KEY (`tagID`) REFERENCES `Tags` (`TagId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CardTags`
--

LOCK TABLES `CardTags` WRITE;
/*!40000 ALTER TABLE `CardTags` DISABLE KEYS */;
/*!40000 ALTER TABLE `CardTags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Cards`
--

DROP TABLE IF EXISTS `Cards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Cards` (
  `cardID` int NOT NULL AUTO_INCREMENT,
  `deckID` int DEFAULT NULL,
  `cardFront` text,
  `cardBack` text,
  `cardType` varchar(255) DEFAULT NULL,
  `intervalLength` int DEFAULT NULL,
  `repetitions` int DEFAULT NULL,
  `dateAdded` date DEFAULT NULL,
  `dateModified` date DEFAULT NULL,
  `previousReviewDate` date DEFAULT NUll,
  `cardEase` float DEFAULT NULL,
  `totalReviewCount` text,
  `isActive` boolean DEFAULT 0,
  `isNew` boolean DEFAULT 0,
  PRIMARY KEY (`cardID`),
  KEY `deckID` (`deckID`),
  CONSTRAINT `Cards_ibfk_1` FOREIGN KEY (`deckID`) REFERENCES `Decks` (`DeckId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cards`
--

LOCK TABLES `Cards` WRITE;
/*!40000 ALTER TABLE `Cards` DISABLE KEYS */;
/*!40000 ALTER TABLE `Cards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Decks`
--

DROP TABLE IF EXISTS `Decks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Decks` (
  `DeckId` int NOT NULL AUTO_INCREMENT,
  `UserId` int DEFAULT NULL,
  `deckName` varchar(255) DEFAULT NULL,
  `freqRate` float DEFAULT NULL,
  `heatMapString` text,
  `newCardsPerDay` int DEFAULT NULL,
  PRIMARY KEY (`DeckId`),
  KEY `UserId` (`UserId`),
  CONSTRAINT `Decks_ibfk_1` FOREIGN KEY (`UserId`) REFERENCES `Users` (`UserId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Decks`
--

LOCK TABLES `Decks` WRITE;
/*!40000 ALTER TABLE `Decks` DISABLE KEYS */;
/*!40000 ALTER TABLE `Decks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Tags`
--

DROP TABLE IF EXISTS `Tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Tags` (
  `TagId` int NOT NULL AUTO_INCREMENT,
  `tagName` varchar(255) DEFAULT NULL,
  `noOfCards` int DEFAULT NULL,
  `dateCreated` date DEFAULT NULL,
  PRIMARY KEY (`TagId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tags`
--

LOCK TABLES `Tags` WRITE;
/*!40000 ALTER TABLE `Tags` DISABLE KEYS */;
/*!40000 ALTER TABLE `Tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `UserStats`
--

DROP TABLE IF EXISTS `UserStats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `UserStats` (
  `userStatId` int NOT NULL AUTO_INCREMENT,
  `userId` int DEFAULT NULL,
  `learningPace` float DEFAULT NULL,
  `reviewFrequency` float DEFAULT NULL,
  `defaultNewCardRate` float DEFAULT NULL,
  `defaultReviewRate` float DEFAULT NULL,
  `deckList` text,
  `deckCount` int DEFAULT NULL,
  `heatMapString` text,
  PRIMARY KEY (`userStatId`),
  KEY `userId` (`userId`),
  CONSTRAINT `UserStats_ibfk_1` FOREIGN KEY (`userId`) REFERENCES `Users` (`UserId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UserStats`
--

LOCK TABLES `UserStats` WRITE;
/*!40000 ALTER TABLE `UserStats` DISABLE KEYS */;
/*!40000 ALTER TABLE `UserStats` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Users` (
  `UserId` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `timeOfEntry` datetime DEFAULT NULL,
  `authKey` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`UserId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-19  0:31:27
