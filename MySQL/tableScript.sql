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
drop table if exists favourite;
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
  `college_id` VARCHAR(3) NOT NULL,
  `ID` VARCHAR(3) NOT NULL,
  `name` VARCHAR(45) NULL,
  `type` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`college_id`, `ID`, `type`),
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
  `idCandidate` VARCHAR(20) NOT NULL,
  `Candidate_name` VARCHAR(45) NULL,
  `gender` VARCHAR(45) NULL,
  `minzu` VARCHAR(45) NULL,
  `status` VARCHAR(20) NULL,
  `CollegeID` VARCHAR(3) NOT NULL,
  `CollegeName` VARCHAR(45) NULL,
  `zf1` INT NULL,
  `addScore` VARCHAR(45) NULL,
  `tot_score` INT NULL,
  `AdmissionLevel` VARCHAR(45) NULL,
  `zhuanye_ID` VARCHAR(3) NOT NULL,
  `AdmitType` VARCHAR(45) NULL,
  `AdmitTime` DATETIME NULL,
  `Chinese` INT NULL,
  `Math` INT NULL,
  `CLiberal` INT NULL,
  `CScience` INT NULL,
  `ForeignLanguage` INT NULL,
  `FLListen` INT NULL,
  `FLSpeaking` INT NULL,
  `type` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCandidate`),
  INDEX `fk_Candidate_zhuanye1_idx` (`CollegeID` ASC, `zhuanye_ID` ASC, `type` ASC),
  CONSTRAINT `fk_Candidate_zhuanye1`
    FOREIGN KEY (`CollegeID` , `zhuanye_ID` , `type`)
    REFERENCES `test`.`zhuanye` (`college_id` , `ID` , `type`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `test`.`rankSci`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`rankSci` (
  `score` INT NOT NULL,
  `rank` INT NOT NULL,
  PRIMARY KEY (`score`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


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
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `test`.`favourite`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`favourite` (
  `college_id` VARCHAR(3) NOT NULL,
  `name` VARCHAR(45) NULL,
  `highestScore` INT NULL,
  `lowestScore` INT NULL,
  `type` VARCHAR(45) NOT NULL,
  `Account_username` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`college_id`, `Account_username`, `type`),
  INDEX `fk_favourite_Account1_idx` (`Account_username` ASC),
  CONSTRAINT `fk_favourite_Account1`
    FOREIGN KEY (`Account_username`)
    REFERENCES `test`.`Account` (`username`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
