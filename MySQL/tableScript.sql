-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema test
-- -----------------------------------------------------

DROP TABLE if exists college;
DROP TABLE if exists zhuanye;
DROP TABLE if exists Account;
DROP TABLE if exists Candidate;
DROP TABLE if exists InvitedList;
DROP TABLE if exists rankArt;
DROP TABLE if exists rankSci;

-- -----------------------------------------------------
-- Schema test
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `test` DEFAULT CHARACTER SET utf8 ;
USE `test` ;

-- -----------------------------------------------------
-- Table `test`.`college`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`college` (
  `idcollege` VARCHAR(3) NOT NULL,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`idcollege`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `test`.`zhuanye`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`zhuanye` (
  `ID` VARCHAR(3) NOT NULL,
  `name` VARCHAR(45) NULL,
  `college_id` VARCHAR(3) NOT NULL,
  `rank` INT NULL,
  `type` VARCHAR(45) NULL DEFAULT 'wen  or li',
  PRIMARY KEY (`ID`, `college_id`),
  INDEX `fk_zhuanye_college1_idx` (`college_id` ASC),
  CONSTRAINT `fk_zhuanye_college1`
    FOREIGN KEY (`college_id`)
    REFERENCES `test`.`college` (`idcollege`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `test`.`Candidate`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`Candidate` (
  `idCandidate` INT NOT NULL,
  `Candidate_name` VARCHAR(45) NULL,
  `gender` VARCHAR(45) NULL,
  `minzu` VARCHAR(45) NULL,
  `status` TINYINT(1) NULL,
  `addScore` VARCHAR(45) NULL,
  `tot_score` INT(11) NULL,
  `CollegeID` VARCHAR(3) NOT NULL,
  `CollegeName` VARCHAR(45) NULL,
  `AdmissionLevel` VARCHAR(45) NULL,
  `zhuanye_ID` VARCHAR(3) NOT NULL,
  `AdmitType` VARCHAR(45) NULL,
  `AdmitTime` DATE NULL,
  `Chinese` INT NULL,
  `Math` INT NULL,
  `CLiberal` INT NULL,
  `CScience` INT NULL,
  `ForeignLanguage` INT NULL,
  `FLListen` INT NULL,
  `FLSpeaking` INT NULL,
  `z1` INT NULL,
  `zf` INT NULL,
  PRIMARY KEY (`idCandidate`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

alter table college convert to character set utf8;
alter table zhuanye convert to character set utf8;

alter table `Candidate` add constraint `Candidate_fk1` foreign key(`zhuanye_ID`,`CollegeID`) REFERENCES `zhuanye`(`ID`,`college_id`);
alter table `Candidate` add constraint `Candidate_fk2` foreign key(`CollegeName`) REFERENCES `college`(`idcollege`);

-- -----------------------------------------------------
-- Table `test`.`rankSci`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`rankSci` (
  `score` INT NOT NULL,
  `rank` INT NOT NULL,
  PRIMARY KEY (`score`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `test`.`InvitedList`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`InvitedList` (
  `key` VARCHAR(15) NOT NULL,
  `number` INT NULL,
  PRIMARY KEY (`key`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `test`.`Account`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`Account` (
  `username` VARCHAR(45) NOT NULL,
  `pwd` VARCHAR(45) NOT NULL,
  `InvitedList_key` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`username`),
  INDEX `fk_Account_InvitedList1_idx` (`InvitedList_key` ASC),
  CONSTRAINT `fk_Account_InvitedList1`
    FOREIGN KEY (`InvitedList_key`)
    REFERENCES `test`.`InvitedList` (`key`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `test`.`rankArt`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`rankArt` (
  `score` INT NOT NULL,
  `rank` INT NOT NULL,
  PRIMARY KEY (`score`))
ENGINE = InnoDB;

USE `test` ;

-- -----------------------------------------------------
-- Placeholder table for view `test`.`zhuanyeList`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`zhuanyeList` (`ID` INT, `name` INT, `college_id` INT, `rank` INT, `type` INT);

-- -----------------------------------------------------
-- Placeholder table for view `test`.`CollegeList_NameOrder`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`CollegeList_NameOrder` (`idcollege` INT, `name` INT);

-- -----------------------------------------------------
-- Placeholder table for view `test`.`CollegeList_IDOrder`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`CollegeList_IDOrder` (`id` INT);

-- -----------------------------------------------------
-- View `test`.`zhuanyeList`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `test`.`zhuanyeList`;
USE `test`;
CREATE  OR REPLACE VIEW `zhuanyeList` AS 
SELECT t.* from zhuanye AS t
GROUP BY college_id;

-- -----------------------------------------------------
-- View `test`.`CollegeList_NameOrder`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `test`.`CollegeList_NameOrder`;
USE `test`;
CREATE  OR REPLACE VIEW `CollegeList_NameOrder` AS
select * 
from college
order by name;

-- -----------------------------------------------------
-- View `test`.`CollegeList_IDOrder`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `test`.`CollegeList_IDOrder`;
USE `test`;
CREATE  OR REPLACE VIEW `CollegeList_IDOrder` AS
select * FROM college
order by idcollege;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
