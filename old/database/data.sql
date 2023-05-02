-- phpMyAdmin SQL Dump
-- version 4.0.10deb1ubuntu0.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 02, 2023 at 12:06 AM
-- Server version: 5.6.33-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `is437`
--

-- --------------------------------------------------------

--
-- Table structure for table `jakirab_sofia_treenode`
--

CREATE TABLE IF NOT EXISTS `jakirab_sofia_treenode` (
  `NodeID` int(11) NOT NULL AUTO_INCREMENT,
  `ParentNodeID` int(11) DEFAULT NULL,
  `NodeLabel` varchar(255) NOT NULL,
  `NodeData` text,
  `NodeLevel` int(11) NOT NULL,
  PRIMARY KEY (`NodeID`),
  KEY `ParentNodeID` (`ParentNodeID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=275 ;

--
-- Dumping data for table `jakirab_sofia_treenode`
--

INSERT INTO `jakirab_sofia_treenode` (`NodeID`, `ParentNodeID`, `NodeLabel`, `NodeData`, `NodeLevel`) VALUES
(1, NULL, 'Mystery', 'How many witches are there in the world?', 2),
(2, 1, 'Horror', 'The cat killed her', 0),
(4, 1, 'Fairytale', 'Cinderella is that you?', 3),
(5, 2, 'Fiction', 'cats', 3),
(6, 1, 'Romance', 'The lady and the tramp', 3),
(20, 2, 'Non-fiction', 'dogs', 3),
(21, NULL, '', '', 1),
(22, NULL, 'asfsasf', 'afsafs', 1),
(23, NULL, 'fafafs', 'asfasf', 1),
(24, NULL, 'hherhe', 'erherh', 1),
(25, NULL, 'book1', 'first test of addtreenode route', 3),
(29, 2, 'Comedy', 'Jack and Jill went to town', 2),
(30, 2, 'Scary', 'Jack attacked', 4),
(31, 2, 'Funny', 'Jackie', 3),
(32, NULL, 'Mystery', 'How many witches are there in the world?', 2),
(40, 2, 'hello', 'friend', 1),
(133, 5, '1', '1', 1),
(134, 5, '1212', '4124', 1),
(140, 4, 'soup', 'what', 1),
(141, 4, 'ee', 'ee', 1),
(142, 2, 'lemonade', 'is not a good idea', 1),
(146, 5, '22', '22', 1),
(147, 29, 'r', 'r', 1),
(150, 20, '2', '2', 1),
(151, 4, '1', '1', 1),
(159, 5, '2', '2', 1),
(160, 5, 'soup', 'is cool', 1),
(180, 5, '1', '1', 1),
(183, NULL, '1', '122', 1),
(192, NULL, '33', '3', 1),
(193, NULL, '5', '33', 1),
(194, NULL, '4', '4', 1),
(195, NULL, '1', '1', 1),
(196, NULL, '1', '1', 1),
(197, NULL, '444', '444', 1),
(239, NULL, 'r', 'r', 1),
(251, 6, 'f', 'f', 1),
(255, 2, 'the universe is', 'data', 1),
(259, 1, '44', '44', 1),
(260, 1, '1', '1', 1),
(261, 5, 'beep', 'ttt', 1);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `jakirab_sofia_treenode`
--
ALTER TABLE `jakirab_sofia_treenode`
  ADD CONSTRAINT `jakirab_sofia_treenode_ibfk_1` FOREIGN KEY (`ParentNodeID`) REFERENCES `jakirab_sofia_treenode` (`NodeID`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;