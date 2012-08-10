-- MySQL dump 10.13  Distrib 5.1.63, for unknown-linux-gnu (x86_64)
--
-- Host: localhost    Database: conicefv_sif
-- ------------------------------------------------------
-- Server version	5.1.63-community-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'conicefv');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_bda51c3c` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM AUTO_INCREMENT=91 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (87,1,87),(86,1,86),(85,1,85),(84,1,84),(83,1,83),(82,1,82),(81,1,51),(80,1,50),(79,1,49),(78,1,48),(77,1,47),(76,1,46),(75,1,39),(74,1,38),(73,1,37),(72,1,36),(71,1,35),(70,1,34),(69,1,33),(68,1,32),(67,1,31),(88,1,91),(89,1,92),(90,1,93);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_e4470c6e` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=94 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add site',6,'add_site'),(17,'Can change site',6,'change_site'),(18,'Can delete site',6,'delete_site'),(19,'Can add log entry',7,'add_logentry'),(20,'Can change log entry',7,'change_logentry'),(21,'Can delete log entry',7,'delete_logentry'),(22,'Can add migration history',8,'add_migrationhistory'),(23,'Can change migration history',8,'change_migrationhistory'),(24,'Can delete migration history',8,'delete_migrationhistory'),(25,'Can add departamento',9,'add_departamento'),(26,'Can change departamento',9,'change_departamento'),(27,'Can delete departamento',9,'delete_departamento'),(28,'Can add municipio',10,'add_municipio'),(29,'Can change municipio',10,'change_municipio'),(30,'Can delete municipio',10,'delete_municipio'),(31,'Can add comunidad',11,'add_comunidad'),(32,'Can change comunidad',11,'change_comunidad'),(33,'Can delete comunidad',11,'delete_comunidad'),(34,'Can add encuestador',12,'add_encuestador'),(35,'Can change encuestador',12,'change_encuestador'),(36,'Can delete encuestador',12,'delete_encuestador'),(37,'Can add empresa',13,'add_empresa'),(38,'Can change empresa',13,'change_empresa'),(39,'Can delete empresa',13,'delete_empresa'),(40,'Can add tipo propiedad bosque',14,'add_tipopropiedadbosque'),(41,'Can change tipo propiedad bosque',14,'change_tipopropiedadbosque'),(42,'Can delete tipo propiedad bosque',14,'delete_tipopropiedadbosque'),(43,'Can add organizado',15,'add_organizado'),(44,'Can change organizado',15,'change_organizado'),(45,'Can delete organizado',15,'delete_organizado'),(46,'Can add organizacion',16,'add_organizacion'),(47,'Can change organizacion',16,'change_organizacion'),(48,'Can delete organizacion',16,'delete_organizacion'),(49,'Can add gobierno gti',17,'add_gobiernogti'),(50,'Can change gobierno gti',17,'change_gobiernogti'),(51,'Can delete gobierno gti',17,'delete_gobiernogti'),(52,'Can add especies naturales',18,'add_especiesnaturales'),(53,'Can change especies naturales',18,'change_especiesnaturales'),(54,'Can delete especies naturales',18,'delete_especiesnaturales'),(55,'Can add especies introducidas',19,'add_especiesintroducidas'),(56,'Can change especies introducidas',19,'change_especiesintroducidas'),(57,'Can delete especies introducidas',19,'delete_especiesintroducidas'),(58,'Can add madera',20,'add_madera'),(59,'Can change madera',20,'change_madera'),(60,'Can delete madera',20,'delete_madera'),(61,'Can add tipo producto',21,'add_tipoproducto'),(62,'Can change tipo producto',21,'change_tipoproducto'),(63,'Can delete tipo producto',21,'delete_tipoproducto'),(64,'Can add proceso industrial bosque',22,'add_procesoindustrialbosque'),(65,'Can change proceso industrial bosque',22,'change_procesoindustrialbosque'),(66,'Can delete proceso industrial bosque',22,'delete_procesoindustrialbosque'),(67,'Can add tipo secados',23,'add_tiposecados'),(68,'Can change tipo secados',23,'change_tiposecados'),(69,'Can delete tipo secados',23,'delete_tiposecados'),(70,'Can add buenas practicas',24,'add_buenaspracticas'),(71,'Can change buenas practicas',24,'change_buenaspracticas'),(72,'Can delete buenas practicas',24,'delete_buenaspracticas'),(73,'Can add proveedores suministros',25,'add_proveedoressuministros'),(74,'Can change proveedores suministros',25,'change_proveedoressuministros'),(75,'Can delete proveedores suministros',25,'delete_proveedoressuministros'),(76,'Can add tipo bosque umf',26,'add_tipobosqueumf'),(77,'Can change tipo bosque umf',26,'change_tipobosqueumf'),(78,'Can delete tipo bosque umf',26,'delete_tipobosqueumf'),(79,'Can add metodo extraccion',27,'add_metodoextraccion'),(80,'Can change metodo extraccion',27,'change_metodoextraccion'),(81,'Can delete metodo extraccion',27,'delete_metodoextraccion'),(82,'Can add propietario bosques',28,'add_propietariobosques'),(83,'Can change propietario bosques',28,'change_propietariobosques'),(84,'Can delete propietario bosques',28,'delete_propietariobosques'),(85,'Can add seguimiento',29,'add_seguimiento'),(86,'Can change seguimiento',29,'change_seguimiento'),(87,'Can delete seguimiento',29,'delete_seguimiento'),(88,'Can add tipo certificacion',30,'add_tipocertificacion'),(89,'Can change tipo certificacion',30,'change_tipocertificacion'),(90,'Can delete tipo certificacion',30,'delete_tipocertificacion'),(91,'Can add datos',31,'add_datos'),(92,'Can change datos',31,'change_datos'),(93,'Can delete datos',31,'delete_datos');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'crocha','','','carlos@simas.org.ni','pbkdf2_sha256$10000$zIUk5kwVy5PD$vz0gMgvMRrLuG5zkDMjwsi1og3h3enwkHM3G16tnCAE=',1,1,1,'2012-08-10 21:18:15','2012-07-13 19:24:48'),(2,'conicefv','','','','pbkdf2_sha256$10000$TuKSlxearpFJ$HPSvCd6jnrKVWmQMNr+KavGZILPEPlbIToSbJ344a3Y=',1,1,0,'2012-07-30 16:39:35','2012-07-13 20:21:28'),(3,'test','','','','pbkdf2_sha256$10000$QQzlcaP8mE1f$gLHpYrQ2SRCIfHlmntX6C6VC5uRCNHs6xbMto7DlLvk=',0,1,0,'2012-07-16 17:55:07','2012-07-16 17:55:07');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_fbfc09f1` (`user_id`),
  KEY `auth_user_groups_bda51c3c` (`group_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (1,2,1);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_fbfc09f1` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_buenaspracticas`
--

DROP TABLE IF EXISTS `bosques_buenaspracticas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_buenaspracticas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_buenaspracticas`
--

LOCK TABLES `bosques_buenaspracticas` WRITE;
/*!40000 ALTER TABLE `bosques_buenaspracticas` DISABLE KEYS */;
INSERT INTO `bosques_buenaspracticas` VALUES (1,'Planificación forestal'),(2,'Manejo silvicultura'),(3,'Aprovechamiento de bajo impacto'),(4,'Gestión de insumos y residuos'),(5,'Protección de biodiversidad'),(6,'Planes de negocio'),(7,'Agroforestería'),(8,'Manejo de bosque'),(9,'Manejo de plantación');
/*!40000 ALTER TABLE `bosques_buenaspracticas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_datos`
--

DROP TABLE IF EXISTS `bosques_datos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_datos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha_seguimiento` date NOT NULL,
  `hombre` int(11) NOT NULL,
  `mujeres` int(11) NOT NULL,
  `uso_agricola` double NOT NULL,
  `uso_pecuario` double NOT NULL,
  `uso_foretal` double NOT NULL,
  `bosque_bajo_manejo` double NOT NULL,
  `uso_agroforestal` double NOT NULL,
  `otros_usos` double NOT NULL,
  `poa_ejecucion` varchar(200) NOT NULL,
  `area_poa` double NOT NULL,
  `permiso_poa` varchar(200) NOT NULL,
  `volumen_cosecha` double NOT NULL,
  `segui_plantaciones` double NOT NULL,
  `registro_orfn` varchar(200) NOT NULL,
  `certificado` int(11) NOT NULL,
  `estado_certificado` int(11) NOT NULL,
  `sequimiento_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `bosques_datos_60f67ab8` (`sequimiento_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_datos`
--

LOCK TABLES `bosques_datos` WRITE;
/*!40000 ALTER TABLE `bosques_datos` DISABLE KEYS */;
/*!40000 ALTER TABLE `bosques_datos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_datos_tipo_certificacion`
--

DROP TABLE IF EXISTS `bosques_datos_tipo_certificacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_datos_tipo_certificacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `datos_id` int(11) NOT NULL,
  `tipocertificacion_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `bosques_datos_tipo_certificacion_datos_id_54a2f9479cc5b8fd_uniq` (`datos_id`,`tipocertificacion_id`),
  KEY `bosques_datos_tipo_certificacion_fb5fa314` (`datos_id`),
  KEY `bosques_datos_tipo_certificacion_cdb94cf8` (`tipocertificacion_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_datos_tipo_certificacion`
--

LOCK TABLES `bosques_datos_tipo_certificacion` WRITE;
/*!40000 ALTER TABLE `bosques_datos_tipo_certificacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `bosques_datos_tipo_certificacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_empresa`
--

DROP TABLE IF EXISTS `bosques_empresa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_empresa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_empresa`
--

LOCK TABLES `bosques_empresa` WRITE;
/*!40000 ALTER TABLE `bosques_empresa` DISABLE KEYS */;
INSERT INTO `bosques_empresa` VALUES (1,'SIMAS'),(2,'Los Pinos');
/*!40000 ALTER TABLE `bosques_empresa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_encuestador`
--

DROP TABLE IF EXISTS `bosques_encuestador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_encuestador` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_encuestador`
--

LOCK TABLES `bosques_encuestador` WRITE;
/*!40000 ALTER TABLE `bosques_encuestador` DISABLE KEYS */;
INSERT INTO `bosques_encuestador` VALUES (1,'Martha Olivera'),(2,'Byron Corrales');
/*!40000 ALTER TABLE `bosques_encuestador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_especiesintroducidas`
--

DROP TABLE IF EXISTS `bosques_especiesintroducidas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_especiesintroducidas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_especiesintroducidas`
--

LOCK TABLES `bosques_especiesintroducidas` WRITE;
/*!40000 ALTER TABLE `bosques_especiesintroducidas` DISABLE KEYS */;
INSERT INTO `bosques_especiesintroducidas` VALUES (1,'Caoba africana'),(2,'Teca'),(3,'Neen'),(4,'Melina'),(5,'Eucalipto'),(6,'Acacia');
/*!40000 ALTER TABLE `bosques_especiesintroducidas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_especiesnaturales`
--

DROP TABLE IF EXISTS `bosques_especiesnaturales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_especiesnaturales` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_especiesnaturales`
--

LOCK TABLES `bosques_especiesnaturales` WRITE;
/*!40000 ALTER TABLE `bosques_especiesnaturales` DISABLE KEYS */;
INSERT INTO `bosques_especiesnaturales` VALUES (1,'Madero negro'),(2,'Marango'),(3,'Cedro'),(4,'Pochote'),(5,'Laurel'),(6,'Guanacaste'),(7,'Genízaro'),(8,'Cedro macho'),(9,'Cedro real'),(10,'Caoba Atlántico'),(11,'Caoba Pacífico'),(12,'Nancitón'),(13,'Guapinol'),(14,'Coyote'),(15,'Pino'),(16,'Ojoche');
/*!40000 ALTER TABLE `bosques_especiesnaturales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_gobiernogti`
--

DROP TABLE IF EXISTS `bosques_gobiernogti`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_gobiernogti` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_gobiernogti`
--

LOCK TABLES `bosques_gobiernogti` WRITE;
/*!40000 ALTER TABLE `bosques_gobiernogti` DISABLE KEYS */;
/*!40000 ALTER TABLE `bosques_gobiernogti` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_madera`
--

DROP TABLE IF EXISTS `bosques_madera`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_madera` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_madera`
--

LOCK TABLES `bosques_madera` WRITE;
/*!40000 ALTER TABLE `bosques_madera` DISABLE KEYS */;
INSERT INTO `bosques_madera` VALUES (1,'Madera en rollo');
/*!40000 ALTER TABLE `bosques_madera` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_metodoextraccion`
--

DROP TABLE IF EXISTS `bosques_metodoextraccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_metodoextraccion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_metodoextraccion`
--

LOCK TABLES `bosques_metodoextraccion` WRITE;
/*!40000 ALTER TABLE `bosques_metodoextraccion` DISABLE KEYS */;
INSERT INTO `bosques_metodoextraccion` VALUES (1,'Mecanizado'),(2,'Tracción animal');
/*!40000 ALTER TABLE `bosques_metodoextraccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_organizacion`
--

DROP TABLE IF EXISTS `bosques_organizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_organizacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_organizacion`
--

LOCK TABLES `bosques_organizacion` WRITE;
/*!40000 ALTER TABLE `bosques_organizacion` DISABLE KEYS */;
INSERT INTO `bosques_organizacion` VALUES (1,'prueba Organizacion');
/*!40000 ALTER TABLE `bosques_organizacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_organizado`
--

DROP TABLE IF EXISTS `bosques_organizado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_organizado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_organizado`
--

LOCK TABLES `bosques_organizado` WRITE;
/*!40000 ALTER TABLE `bosques_organizado` DISABLE KEYS */;
INSERT INTO `bosques_organizado` VALUES (1,'No organizado'),(2,'Asociación gremial'),(3,'Cooperativa'),(4,'Empresa rural');
/*!40000 ALTER TABLE `bosques_organizado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_procesoindustrialbosque`
--

DROP TABLE IF EXISTS `bosques_procesoindustrialbosque`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_procesoindustrialbosque` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_procesoindustrialbosque`
--

LOCK TABLES `bosques_procesoindustrialbosque` WRITE;
/*!40000 ALTER TABLE `bosques_procesoindustrialbosque` DISABLE KEYS */;
INSERT INTO `bosques_procesoindustrialbosque` VALUES (1,'Aserrado'),(2,'Arrastre de la madera'),(3,'Troceo'),(4,'Transporte secado de la madera');
/*!40000 ALTER TABLE `bosques_procesoindustrialbosque` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_propietariobosques`
--

DROP TABLE IF EXISTS `bosques_propietariobosques`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_propietariobosques` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `encuestador_id` int(11) NOT NULL,
  `empresa_id` int(11) NOT NULL,
  `nombre_propietario` varchar(200) NOT NULL,
  `sexo_propietario` int(11) NOT NULL,
  `cedula_propietario` varchar(200) NOT NULL,
  `propietario_ruc` varchar(200) NOT NULL,
  `representante_tecnico` varchar(200) NOT NULL,
  `sexo_tecnico` int(11) NOT NULL,
  `cedula_tecnico` varchar(200) NOT NULL,
  `tecnico_ruc` varchar(200) NOT NULL,
  `nombre_propiedad` varchar(200) NOT NULL,
  `registro_catastral` varchar(200) NOT NULL,
  `area_propiedad` double NOT NULL,
  `tel_convencional` varchar(15) DEFAULT NULL,
  `tel_celular` varchar(15) DEFAULT NULL,
  `email` varchar(75) DEFAULT NULL,
  `web` varchar(200) DEFAULT NULL,
  `direccion` varchar(200) DEFAULT NULL,
  `latitud` double DEFAULT NULL,
  `longitud` double DEFAULT NULL,
  `departamento_id` int(11) NOT NULL,
  `municipio_id` int(11) NOT NULL,
  `comunidad_id` int(11) NOT NULL,
  `desde` date NOT NULL,
  `gobierno_gti` int(11) NOT NULL,
  `nombre_gti_id` int(11) DEFAULT NULL,
  `madera_id` int(11) DEFAULT NULL,
  `madera_procesada` int(11) DEFAULT NULL,
  `consumo` int(11) DEFAULT NULL,
  `producto_no_maderable` int(11) NOT NULL,
  `nombre_umf` varchar(200) NOT NULL,
  `area_umf` double NOT NULL,
  `codigo_umf` varchar(200) NOT NULL,
  `periodo_vigencia` int(11) NOT NULL,
  `poas_umf` int(11) NOT NULL,
  `secado_horno` double NOT NULL,
  `codigo_certificado` varchar(200) DEFAULT NULL,
  `area_certificada` double DEFAULT NULL,
  `year` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `bosques_propietariobosques_38e1e44c` (`encuestador_id`),
  KEY `bosques_propietariobosques_54324052` (`empresa_id`),
  KEY `bosques_propietariobosques_8865b15a` (`departamento_id`),
  KEY `bosques_propietariobosques_f3143aaa` (`municipio_id`),
  KEY `bosques_propietariobosques_62329ccf` (`comunidad_id`),
  KEY `bosques_propietariobosques_452c327a` (`nombre_gti_id`),
  KEY `bosques_propietariobosques_21274626` (`madera_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_propietariobosques`
--

LOCK TABLES `bosques_propietariobosques` WRITE;
/*!40000 ALTER TABLE `bosques_propietariobosques` DISABLE KEYS */;
INSERT INTO `bosques_propietariobosques` VALUES (1,'2012-07-13',1,1,'Byron Corrales Rivas',1,'001-030386-0003E','001-030386-0003E','Carlos Rocha',1,'001-030386-0003E','001-030386-0003E','Reserva El Arenal','1234',34,'22491062','86635944','byroncorrales@gmail.com','http://www.simas.org.ni/','P del H 1c a 3 1/2c al sur',13.066687,-85.873518,10,1035,1,'2010-07-13',2,NULL,1,1,1,1,'El Arenal',23,'1234',2,1,23,'123123',34,2012),(2,'2012-07-13',2,2,'Aureliano y José Arcadio Buendía',1,'003-250626-3365ñ','14586598-23','Gabriel García Márquez',1,'00358689','556889-415','Cien años ','454555',236,'225687855','8554588565','cien@buendia.com','http://www.buendia.com/','Km 456.5 carretera Cuajiniquilapa',12.66,-86.233,5,550,2,'2000-07-13',2,NULL,NULL,2,2,2,'Edityo',45,'2525',10,11,5658,'',NULL,2012),(3,'2012-07-13',2,1,'Julio Gonzalez Smith',1,'062938','55566677','Silver Borge',1,'000-2345-888J','678321A','Pueblo Nuevo','034567',15,'','','','','',12.88678,-84.057312,93,9315,3,'2012-07-13',2,NULL,1,1,1,1,'Finca Pueblo Nuevo',5,'000999',5,5,0,'',NULL,2012);
/*!40000 ALTER TABLE `bosques_propietariobosques` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_propietariobosques_bosques_umf`
--

DROP TABLE IF EXISTS `bosques_propietariobosques_bosques_umf`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_propietariobosques_bosques_umf` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `propietariobosques_id` int(11) NOT NULL,
  `tipobosqueumf_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `bosques_propietario_propietariobosques_id_566dbc4b365f7ecb_uniq` (`propietariobosques_id`,`tipobosqueumf_id`),
  KEY `bosques_propietariobosques_bosques_umf_1e1584c2` (`propietariobosques_id`),
  KEY `bosques_propietariobosques_bosques_umf_8576d06a` (`tipobosqueumf_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_propietariobosques_bosques_umf`
--

LOCK TABLES `bosques_propietariobosques_bosques_umf` WRITE;
/*!40000 ALTER TABLE `bosques_propietariobosques_bosques_umf` DISABLE KEYS */;
INSERT INTO `bosques_propietariobosques_bosques_umf` VALUES (1,1,2),(5,2,4),(4,2,2),(6,3,2);
/*!40000 ALTER TABLE `bosques_propietariobosques_bosques_umf` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_propietariobosques_buenas_practicas`
--

DROP TABLE IF EXISTS `bosques_propietariobosques_buenas_practicas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_propietariobosques_buenas_practicas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `propietariobosques_id` int(11) NOT NULL,
  `buenaspracticas_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `bosques_propietario_propietariobosques_id_10adbd03245b471b_uniq` (`propietariobosques_id`,`buenaspracticas_id`),
  KEY `bosques_propietariobosques_buenas_practicas_1e1584c2` (`propietariobosques_id`),
  KEY `bosques_propietariobosques_buenas_practicas_3af323a7` (`buenaspracticas_id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_propietariobosques_buenas_practicas`
--

LOCK TABLES `bosques_propietariobosques_buenas_practicas` WRITE;
/*!40000 ALTER TABLE `bosques_propietariobosques_buenas_practicas` DISABLE KEYS */;
INSERT INTO `bosques_propietariobosques_buenas_practicas` VALUES (1,1,6),(2,1,7),(8,2,7),(7,2,5),(6,2,3),(9,3,1),(10,3,2),(11,3,3);
/*!40000 ALTER TABLE `bosques_propietariobosques_buenas_practicas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_propietariobosques_extraccion`
--

DROP TABLE IF EXISTS `bosques_propietariobosques_extraccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_propietariobosques_extraccion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `propietariobosques_id` int(11) NOT NULL,
  `metodoextraccion_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `bosques_propietario_propietariobosques_id_24fd09128090b67b_uniq` (`propietariobosques_id`,`metodoextraccion_id`),
  KEY `bosques_propietariobosques_extraccion_1e1584c2` (`propietariobosques_id`),
  KEY `bosques_propietariobosques_extraccion_2e278d0` (`metodoextraccion_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_propietariobosques_extraccion`
--

LOCK TABLES `bosques_propietariobosques_extraccion` WRITE;
/*!40000 ALTER TABLE `bosques_propietariobosques_extraccion` DISABLE KEYS */;
INSERT INTO `bosques_propietariobosques_extraccion` VALUES (1,1,2),(5,2,2),(4,2,1),(6,3,2);
/*!40000 ALTER TABLE `bosques_propietariobosques_extraccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_propietariobosques_introducida`
--

DROP TABLE IF EXISTS `bosques_propietariobosques_introducida`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_propietariobosques_introducida` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `propietariobosques_id` int(11) NOT NULL,
  `especiesintroducidas_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `bosques_propietario_propietariobosques_id_77bcfd4bf5049038_uniq` (`propietariobosques_id`,`especiesintroducidas_id`),
  KEY `bosques_propietariobosques_introducida_1e1584c2` (`propietariobosques_id`),
  KEY `bosques_propietariobosques_introducida_7f0c61c8` (`especiesintroducidas_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_propietariobosques_introducida`
--

LOCK TABLES `bosques_propietariobosques_introducida` WRITE;
/*!40000 ALTER TABLE `bosques_propietariobosques_introducida` DISABLE KEYS */;
INSERT INTO `bosques_propietariobosques_introducida` VALUES (1,1,4),(2,1,5),(3,1,6),(5,2,6),(6,3,2),(7,3,5),(8,3,6);
/*!40000 ALTER TABLE `bosques_propietariobosques_introducida` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_propietariobosques_naturales`
--

DROP TABLE IF EXISTS `bosques_propietariobosques_naturales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_propietariobosques_naturales` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `propietariobosques_id` int(11) NOT NULL,
  `especiesnaturales_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `bosques_propietario_propietariobosques_id_35997b561abf067e_uniq` (`propietariobosques_id`,`especiesnaturales_id`),
  KEY `bosques_propietariobosques_naturales_1e1584c2` (`propietariobosques_id`),
  KEY `bosques_propietariobosques_naturales_6383821b` (`especiesnaturales_id`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_propietariobosques_naturales`
--

LOCK TABLES `bosques_propietariobosques_naturales` WRITE;
/*!40000 ALTER TABLE `bosques_propietariobosques_naturales` DISABLE KEYS */;
INSERT INTO `bosques_propietariobosques_naturales` VALUES (1,1,1),(2,1,2),(3,1,3),(11,2,6),(10,2,10),(9,2,11),(8,2,2),(12,3,2),(13,3,3),(14,3,4),(15,3,5),(16,3,6),(17,3,7),(18,3,8),(19,3,9),(20,3,10),(21,3,11),(22,3,12);
/*!40000 ALTER TABLE `bosques_propietariobosques_naturales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_propietariobosques_organizacion`
--

DROP TABLE IF EXISTS `bosques_propietariobosques_organizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_propietariobosques_organizacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `propietariobosques_id` int(11) NOT NULL,
  `organizacion_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `bosques_propietario_propietariobosques_id_409cc8e6d00883d7_uniq` (`propietariobosques_id`,`organizacion_id`),
  KEY `bosques_propietariobosques_organizacion_1e1584c2` (`propietariobosques_id`),
  KEY `bosques_propietariobosques_organizacion_48753264` (`organizacion_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_propietariobosques_organizacion`
--

LOCK TABLES `bosques_propietariobosques_organizacion` WRITE;
/*!40000 ALTER TABLE `bosques_propietariobosques_organizacion` DISABLE KEYS */;
INSERT INTO `bosques_propietariobosques_organizacion` VALUES (1,1,1),(3,2,1),(4,3,1);
/*!40000 ALTER TABLE `bosques_propietariobosques_organizacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_propietariobosques_organizado`
--

DROP TABLE IF EXISTS `bosques_propietariobosques_organizado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_propietariobosques_organizado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `propietariobosques_id` int(11) NOT NULL,
  `organizado_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `bosques_propietario_propietariobosques_id_2ebb0f1cbdf4ad2b_uniq` (`propietariobosques_id`,`organizado_id`),
  KEY `bosques_propietariobosques_organizado_1e1584c2` (`propietariobosques_id`),
  KEY `bosques_propietariobosques_organizado_c76e27b2` (`organizado_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_propietariobosques_organizado`
--

LOCK TABLES `bosques_propietariobosques_organizado` WRITE;
/*!40000 ALTER TABLE `bosques_propietariobosques_organizado` DISABLE KEYS */;
INSERT INTO `bosques_propietariobosques_organizado` VALUES (1,1,1),(3,2,1),(4,3,1);
/*!40000 ALTER TABLE `bosques_propietariobosques_organizado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_propietariobosques_procesos_industriales`
--

DROP TABLE IF EXISTS `bosques_propietariobosques_procesos_industriales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_propietariobosques_procesos_industriales` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `propietariobosques_id` int(11) NOT NULL,
  `procesoindustrialbosque_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `bosques_propietario_propietariobosques_id_19509e52e88b4ebe_uniq` (`propietariobosques_id`,`procesoindustrialbosque_id`),
  KEY `bosques_propietariobosques_procesos_industriales_1e1584c2` (`propietariobosques_id`),
  KEY `bosques_propietariobosques_procesos_industriales_c9e18d0e` (`procesoindustrialbosque_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_propietariobosques_procesos_industriales`
--

LOCK TABLES `bosques_propietariobosques_procesos_industriales` WRITE;
/*!40000 ALTER TABLE `bosques_propietariobosques_procesos_industriales` DISABLE KEYS */;
INSERT INTO `bosques_propietariobosques_procesos_industriales` VALUES (1,1,4),(5,2,2),(4,2,1),(6,3,1),(7,3,4);
/*!40000 ALTER TABLE `bosques_propietariobosques_procesos_industriales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_propietariobosques_proveedores`
--

DROP TABLE IF EXISTS `bosques_propietariobosques_proveedores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_propietariobosques_proveedores` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `propietariobosques_id` int(11) NOT NULL,
  `proveedoressuministros_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `bosques_propietario_propietariobosques_id_1a64b4bef5f205ec_uniq` (`propietariobosques_id`,`proveedoressuministros_id`),
  KEY `bosques_propietariobosques_proveedores_1e1584c2` (`propietariobosques_id`),
  KEY `bosques_propietariobosques_proveedores_6034fa8c` (`proveedoressuministros_id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_propietariobosques_proveedores`
--

LOCK TABLES `bosques_propietariobosques_proveedores` WRITE;
/*!40000 ALTER TABLE `bosques_propietariobosques_proveedores` DISABLE KEYS */;
INSERT INTO `bosques_propietariobosques_proveedores` VALUES (1,1,1),(2,1,4),(14,2,10),(13,2,9),(12,2,5),(11,2,4),(10,2,3),(9,2,1),(15,3,9),(16,3,11),(17,3,4),(18,3,7);
/*!40000 ALTER TABLE `bosques_propietariobosques_proveedores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_propietariobosques_secado`
--

DROP TABLE IF EXISTS `bosques_propietariobosques_secado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_propietariobosques_secado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `propietariobosques_id` int(11) NOT NULL,
  `tiposecados_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `bosques_propietario_propietariobosques_id_2efd539d6ce31771_uniq` (`propietariobosques_id`,`tiposecados_id`),
  KEY `bosques_propietariobosques_secado_1e1584c2` (`propietariobosques_id`),
  KEY `bosques_propietariobosques_secado_fb9ebf6f` (`tiposecados_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_propietariobosques_secado`
--

LOCK TABLES `bosques_propietariobosques_secado` WRITE;
/*!40000 ALTER TABLE `bosques_propietariobosques_secado` DISABLE KEYS */;
INSERT INTO `bosques_propietariobosques_secado` VALUES (1,1,5),(5,2,4),(4,2,3),(6,3,1);
/*!40000 ALTER TABLE `bosques_propietariobosques_secado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_propietariobosques_tipo_producto`
--

DROP TABLE IF EXISTS `bosques_propietariobosques_tipo_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_propietariobosques_tipo_producto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `propietariobosques_id` int(11) NOT NULL,
  `tipoproducto_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `bosques_propietario_propietariobosques_id_68d5f0dad9baaaa9_uniq` (`propietariobosques_id`,`tipoproducto_id`),
  KEY `bosques_propietariobosques_tipo_producto_1e1584c2` (`propietariobosques_id`),
  KEY `bosques_propietariobosques_tipo_producto_7afc4aaa` (`tipoproducto_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_propietariobosques_tipo_producto`
--

LOCK TABLES `bosques_propietariobosques_tipo_producto` WRITE;
/*!40000 ALTER TABLE `bosques_propietariobosques_tipo_producto` DISABLE KEYS */;
INSERT INTO `bosques_propietariobosques_tipo_producto` VALUES (1,1,1),(2,1,3),(3,3,1),(4,3,2);
/*!40000 ALTER TABLE `bosques_propietariobosques_tipo_producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_propietariobosques_tipo_propiedad`
--

DROP TABLE IF EXISTS `bosques_propietariobosques_tipo_propiedad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_propietariobosques_tipo_propiedad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `propietariobosques_id` int(11) NOT NULL,
  `tipopropiedadbosque_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `bosques_propietario_propietariobosques_id_14b5ddfe40e77fc8_uniq` (`propietariobosques_id`,`tipopropiedadbosque_id`),
  KEY `bosques_propietariobosques_tipo_propiedad_1e1584c2` (`propietariobosques_id`),
  KEY `bosques_propietariobosques_tipo_propiedad_4ba5ef2` (`tipopropiedadbosque_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_propietariobosques_tipo_propiedad`
--

LOCK TABLES `bosques_propietariobosques_tipo_propiedad` WRITE;
/*!40000 ALTER TABLE `bosques_propietariobosques_tipo_propiedad` DISABLE KEYS */;
INSERT INTO `bosques_propietariobosques_tipo_propiedad` VALUES (1,1,4),(3,2,4),(4,3,1);
/*!40000 ALTER TABLE `bosques_propietariobosques_tipo_propiedad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_proveedoressuministros`
--

DROP TABLE IF EXISTS `bosques_proveedoressuministros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_proveedoressuministros` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_proveedoressuministros`
--

LOCK TABLES `bosques_proveedoressuministros` WRITE;
/*!40000 ALTER TABLE `bosques_proveedoressuministros` DISABLE KEYS */;
INSERT INTO `bosques_proveedoressuministros` VALUES (1,'Comunidades'),(2,'Finqueros'),(3,'Estaciones de combustible y lubricantes'),(4,'Distribuidoras de alimentos'),(5,'Distribuidores de maquinaria y equipos'),(6,'Librerías'),(7,'Ferreterías'),(8,'Tiendas especializadas en equipos y artículos forestales'),(9,'Ventas de repuestos'),(10,'Rentado de maquinaria pesada'),(11,'Regentes');
/*!40000 ALTER TABLE `bosques_proveedoressuministros` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_seguimiento`
--

DROP TABLE IF EXISTS `bosques_seguimiento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_seguimiento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `propietario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `bosques_seguimiento_2b2afea1` (`propietario_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_seguimiento`
--

LOCK TABLES `bosques_seguimiento` WRITE;
/*!40000 ALTER TABLE `bosques_seguimiento` DISABLE KEYS */;
/*!40000 ALTER TABLE `bosques_seguimiento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_tipobosqueumf`
--

DROP TABLE IF EXISTS `bosques_tipobosqueumf`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_tipobosqueumf` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_tipobosqueumf`
--

LOCK TABLES `bosques_tipobosqueumf` WRITE;
/*!40000 ALTER TABLE `bosques_tipobosqueumf` DISABLE KEYS */;
INSERT INTO `bosques_tipobosqueumf` VALUES (1,'Bosque natural seco'),(2,'Bosque natural húmedo'),(3,'Plantaciones forestales'),(4,'Bosque de manglares');
/*!40000 ALTER TABLE `bosques_tipobosqueumf` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_tipocertificacion`
--

DROP TABLE IF EXISTS `bosques_tipocertificacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_tipocertificacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_tipocertificacion`
--

LOCK TABLES `bosques_tipocertificacion` WRITE;
/*!40000 ALTER TABLE `bosques_tipocertificacion` DISABLE KEYS */;
INSERT INTO `bosques_tipocertificacion` VALUES (1,'FSC'),(2,'CW Full'),(3,'SLIMF'),(4,'Comercio justo'),(5,'ISSO'),(6,'Otras');
/*!40000 ALTER TABLE `bosques_tipocertificacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_tipoproducto`
--

DROP TABLE IF EXISTS `bosques_tipoproducto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_tipoproducto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_tipoproducto`
--

LOCK TABLES `bosques_tipoproducto` WRITE;
/*!40000 ALTER TABLE `bosques_tipoproducto` DISABLE KEYS */;
INSERT INTO `bosques_tipoproducto` VALUES (1,'Semillas forestales'),(2,'Bejuco mimbre'),(3,'Palmas'),(4,'Alimentos');
/*!40000 ALTER TABLE `bosques_tipoproducto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_tipopropiedadbosque`
--

DROP TABLE IF EXISTS `bosques_tipopropiedadbosque`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_tipopropiedadbosque` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_tipopropiedadbosque`
--

LOCK TABLES `bosques_tipopropiedadbosque` WRITE;
/*!40000 ALTER TABLE `bosques_tipopropiedadbosque` DISABLE KEYS */;
INSERT INTO `bosques_tipopropiedadbosque` VALUES (1,'Privada individual'),(2,'Privada sociedad empresarial'),(3,'Colectiva indígena'),(4,'Colectiva cooperativa');
/*!40000 ALTER TABLE `bosques_tipopropiedadbosque` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosques_tiposecados`
--

DROP TABLE IF EXISTS `bosques_tiposecados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosques_tiposecados` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosques_tiposecados`
--

LOCK TABLES `bosques_tiposecados` WRITE;
/*!40000 ALTER TABLE `bosques_tiposecados` DISABLE KEYS */;
INSERT INTO `bosques_tiposecados` VALUES (1,'Natural (al aire libre)'),(2,'Horno solar'),(3,'Horno artesanal'),(4,'Horno convencional eléctrico'),(5,'Horno con residuo y desechos de madera'),(6,'Otros');
/*!40000 ALTER TABLE `bosques_tiposecados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_fbfc09f1` (`user_id`),
  KEY `django_admin_log_e4470c6e` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=101 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2012-07-13 20:19:14',1,24,'1','Planificación forestal',1,''),(2,'2012-07-13 20:19:33',1,24,'2','Manejo silvicultura',1,''),(3,'2012-07-13 20:19:51',1,24,'3','Aprovechamiento de bajo impacto',1,''),(4,'2012-07-13 20:20:07',1,24,'4','Gestión de insumos y residuos',1,''),(5,'2012-07-13 20:20:33',1,24,'5','Protección de biodiversidad',1,''),(6,'2012-07-13 20:20:40',1,2,'1','conicefv',1,''),(7,'2012-07-13 20:20:45',1,24,'6','Planes de negocio',1,''),(8,'2012-07-13 20:21:06',1,24,'7','Agroforestería',1,''),(9,'2012-07-13 20:21:19',1,24,'8','Manejo de bosque',1,''),(10,'2012-07-13 20:21:28',1,3,'2','conicefv',1,''),(11,'2012-07-13 20:21:30',1,24,'9','Manejo de plantación',1,''),(12,'2012-07-13 20:21:39',1,3,'2','conicefv',2,'Modificado/a password, is_staff y groups.'),(13,'2012-07-13 20:23:10',1,2,'1','conicefv',2,'Modificado/a permissions.'),(14,'2012-07-13 20:24:28',1,18,'1','Madero negro',1,''),(15,'2012-07-13 20:24:42',1,18,'2','Marango',1,''),(16,'2012-07-13 20:24:49',1,18,'3','Cedro',1,''),(17,'2012-07-13 20:24:55',1,18,'4','Pochote',1,''),(18,'2012-07-13 20:25:03',1,18,'5','Laurel',1,''),(19,'2012-07-13 20:25:11',1,18,'6','Guanacaste',1,''),(20,'2012-07-13 20:25:19',1,18,'7','Genízaro',1,''),(21,'2012-07-13 20:25:36',1,18,'8','Cedro macho',1,''),(22,'2012-07-13 20:25:46',1,18,'9','Cedro real',1,''),(23,'2012-07-13 20:25:58',1,18,'10','Caoba atlántico',1,''),(24,'2012-07-13 20:26:08',1,18,'11','Caoba pacífico',1,''),(25,'2012-07-13 20:26:16',1,18,'12','Nancitón',1,''),(26,'2012-07-13 20:26:27',1,18,'13','Guapinol',1,''),(27,'2012-07-13 20:26:35',1,18,'14','Coyote',1,''),(28,'2012-07-13 20:26:41',1,18,'15','Pino',1,''),(29,'2012-07-13 20:26:58',1,18,'10','Caoba Atlántico',2,'Modificado/a nombre.'),(30,'2012-07-13 20:27:32',1,18,'11','Caoba Pacífico',2,'Modificado/a nombre.'),(31,'2012-07-13 20:34:17',1,19,'1','Caoba africana',1,''),(32,'2012-07-13 20:34:29',1,19,'2','Teca',1,''),(33,'2012-07-13 20:36:27',1,19,'3','Neen',1,''),(34,'2012-07-13 20:36:48',1,19,'4','Melina',1,''),(35,'2012-07-13 20:36:54',1,19,'5','Eucalipto',1,''),(36,'2012-07-13 20:37:02',1,19,'6','Acacia',1,''),(37,'2012-07-13 20:40:50',1,21,'1','Madera en rollo',1,''),(38,'2012-07-13 20:45:19',1,20,'1','Madera en rollo',1,''),(39,'2012-07-13 20:46:11',1,21,'1','Semillas forestales',2,'Modificado/a nombre.'),(40,'2012-07-13 20:46:38',1,21,'2','Bejuco mimbre',1,''),(41,'2012-07-13 20:46:47',1,21,'3','Palmas',1,''),(42,'2012-07-13 20:46:54',1,21,'4','Alimentos',1,''),(43,'2012-07-13 20:47:38',1,22,'1','Aserrado',1,''),(44,'2012-07-13 20:47:56',1,22,'2','Arrastre de la madera',1,''),(45,'2012-07-13 20:48:04',1,22,'3','Troceo',1,''),(46,'2012-07-13 20:48:24',1,22,'4','Transporte secado de la madera',1,''),(47,'2012-07-13 20:50:28',1,23,'1','Natural (al aire libre)',1,''),(48,'2012-07-13 20:50:42',1,23,'2','Horno solar',1,''),(49,'2012-07-13 20:50:51',1,23,'3','Horno artesanal',1,''),(50,'2012-07-13 20:51:08',1,23,'4','Horno convencional eléctrico',1,''),(51,'2012-07-13 20:51:22',1,23,'5','Horno con residuo y desechos de madera',1,''),(52,'2012-07-13 20:51:36',1,23,'6','Otros',1,''),(53,'2012-07-13 20:53:53',1,25,'1','Comunidades',1,''),(54,'2012-07-13 20:54:00',1,25,'2','Finqueros',1,''),(55,'2012-07-13 20:54:17',1,25,'3','Estaciones de combustible y lubricantes',1,''),(56,'2012-07-13 20:54:28',1,25,'4','Distribuidoras de alimentos',1,''),(57,'2012-07-13 20:54:44',1,25,'5','Distribuidores de maquinaria y equipos',1,''),(58,'2012-07-13 20:54:56',1,25,'6','Librerías',1,''),(59,'2012-07-13 20:55:02',1,25,'7','Ferreterías',1,''),(60,'2012-07-13 20:55:29',1,25,'8','Tiendas especializadas en equipos y artículos forestales',1,''),(61,'2012-07-13 20:55:39',1,25,'9','Ventas de repuestos',1,''),(62,'2012-07-13 20:55:50',1,25,'10','Rentado de maquinaria pesada',1,''),(63,'2012-07-13 20:55:58',1,25,'11','Regentes',1,''),(64,'2012-07-13 21:28:15',1,26,'1','Bosque natural seco',1,''),(65,'2012-07-13 21:28:25',1,26,'2','Bosque natural húmedo',1,''),(66,'2012-07-13 21:28:35',1,26,'3','Plantaciones forestales',1,''),(67,'2012-07-13 21:28:54',1,26,'4','Bosque de manglares',1,''),(68,'2012-07-13 21:29:26',1,27,'1','Mecanizado',1,''),(69,'2012-07-13 21:29:35',1,27,'2','Tracción animal',1,''),(70,'2012-07-13 21:38:02',1,30,'1','FSC',1,''),(71,'2012-07-13 21:38:19',1,30,'2','CW Full',1,''),(72,'2012-07-13 21:38:38',1,30,'3','SLIMF',1,''),(73,'2012-07-13 21:38:46',1,30,'4','Comercio justo',1,''),(74,'2012-07-13 21:38:53',1,30,'5','ISSO',1,''),(75,'2012-07-13 21:39:02',1,30,'6','Otras',1,''),(76,'2012-07-13 21:48:53',1,15,'1','No organizado',1,''),(77,'2012-07-13 21:49:03',1,15,'2','Asociación gremial',1,''),(78,'2012-07-13 21:49:11',1,15,'3','Cooperativa',1,''),(79,'2012-07-13 21:49:17',1,15,'4','Empresa rural',1,''),(80,'2012-07-13 21:51:14',1,14,'1','Privada individual',1,''),(81,'2012-07-13 21:51:25',1,14,'2','Privada sociedad empresarial',1,''),(82,'2012-07-13 21:51:33',1,14,'3','Colectiva indígena',1,''),(83,'2012-07-13 21:51:43',1,14,'4','Colectiva cooperativa',1,''),(84,'2012-07-13 22:00:59',1,16,'1','prueba Organizacion',1,''),(85,'2012-07-13 22:12:57',2,12,'1','Martha Olivera',1,''),(86,'2012-07-13 22:13:05',2,13,'1','SIMAS',1,''),(87,'2012-07-13 22:39:57',1,2,'1','conicefv',2,'Modificado/a permissions.'),(88,'2012-07-13 22:45:08',2,11,'1','Aranjuez',1,''),(89,'2012-07-13 22:46:58',1,2,'1','conicefv',2,'Modificado/a permissions.'),(90,'2012-07-13 22:47:59',2,28,'1','Byron Corrales Rivas',1,''),(91,'2012-07-13 22:48:42',2,12,'2','Byron Corrales',1,''),(92,'2012-07-13 22:49:39',2,13,'2','Los Pinos',1,''),(93,'2012-07-13 22:53:58',2,11,'2','Soledad',1,''),(94,'2012-07-13 22:56:33',1,2,'1','conicefv',2,'Modificado/a permissions.'),(95,'2012-07-13 23:00:12',2,28,'2','Aureliano y José Arcadio Buendía',1,''),(96,'2012-07-13 23:01:05',2,28,'2','Aureliano y José Arcadio Buendía',2,'Modificado/a longitud.'),(97,'2012-07-14 00:40:46',2,11,'3','Pueblo Nuevo',1,''),(98,'2012-07-14 00:43:39',2,28,'3','Julio Gonzalez Smith',1,''),(99,'2012-07-16 17:50:39',1,18,'16','Ojoche',1,''),(100,'2012-07-16 17:55:07',1,3,'3','test',1,'');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=32 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'content type','contenttypes','contenttype'),(5,'session','sessions','session'),(6,'site','sites','site'),(7,'log entry','admin','logentry'),(8,'migration history','south','migrationhistory'),(9,'departamento','lugar','departamento'),(10,'municipio','lugar','municipio'),(11,'comunidad','lugar','comunidad'),(12,'encuestador','bosques','encuestador'),(13,'empresa','bosques','empresa'),(14,'tipo propiedad bosque','bosques','tipopropiedadbosque'),(15,'organizado','bosques','organizado'),(16,'organizacion','bosques','organizacion'),(17,'gobierno gti','bosques','gobiernogti'),(18,'especies naturales','bosques','especiesnaturales'),(19,'especies introducidas','bosques','especiesintroducidas'),(20,'madera','bosques','madera'),(21,'tipo producto','bosques','tipoproducto'),(22,'proceso industrial bosque','bosques','procesoindustrialbosque'),(23,'tipo secados','bosques','tiposecados'),(24,'buenas practicas','bosques','buenaspracticas'),(25,'proveedores suministros','bosques','proveedoressuministros'),(26,'tipo bosque umf','bosques','tipobosqueumf'),(27,'metodo extraccion','bosques','metodoextraccion'),(28,'propietario bosques','bosques','propietariobosques'),(29,'seguimiento','bosques','seguimiento'),(30,'tipo certificacion','bosques','tipocertificacion'),(31,'datos','bosques','datos');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_c25c2c28` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('9802fc49c3259a226f609d244080163c','NTgwZDg5NjU5NWQwNGQxNWZhOGU1MzM4ZjQxNWRhMWU5MmE2NzAwMjqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-07-31 14:02:26'),('bd5a858d91df1de57b13ad54c263354f','N2ZmNjQzMTYxMjliZjg5ZTJjMDgyMDU4MjJjZDdhZDdjYzUzZWU0NTqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2012-07-30 17:49:00'),('94501c5d3b403c114a92ed1e8de4c631','MTQ3MmJkMmY1NzViMjRjZDMzMGZlZTUzZDhjYzRkODk0ZDU4ZWI3YzqAAn1xAShVDV9hdXRoX3Vz\nZXJfaWSKAQFVA2d0aU5VBWZlY2hhTlUSX2F1dGhfdXNlcl9iYWNrZW5kVSlkamFuZ28uY29udHJp\nYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZFUOdGlwb19wcm9waWVkYWROVQ90aXBvX2Jvc3F1\nZV91bWZOVQpvcmdhbml6YWRvTnUu\n','2012-07-30 16:10:45'),('b95cffe21e11d132d805761c6483b232','NWQyZmY5MDI0NmI5ZmQyNmY2MGVjYTY3N2RmOWFiNzIzZjcwY2I5ODqAAn1xAShVA2d0aU5VBWZl\nY2hhTlUKdGVzdGNvb2tpZVUGd29ya2VkcQJVDnRpcG9fcHJvcGllZGFkTlUPdGlwb19ib3NxdWVf\ndW1mTlUKb3JnYW5pemFkb051Lg==\n','2012-07-30 04:36:23'),('02d4b363817bf1e42f47e8a005d28407','YzU3MjI4MTVlMDA4NDZlZmMzODhiMjljMWU3YmY1NDkxZmFkMzRmMzqAAn1xAShVDV9hdXRoX3Vz\nZXJfaWSKAQJVA2d0aU5VBWZlY2hhTlUSX2F1dGhfdXNlcl9iYWNrZW5kVSlkamFuZ28uY29udHJp\nYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZFUOdGlwb19wcm9waWVkYWROVQ90aXBvX2Jvc3F1\nZV91bWZOVQpvcmdhbml6YWRvTnUu\n','2012-07-27 22:22:55'),('f4940618f10f991bac1d26590ff516b4','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-07-27 20:59:39'),('0d342fb03adbc8ed719c50df6b372618','YzU3MjI4MTVlMDA4NDZlZmMzODhiMjljMWU3YmY1NDkxZmFkMzRmMzqAAn1xAShVDV9hdXRoX3Vz\nZXJfaWSKAQJVA2d0aU5VBWZlY2hhTlUSX2F1dGhfdXNlcl9iYWNrZW5kVSlkamFuZ28uY29udHJp\nYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZFUOdGlwb19wcm9waWVkYWROVQ90aXBvX2Jvc3F1\nZV91bWZOVQpvcmdhbml6YWRvTnUu\n','2012-08-03 21:12:55'),('91d5b70708b99101817dd9e1c2dd62fd','NGU2OTMyMmNlNzAzMzBjZDlhY2RhMzRmZjQ3NTBiZDdjMTQ1YjVkNzqAAn1xAS4=\n','2012-07-30 15:15:42'),('fb9ce2ea19339267d527a61e03e13a21','NDI0MWY5MTcxYzc2MTQwNjJmOGIyZTQ5Zjk1ZDZkMzMzNWY4NDgyMTqAAn1xAShVDV9hdXRoX3Vz\nZXJfaWSKAQJVA2d0aVgBAAAAMVUFZmVjaGFYBAAAADIwMTJxAlUSX2F1dGhfdXNlcl9iYWNrZW5k\nVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZFUOdGlwb19wcm9waWVk\nYWRjZGphbmdvLmRiLm1vZGVscy5iYXNlCm1vZGVsX3VucGlja2xlCnEDY2Jvc3F1ZXMubW9kZWxz\nClRpcG9Qcm9waWVkYWRCb3NxdWUKcQRdY2RqYW5nby5kYi5tb2RlbHMuYmFzZQpzaW1wbGVfY2xh\nc3NfZmFjdG9yeQpxBYdScQZ9cQcoVQZub21icmVxCFgVAAAAQ29sZWN0aXZhIGNvb3BlcmF0aXZh\nVQZfc3RhdGVxCWNkamFuZ28uZGIubW9kZWxzLmJhc2UKTW9kZWxTdGF0ZQpxCimBcQt9cQwoVQZh\nZGRpbmdxDYlVAmRicQ5VB2RlZmF1bHRxD3ViVQJpZHEQigEEdWJVD3RpcG9fYm9zcXVlX3VtZmgD\nY2Jvc3F1ZXMubW9kZWxzClRpcG9Cb3NxdWVVbWYKcRFdaAWHUnESfXETKGgIWBYAAABCb3NxdWUg\nbmF0dXJhbCBow7ptZWRvaAloCimBcRR9cRUoaA2JaA5oD3ViaBCKAQJ1YlUKb3JnYW5pemFkb051\nLg==\n','2012-07-27 22:56:32'),('d26c9af4cdfe8c8e9d6306f7985ca71e','YzU3MjI4MTVlMDA4NDZlZmMzODhiMjljMWU3YmY1NDkxZmFkMzRmMzqAAn1xAShVDV9hdXRoX3Vz\nZXJfaWSKAQJVA2d0aU5VBWZlY2hhTlUSX2F1dGhfdXNlcl9iYWNrZW5kVSlkamFuZ28uY29udHJp\nYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZFUOdGlwb19wcm9waWVkYWROVQ90aXBvX2Jvc3F1\nZV91bWZOVQpvcmdhbml6YWRvTnUu\n','2012-07-28 00:46:30'),('fb92879e94beb8b3bcfb115894302c6f','NDBmZDdiN2Y4NjA5MmRhMDkzMzRlNTI4ZWE2NTRjYzUxZDU5MWEzMDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2012-07-28 02:14:11'),('a93567a0d0cc409d5c4dffde0e9015f1','MDRmMTliM2NiMDBmYTEyZDljMTU1YTgzYmMwZTg1MjQ0OTZkNzZkMDqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZmNkamFuZ28uZGIubW9kZWxzLmJhc2UKbW9kZWxfdW5waWNrbGUKcQJjYm9zcXVlcy5t\nb2RlbHMKVGlwb0Jvc3F1ZVVtZgpxA11jZGphbmdvLmRiLm1vZGVscy5iYXNlCnNpbXBsZV9jbGFz\nc19mYWN0b3J5CnEEh1JxBX1xBihVBm5vbWJyZXEHWBMAAABCb3NxdWUgZGUgbWFuZ2xhcmVzVQZf\nc3RhdGVxCGNkamFuZ28uZGIubW9kZWxzLmJhc2UKTW9kZWxTdGF0ZQpxCSmBcQp9cQsoVQZhZGRp\nbmdxDIlVAmRicQ1VB2RlZmF1bHRxDnViVQJpZHEPigEEdWJVA2d0aVgAAAAAVQVmZWNoYVgEAAAA\nMjAxMnEQVQ50aXBvX3Byb3BpZWRhZE5VCm9yZ2FuaXphZG9OdS4=\n','2012-07-29 18:16:04'),('e678cc0291a58bfd8e730200a6c5ea68','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-07-30 13:52:13'),('73122dd1849f5e3fba8d3142a086b51b','N2E0NTgxMmM1OWVlMDA3MzdhZThkNTU2NDE5MzcxYjQ5NjQxYjZlNTqAAn1xAShVDV9hdXRoX3Vz\nZXJfaWRxAooBAlUDZ3RpTlUFZmVjaGFOVRJfYXV0aF91c2VyX2JhY2tlbmRxA1UpZGphbmdvLmNv\nbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmRxBFUOdGlwb19wcm9waWVkYWROVQ90aXBv\nX2Jvc3F1ZV91bWZOVQpvcmdhbml6YWRvTnUu\n','2012-07-30 03:05:35'),('25c3df0534fdb3eb1e65d4da9711de3f','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-07-30 13:55:36'),('f9d1ee21a24c82f92268533b5ed12ae1','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-07-30 16:48:42'),('1530fd83aa6cec3e598ab51b37286f39','YzU3MjI4MTVlMDA4NDZlZmMzODhiMjljMWU3YmY1NDkxZmFkMzRmMzqAAn1xAShVDV9hdXRoX3Vz\nZXJfaWSKAQJVA2d0aU5VBWZlY2hhTlUSX2F1dGhfdXNlcl9iYWNrZW5kVSlkamFuZ28uY29udHJp\nYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZFUOdGlwb19wcm9waWVkYWROVQ90aXBvX2Jvc3F1\nZV91bWZOVQpvcmdhbml6YWRvTnUu\n','2012-07-30 16:10:34'),('e639ce29157320159a18934aa17b3d24','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-07-31 14:02:31'),('74bbd02f3c67df3a1f965c0f75a3a572','YzU3MjI4MTVlMDA4NDZlZmMzODhiMjljMWU3YmY1NDkxZmFkMzRmMzqAAn1xAShVDV9hdXRoX3Vz\nZXJfaWSKAQJVA2d0aU5VBWZlY2hhTlUSX2F1dGhfdXNlcl9iYWNrZW5kVSlkamFuZ28uY29udHJp\nYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZFUOdGlwb19wcm9waWVkYWROVQ90aXBvX2Jvc3F1\nZV91bWZOVQpvcmdhbml6YWRvTnUu\n','2012-07-30 17:56:20'),('34f6a06961f00119768232bddb9f21f5','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-07-30 17:30:21'),('8b1a8ca4271ab701f6ba256ef1c0de5b','NTgwZDg5NjU5NWQwNGQxNWZhOGU1MzM4ZjQxNWRhMWU5MmE2NzAwMjqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-07-31 15:51:32'),('7068e576e4dd7e99d534eecdafcfb5c8','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-07-31 15:52:22'),('5091df24f5a8fa3853285e6c54ae487e','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-08-01 20:43:54'),('0f4a3ac38b58f189fe0783194c6f1886','NTgwZDg5NjU5NWQwNGQxNWZhOGU1MzM4ZjQxNWRhMWU5MmE2NzAwMjqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-08-02 01:12:32'),('e1aa4153b5fcc1181654bef93f43440d','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-08-02 01:39:04'),('505eeb461476cd1cae4e6ac4c6e89fea','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-08-02 09:24:06'),('c2bec869e54f569e73de09ccca50021d','NTgwZDg5NjU5NWQwNGQxNWZhOGU1MzM4ZjQxNWRhMWU5MmE2NzAwMjqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-08-02 09:24:46'),('93e0341beb3a7fc43cf0ebc9b7144474','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-08-03 10:37:46'),('5e262a9a80693a2041aa2ddd32fc0226','NTgwZDg5NjU5NWQwNGQxNWZhOGU1MzM4ZjQxNWRhMWU5MmE2NzAwMjqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-08-03 14:22:50'),('b0c39b1f825e49285f7a964eefad1a19','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-08-03 14:22:56'),('642e8b1a3aaba67505685171e920b6be','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-08-03 18:52:30'),('8ae4502c5eaab4eba0da2e41b1f62c0b','NTgwZDg5NjU5NWQwNGQxNWZhOGU1MzM4ZjQxNWRhMWU5MmE2NzAwMjqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-08-03 19:09:23'),('77471a43856ffd34f614b3cc57aabfd1','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-08-05 01:38:51'),('b2173770b353def7721e5771677768d9','NTgwZDg5NjU5NWQwNGQxNWZhOGU1MzM4ZjQxNWRhMWU5MmE2NzAwMjqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-08-05 02:07:57'),('502f0c65cbea4c45f1680ecdd93dd3d0','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-08-05 17:35:58'),('0732950730e9c3d585474bb643789594','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-08-08 02:15:58'),('fc89ec86c31ee6c6c6a97f3d76e15dca','MmQ5ZGQxMDI4YjU2MDc5Nzc3NGMxNmMyNTcxYmU2NTVkOTU1YmEyODqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZk5VA2d0aU5VBWZlY2hhTlUOdGlwb19wcm9waWVkYWROVQpvcmdhbml6YWRvTnUu\n','2012-08-08 02:18:24'),('06c2626fdc1f3526765280337dbd08a4','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-08-09 17:54:17'),('be8eaa375e64817fdcb303c0aa292272','NTgwZDg5NjU5NWQwNGQxNWZhOGU1MzM4ZjQxNWRhMWU5MmE2NzAwMjqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-08-09 17:54:19'),('076e7b899d938aa5bbc58a17058e8107','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-08-10 16:58:34'),('c74fb1cf6c38da82522e313bfc288b5a','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-08-10 19:48:21'),('ad1a7431a3db9bee732d71efd6d22c31','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-08-12 14:20:35'),('78f35da21d1f63bf14b77b09fc391e3f','NTgwZDg5NjU5NWQwNGQxNWZhOGU1MzM4ZjQxNWRhMWU5MmE2NzAwMjqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-08-12 14:20:40'),('4ec73fa056d277b899b44fb027427e4d','MDRmMTliM2NiMDBmYTEyZDljMTU1YTgzYmMwZTg1MjQ0OTZkNzZkMDqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZmNkamFuZ28uZGIubW9kZWxzLmJhc2UKbW9kZWxfdW5waWNrbGUKcQJjYm9zcXVlcy5t\nb2RlbHMKVGlwb0Jvc3F1ZVVtZgpxA11jZGphbmdvLmRiLm1vZGVscy5iYXNlCnNpbXBsZV9jbGFz\nc19mYWN0b3J5CnEEh1JxBX1xBihVBm5vbWJyZXEHWBMAAABCb3NxdWUgZGUgbWFuZ2xhcmVzVQZf\nc3RhdGVxCGNkamFuZ28uZGIubW9kZWxzLmJhc2UKTW9kZWxTdGF0ZQpxCSmBcQp9cQsoVQZhZGRp\nbmdxDIlVAmRicQ1VB2RlZmF1bHRxDnViVQJpZHEPigEEdWJVA2d0aVgAAAAAVQVmZWNoYVgEAAAA\nMjAxMnEQVQ50aXBvX3Byb3BpZWRhZE5VCm9yZ2FuaXphZG9OdS4=\n','2012-08-12 19:13:24'),('bab453f7328cd2313efe1817fbffb865','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-08-13 13:47:01'),('e067ed1a6ee03f8d8a9771a3d2515511','NTgwZDg5NjU5NWQwNGQxNWZhOGU1MzM4ZjQxNWRhMWU5MmE2NzAwMjqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-08-13 13:47:04'),('9f0cf3a242749898964e26039bc33db3','MmQ5ZGQxMDI4YjU2MDc5Nzc3NGMxNmMyNTcxYmU2NTVkOTU1YmEyODqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZk5VA2d0aU5VBWZlY2hhTlUOdGlwb19wcm9waWVkYWROVQpvcmdhbml6YWRvTnUu\n','2012-08-13 17:08:03'),('744a0bb19a9c3a130b0ef661c544eb79','ZjFhNmUwY2NiZjMyNTMxMWVlZmQ1MTM5N2U3NTQ0OTc3YmQyYTIyNDqAAn1xAShVDV9hdXRoX3Vz\nZXJfaWSKAQJVA2d0aVgAAAAAVQVmZWNoYVgEAAAAMjAxMnECVRJfYXV0aF91c2VyX2JhY2tlbmRV\nKWRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kVQ50aXBvX3Byb3BpZWRh\nZE5VD3RpcG9fYm9zcXVlX3VtZk5VCm9yZ2FuaXphZG9OdS4=\n','2012-08-13 16:54:24'),('7c655893cb0bd29742d9592608680275','MmQ5ZGQxMDI4YjU2MDc5Nzc3NGMxNmMyNTcxYmU2NTVkOTU1YmEyODqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZk5VA2d0aU5VBWZlY2hhTlUOdGlwb19wcm9waWVkYWROVQpvcmdhbml6YWRvTnUu\n','2012-08-14 16:13:01'),('36b35c5f934cbaf38c7274c94e973e77','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-08-15 01:50:30'),('955fcd78a7ccd72dff2ac64c116928ba','N2ZmNjQzMTYxMjliZjg5ZTJjMDgyMDU4MjJjZDdhZDdjYzUzZWU0NTqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2012-08-14 16:28:17'),('c5a7a8e5d73c83e470c5beaddf9720d8','MmIyYzFjZDNjMjZiM2M2NDBiMmM0MjZjMWFmNTU5MTRlZWRiMGRiMDqAAn1xAShVA2d0aXECTlUF\nZmVjaGFxA05VCnRlc3Rjb29raWVVBndvcmtlZFUOdGlwb19wcm9waWVkYWRxBE5VD3RpcG9fYm9z\ncXVlX3VtZnEFTlUKb3JnYW5pemFkb3EGTnUu\n','2012-08-15 14:25:06'),('49eefa20e6129caac8b6174a3b2c4276','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-08-16 16:57:01'),('6f1db60735c8a62bbf08f63c908f22c0','NTgwZDg5NjU5NWQwNGQxNWZhOGU1MzM4ZjQxNWRhMWU5MmE2NzAwMjqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-08-16 16:57:05'),('9a7dfc9d0e97995333228292eccb9e1b','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-08-17 06:38:02'),('4488df0d94d4485c34edbcdcbd2a7cc2','NTgwZDg5NjU5NWQwNGQxNWZhOGU1MzM4ZjQxNWRhMWU5MmE2NzAwMjqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-08-17 13:45:45'),('079f4ef31000858af8ce349fa49ea87c','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-08-17 13:45:47'),('9232466138fd0d783ca7930b63e23590','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-08-18 14:57:52'),('ac7a08c9eeb7758a90465f8d5c76d9d2','Y2IxNDUxYmQ3OWVkMmQ4NjgzMzY0ZjlhNTM0MzBkMmJlYjU2MWM1YTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZk5VA2d0aVgAAAAAVQVmZWNoYVgEAAAAMjAxMnECVQ50aXBvX3Byb3BpZWRhZE5VCm9y\nZ2FuaXphZG9OdS4=\n','2012-08-18 16:42:58'),('641930c49fb8be1ac5456652963ddb18','NTgwZDg5NjU5NWQwNGQxNWZhOGU1MzM4ZjQxNWRhMWU5MmE2NzAwMjqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-08-19 13:11:48'),('cb5d1c4305b898115617765229b13f93','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-08-19 13:11:50'),('54062537bacb8794cd6b47289df1a7df','MmQ5ZGQxMDI4YjU2MDc5Nzc3NGMxNmMyNTcxYmU2NTVkOTU1YmEyODqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZk5VA2d0aU5VBWZlY2hhTlUOdGlwb19wcm9waWVkYWROVQpvcmdhbml6YWRvTnUu\n','2012-08-19 13:46:53'),('757a4e8190689b9d209cdbab39bf2cca','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-08-19 15:20:01'),('7ba2ea15d39b194af24d8e033f7d4585','NTgwZDg5NjU5NWQwNGQxNWZhOGU1MzM4ZjQxNWRhMWU5MmE2NzAwMjqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-08-19 15:24:46'),('f6229144745ea9a201e5259436d19ef5','MmQ5ZGQxMDI4YjU2MDc5Nzc3NGMxNmMyNTcxYmU2NTVkOTU1YmEyODqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZk5VA2d0aU5VBWZlY2hhTlUOdGlwb19wcm9waWVkYWROVQpvcmdhbml6YWRvTnUu\n','2012-08-19 18:53:30'),('712e853b278fc9b1df56c3dd2ab3d4ca','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-08-20 13:35:54'),('4acd5d5e5df0bfc02a90b7edbe19b4ca','NTgwZDg5NjU5NWQwNGQxNWZhOGU1MzM4ZjQxNWRhMWU5MmE2NzAwMjqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-08-20 13:35:57'),('ffcefc4438f2b8ed8947799f33b8539d','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-08-20 18:26:48'),('2ee861ce37cdd9b399444382a9406b4b','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-08-20 21:21:03'),('b62671af2c25ca2a1ca1e7e8fb118ec5','NTgwZDg5NjU5NWQwNGQxNWZhOGU1MzM4ZjQxNWRhMWU5MmE2NzAwMjqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-08-21 02:52:33'),('03f87b3a0effe73bdc68d736fb9627df','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-08-21 13:56:01'),('3ab9dd2722e2c51fbac1b0a07b5bb07d','NTgwZDg5NjU5NWQwNGQxNWZhOGU1MzM4ZjQxNWRhMWU5MmE2NzAwMjqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-08-21 13:56:03'),('92e3896a1c94e28e234ae007bcc0737a','NTgwZDg5NjU5NWQwNGQxNWZhOGU1MzM4ZjQxNWRhMWU5MmE2NzAwMjqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-08-22 14:06:39'),('4d5bbdc154746916f54037ad27d8c3ad','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-08-22 14:06:43'),('1f3cd53ba69a3b7bb4939e738f7d0885','NTgwZDg5NjU5NWQwNGQxNWZhOGU1MzM4ZjQxNWRhMWU5MmE2NzAwMjqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-08-23 14:02:19'),('d63bb2e1976b3e33e9bfad6c5950b3f4','MTQ3MmJkMmY1NzViMjRjZDMzMGZlZTUzZDhjYzRkODk0ZDU4ZWI3YzqAAn1xAShVDV9hdXRoX3Vz\nZXJfaWSKAQFVA2d0aU5VBWZlY2hhTlUSX2F1dGhfdXNlcl9iYWNrZW5kVSlkamFuZ28uY29udHJp\nYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZFUOdGlwb19wcm9waWVkYWROVQ90aXBvX2Jvc3F1\nZV91bWZOVQpvcmdhbml6YWRvTnUu\n','2012-08-22 21:53:31'),('86883403da335a72893c3ea007ac8301','YmYwYWEyM2JiZDQwZTc0YzUzNmJmNmZiZTk4ZGY1ZWVhOTU0N2Q5ZTqAAn1xAShVD3RpcG9fYm9z\ncXVlX3VtZnECTlUDZ3RpcQNOVQVmZWNoYXEETlUOdGlwb19wcm9waWVkYWRxBU5VCm9yZ2FuaXph\nZG9xBk51Lg==\n','2012-08-23 14:02:22'),('9ba32f1e1f4b4202a085e6e991d91e85','N2ZmNjQzMTYxMjliZjg5ZTJjMDgyMDU4MjJjZDdhZDdjYzUzZWU0NTqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2012-08-24 21:18:15');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lugar_comunidad`
--

DROP TABLE IF EXISTS `lugar_comunidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lugar_comunidad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `municipio_id` int(11) NOT NULL,
  `nombre` varchar(40) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lugar_comunidad_f3143aaa` (`municipio_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lugar_comunidad`
--

LOCK TABLES `lugar_comunidad` WRITE;
/*!40000 ALTER TABLE `lugar_comunidad` DISABLE KEYS */;
INSERT INTO `lugar_comunidad` VALUES (1,1035,'Aranjuez'),(2,550,'Soledad'),(3,9315,'Pueblo Nuevo');
/*!40000 ALTER TABLE `lugar_comunidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lugar_departamento`
--

DROP TABLE IF EXISTS `lugar_departamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lugar_departamento` (
  `id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `slug` varchar(50) DEFAULT NULL,
  `extension` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lugar_departamento`
--

LOCK TABLES `lugar_departamento` WRITE;
/*!40000 ALTER TABLE `lugar_departamento` DISABLE KEYS */;
INSERT INTO `lugar_departamento` VALUES (5,'Nueva Segovia','Nueva-segovia','3491.28'),(10,'Jinotega','jinotega','9222.40'),(20,'Madriz','madriz','1708.23'),(25,'Estelí','esteli','2229.69'),(30,'Chinandega','chinandega','4822.46'),(35,'León','leon','5138.03'),(40,'Matagalpa','matagalpa','6803.86'),(50,'Boaco','boaco','4176.68'),(55,'Managua','managua','3465.10'),(60,'Masaya','masaya','610.78'),(65,'Chontales','chontales','6481.27'),(70,'Granada','granada','1039.68'),(75,'Carazo','carazo','1081.40'),(80,'Rivas','rivas','2161.82'),(85,'Rí­o San Juan','Rio-san-juan','7540.90'),(91,'RAAN','RAAN','32819.68'),(93,'RAAS','RAAS','27546.32'),(99,'Cobertura Nacional','cobertura-nacional','333333.00');
/*!40000 ALTER TABLE `lugar_departamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lugar_municipio`
--

DROP TABLE IF EXISTS `lugar_municipio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lugar_municipio` (
  `id` int(11) NOT NULL,
  `departamento_id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `slug` varchar(50) DEFAULT NULL,
  `extension` decimal(10,2) DEFAULT NULL,
  `latitud` decimal(8,5) DEFAULT NULL,
  `longitud` decimal(8,5) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  UNIQUE KEY `slug` (`slug`),
  KEY `lugar_municipio_8865b15a` (`departamento_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lugar_municipio`
--

LOCK TABLES `lugar_municipio` WRITE;
/*!40000 ALTER TABLE `lugar_municipio` DISABLE KEYS */;
INSERT INTO `lugar_municipio` VALUES (505,5,'Jalapa','jalapa','0.00','13.92286','-86.12520'),(510,5,'Murra','murra','0.00','13.75900','-86.01799'),(515,5,'El Jí­caro','El-jicaro','0.00','13.72326','-86.13705'),(520,5,'San Fernando','San-fernando','0.00','13.67729','-86.31484'),(525,5,'Mozonte','mozonte','0.00','13.66168','-86.43706'),(530,5,'Dipilto','dipilto','0.00','13.72243','-86.50720'),(535,5,'Macuelizo','macuelizo','0.00','13.65239','-86.61380'),(540,5,'Santa Marí­a','santamaria','0.00','13.74753','-86.71077'),(545,5,'Ocotal','ocotal','0.00','13.63432','-86.47745'),(550,5,'Ciudad Antigua','Ciudad-antigua','0.00','13.64217','-86.30893'),(555,5,'Quilalí','quilali','0.00','13.56675','-86.02952'),(560,5,'Wiwili de Nueva Segovia','Wiwili-nuevasegovia','0.00','13.62667','-85.82369'),(1005,10,'Wiwilí','Wiwili','0.00','13.62130','-85.81864'),(1010,10,'El Cúa','El-cua','0.00','13.36764','-85.67330'),(1012,10,'San José Bocay','San-jose-bocay','0.00','13.61976','-85.50080'),(1015,10,'Sta. María de Pantasma','Santa-maria-pantasma','0.00','13.36667','-85.95000'),(1020,10,'San Rafael del Norte','San-rafael-del-norte','0.00','13.21391','-86.11043'),(1025,10,'San Sebastian de Yalí','yali','0.00','13.30500','-86.18636'),(1030,10,'La Concordia','La-concordia','0.00','13.19535','-86.16693'),(1035,10,'Jinotega','jinotega','0.00','13.09165','-86.00121'),(2005,20,'Somoto','somoto','0.00','13.48129','-86.58337'),(2010,20,'Totogalpa','totogalpa','0.00','13.56336','-86.49281'),(2015,20,'Telpaneca','telpaneca','0.00','13.53131','-86.28693'),(2020,20,'San Juan de Río Coco','San-juan-rio-coco','0.00','13.54458','-86.16537'),(2025,20,'Palacaguina','palacaguina','0.00','13.45597','-86.40710'),(2030,20,'Yalaguina','yalaguina','0.00','13.48351','-86.49344'),(2035,20,'San Lucas','San-lucas','0.00','13.41358','-86.61176'),(2040,20,'Las Sabanas','Las-sabanas','0.00','13.34324','-86.62194'),(2045,20,'San José de Cusmapa','San-jose-cusmapa','0.00','13.28847','-86.65489'),(2505,25,'Pueblo Nuevo','Pueblo-nuevo','0.00','13.37937','-86.48077'),(2510,25,'Condega','condega','0.00','13.36213','-86.39789'),(2515,25,'Estelí','esteli','0.00','13.08948','-86.35551'),(2520,25,'San Juan de Limay','Sanjuan-limay','0.00','13.17489','-86.61234'),(2525,25,'La Trinidad','trinidad','0.00','12.96823','-86.23604'),(2530,25,'San Nicolás','San-nicolas','0.00','12.93312','-86.34700'),(3005,30,'San Pedro del Norte','San-pedro-del-norte','0.00','13.27596','-86.87777'),(3010,30,'San Francisco del Norte','San-francisco-del-norte','0.00','13.20016','-86.77192'),(3015,30,'Cinco Pinos','Cinco-pinos','0.00','13.23036','-86.86719'),(3020,30,'Santo Tomás del Norte','Santo-tomas-del-norte','0.00','13.18701','-86.92352'),(3025,30,'El Viejo','El-viejo','0.00','12.66228','-87.16541'),(3030,30,'Pto. Morazán','Puerto-morazan','0.00','12.76721','-87.13388'),(3035,30,'Somotillo','somotillo','0.00','13.04495','-86.90499'),(3040,30,'Villanueva','villanueva','0.00','12.96391','-86.81468'),(3045,30,'Chinandega','chinandega','0.00','12.62872','-87.13149'),(3050,30,'El Realejo','El-realejo','0.00','12.54551','-87.16736'),(3055,30,'Corinto','corinto','0.00','12.48461','-87.17122'),(3060,30,'Chichigalpa','chichigalpa','0.00','12.57224','-87.02849'),(3065,30,'Posoltega','posotelga','0.00','12.54410','-86.98010'),(3505,35,'Achuapa','achuapa','0.00','13.05433','-86.59070'),(3510,35,'El Sauce','El-sauce','0.00','12.88694','-86.53952'),(3515,35,'Santa Rosa del Peñon','Santa-rosa-del-penon','0.00','12.80142','-86.37144'),(3520,35,'El Jicaral','El-jicaral','0.00','12.72672','-86.38134'),(3525,35,'Larreynaga','larreynaga','0.00','12.59311','-86.68015'),(3530,35,'Telica','telica','0.00','12.52152','-86.86030'),(3535,35,'Quezalguaque','quezalguaque','0.00','12.50614','-86.90366'),(3540,35,'León','leon','0.00','12.43481','-86.88174'),(3545,35,'La Paz Centro','La-paz-centro','0.00','12.34011','-86.67625'),(3550,35,'Nagarote','nagarote','0.00','12.26531','-86.56812'),(4005,40,'Rancho Grande','Rancho-grande','0.00','13.25352','-85.55268'),(4010,40,'Rí­o Blanco','Rio-blanco','0.00','12.93044','-85.22610'),(4015,40,'El Tuma - La Dalia','El-tuma','0.00','13.13735','-85.73788'),(4020,40,'San Isidro','San-isidro','0.00','12.92937','-86.19550'),(4025,40,'Sébaco','sebaco','0.00','12.85190','-86.09696'),(4030,40,'Matagalpa','matagalpa','0.00','12.92709','-85.91747'),(4035,40,'San Ramón','San-ramon','0.00','12.92254','-85.83968'),(4040,40,'Matiguás','matiguas','0.00','12.83710','-85.46079'),(4045,40,'Muy Muy','muymuy','0.00','12.76125','-85.63123'),(4050,40,'Esquipulas','esquipulas','0.00','12.66446','-85.78909'),(4055,40,'San Dionisio','San-dionisio','0.00','12.76190','-85.85091'),(4060,40,'Terrabona','terrabona','0.00','12.73009','-85.96487'),(4065,40,'Ciudad Darí­o','Ciudad-dario','0.00','12.73000','-86.12457'),(5005,50,'San José de los Remates','San-jose-de-los-remates','0.00','12.59748','-85.76253'),(5010,50,'Boaco','boaco','0.00','12.47160','-85.65952'),(5015,50,'Camoapa','camoapa','0.00','12.38377','-85.51465'),(5020,50,'Santa Lucía','Santa-lucia','0.00','12.53226','-85.71156'),(5025,50,'Teustepe','teustepe','0.00','12.41979','-85.79922'),(5030,50,'San  Lorenzo','San-lorenzo','0.00','12.37789','-85.66718'),(5505,55,'San Francisco Libre','San-francisco-libre','0.00','12.50458','-86.30105'),(5510,55,'Tipitapa','tipitapa','0.00','12.19662','-86.09682'),(5515,55,'Mateare','mateare','0.00','12.23536','-86.43013'),(5520,55,'Villa Carlos Fonseca','Villa-carlos-fonseca','0.00','11.97924','-86.50809'),(5522,55,'Ciudad Sandino','Ciudad-sandino','0.00','12.16082','-86.35004'),(5525,55,'Managua','managua','0.00','12.14746','-86.27339'),(5530,55,'Ticuantepe','ticuantepe','0.00','12.02125','-86.20288'),(5532,55,'El Crucero','El-crucero','0.00','11.97865','-86.31076'),(5535,55,'San Rafael del Sur','San-rafael-del-sur','0.00','11.84681','-86.43977'),(6005,60,'Nindirí','nindiri','0.00','12.00243','-86.12067'),(6010,60,'Masaya','masaya','0.00','11.97735','-86.09606'),(6015,60,'Tisma','tisma','0.00','12.08133','-86.01921'),(6020,60,'La Concepción','La-concepcion','0.00','11.93615','-86.19220'),(6025,60,'Masatepe','masatepe','0.00','11.91344','-86.14475'),(6030,60,'Nandasmo','nandasmo','0.00','11.90933','-86.13055'),(6035,60,'Catarina','catarina','0.00','11.91078','-86.07407'),(6040,60,'San Juan de Oriente','San-juan-de-oriente','0.00','11.90479','-86.07311'),(6045,60,'Niquinohomo','niquinomo','0.00','11.90408','-86.09472'),(6505,65,'Comalapa','comalapa','0.00','12.28340','-85.51142'),(6507,65,'San Francisco Cuapa','San-francisco-cuapa','0.00','12.26671','-85.38308'),(6510,65,'Juigalpa','juigalpa','0.00','12.10580','-85.36842'),(6515,65,'La Libertad','La-libertad','0.00','12.21539','-85.16549'),(6520,65,'Santo Domingo','Santo-domingo','0.00','12.26301','-85.08232'),(6525,65,'Santo Tomás','Santo-tomas','0.00','12.06902','-85.09340'),(6530,65,'San Pedro de Lóvago','San-pedro-de-lovago','0.00','12.12852','-85.11572'),(6535,65,'Acoyapa','acoyapa','0.00','11.96764','-85.17044'),(6540,65,'Villa Sandino','Villa-sandino','0.00','12.04779','-84.99334'),(6545,65,'El Coral','El-coral','0.00','11.91576','-84.65041'),(7005,70,'Diriá','diria','0.00','11.88416','-86.05565'),(7010,70,'Diriomo','diriomo','0.00','11.87494','-86.05110'),(7015,70,'Granada','granada','0.00','11.93095','-85.95696'),(7020,70,'Nandaime','nandaime','0.00','11.75630','-86.05345'),(7505,75,'San Marcos','San-marcos','0.00','11.90651','-86.20314'),(7510,75,'Jinotepe','jinotepe','0.00','11.84831','-86.19846'),(7515,75,'Dolores','dolores','0.00','11.85565','-86.21535'),(7520,75,'Diriamba','diriamba','0.00','11.85572','-86.24074'),(7525,75,'El Rosario','El-rosario','0.00','11.83224','-86.16484'),(7530,75,'La Paz de Carazo','La-paz-de-carazo','0.00','11.82206','-86.12750'),(7535,75,'Santa Teresa','Santa-tereza','0.00','11.80272','-86.16281'),(7540,75,'La Conquista','La-conquista','0.00','11.73336','-86.19297'),(8005,80,'Tola','tola','0.00','11.43868','-85.93907'),(8010,80,'Belén','belen','0.00','11.50081','-85.89014'),(8015,80,'Potosí','potosi','0.00','11.49320','-85.85709'),(8020,80,'Buenos Aires','Buenos-aires','0.00','11.46923','-85.81701'),(8025,80,'Moyogalpa','moyogalpa','0.00','11.53947','-85.69746'),(8030,80,'Altagracia','altagracia','0.00','11.56547','-85.57793'),(8035,80,'San Jorge','San-jorge','0.00','11.45532','-85.80074'),(8040,80,'Rivas','rivas','0.00','11.43975','-85.82880'),(8045,80,'San Juan del Sur','San-juan-del-sur','0.00','11.25384','-85.87177'),(8050,80,'Cárdenas','cardenas','0.00','11.19521','-85.50886'),(8505,85,'Morrito','morrito','0.00','11.62130','-85.08169'),(8510,85,'El Almendro','El-almendro','0.00','11.67684','-84.70362'),(8515,85,'San Miguelito','San-miguelito','0.00','11.40156','-84.90005'),(8520,85,'San Carlos','San-carlos','0.00','11.12088','-84.77837'),(8525,85,'El Castillo','El-castillo','0.00','11.03969','-84.47295'),(8530,85,'San Juan del Norte','San-juan-del-norte','0.00','10.94671','-83.73479'),(9105,91,'Waspán','waspan','0.00','14.74386','-83.96885'),(9110,91,'Puerto Cabezas','Puerto-cabezas','0.00','14.03313','-83.38223'),(9115,91,'Rosita','rosita','0.00','13.91060','-84.39153'),(9120,91,'Bonanza','bonanza','0.00','14.02584','-84.62088'),(9127,91,'Mulukuku','mulukuku','0.00','13.15000','-84.96667'),(9125,91,'Waslala','waslala','0.00','13.33465','-85.37099'),(9130,91,'Siuna','siuna','0.00','13.73857','-84.78491'),(9135,91,'Prinzapolka','prinzapolka','0.00','13.40611','-83.56229'),(9305,93,'Paiwas','paiwas','0.00','12.78548','-85.12402'),(9310,93,'La Cruz de Río Grande','La-cruz-rio-grande','0.00','13.11145','-84.18835'),(9312,93,'Desembocadura de Río Grande','Desembocadura-rio-grande','0.00','12.93208','-83.57697'),(9315,93,'Laguna de Perlas','Laguna-de-perlas','0.00','12.34096','-83.67052'),(9316,93,'El Tortuguero','El-tortuguero','0.00','12.82085','-84.19906'),(9320,93,'Rama','rama','0.00','12.16004','-84.21913'),(9323,93,'El Ayote','El-ayote','0.00','12.49486','-84.81943'),(9325,93,'Muelle de los Bueyes','Muelle-de-los-bueyes','0.00','12.06764','-84.53749'),(9330,93,'Kukra - Hill','Kukra-hill','0.00','12.24163','-83.74532'),(9335,93,'Corn Island','Corn-island','0.00','12.18017','-83.05975'),(9340,93,'Bluefields','bluefields','0.00','12.01144','-83.76388'),(9345,93,'Nueva Guinea','Nueva-guinea','0.00','11.68827','-84.45794'),(1040,10,'Altowangky','altowanky','0.00',NULL,NULL);
/*!40000 ALTER TABLE `lugar_municipio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `south_migrationhistory`
--

DROP TABLE IF EXISTS `south_migrationhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `south_migrationhistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` varchar(255) NOT NULL,
  `migration` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `south_migrationhistory`
--

LOCK TABLES `south_migrationhistory` WRITE;
/*!40000 ALTER TABLE `south_migrationhistory` DISABLE KEYS */;
INSERT INTO `south_migrationhistory` VALUES (1,'lugar','0001_initial','2012-07-13 19:25:04'),(2,'bosques','0001_initial','2012-07-13 19:25:04');
/*!40000 ALTER TABLE `south_migrationhistory` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2012-08-10 17:17:49
