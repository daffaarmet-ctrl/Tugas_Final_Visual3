-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 28, 2025 at 03:34 AM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbvisual3_2310010120`
--

-- --------------------------------------------------------

--
-- Table structure for table `data_gaji`
--

CREATE TABLE `data_gaji` (
  `id_gaji` varchar(10) NOT NULL,
  `id_karyawan` varchar(10) DEFAULT NULL,
  `tanggal_gaji` date DEFAULT NULL,
  `kategori` varchar(50) DEFAULT NULL,
  `jumlah_gaji` bigint UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `data_gaji`
--

INSERT INTO `data_gaji` (`id_gaji`, `id_karyawan`, `tanggal_gaji`, `kategori`, `jumlah_gaji`) VALUES
('1', 'K001', '2000-01-01', 'Mingguan', 30000),
('G001', 'K001', '2024-04-30', 'Bulanan', 400000),
('G002', 'K002', '2024-04-30', 'Bulanan', 520000),
('G003', 'K003', '2024-04-30', 'Bulanan', 300000);

-- --------------------------------------------------------

--
-- Table structure for table `data_inventory`
--

CREATE TABLE `data_inventory` (
  `id_barang` varchar(10) NOT NULL,
  `nama_barang` varchar(100) DEFAULT NULL,
  `kategori` varchar(50) DEFAULT NULL,
  `satuan` varchar(20) DEFAULT NULL,
  `jumlah` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `data_inventory`
--

INSERT INTO `data_inventory` (`id_barang`, `nama_barang`, `kategori`, `satuan`, `jumlah`) VALUES
('B001', 'Pupuk A', 'Pupuk', 'Kg', 100),
('B002', 'Sarung Tangan', 'Peralatan', 'Pcs', 50),
('B003', 'Pestisida', 'Obat', 'Botol', 30);

-- --------------------------------------------------------

--
-- Table structure for table `data_karyawan`
--

CREATE TABLE `data_karyawan` (
  `id_karyawan` varchar(10) NOT NULL,
  `nama_karyawan` varchar(100) DEFAULT NULL,
  `alamat` varchar(150) DEFAULT NULL,
  `umur` int DEFAULT NULL,
  `no_telp` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `data_karyawan`
--

INSERT INTO `data_karyawan` (`id_karyawan`, `nama_karyawan`, `alamat`, `umur`, `no_telp`) VALUES
('K001', 'Bambang', 'Desa A', 32, '08123456789'),
('K002', 'Indira', 'Desa B', 28, '082233445566'),
('K003', 'Sari', 'Desa C', 30, '08333445566');

-- --------------------------------------------------------

--
-- Table structure for table `data_panen`
--

CREATE TABLE `data_panen` (
  `id_panen` varchar(10) NOT NULL,
  `id_karyawan` varchar(10) DEFAULT NULL,
  `tanggal_panen` date DEFAULT NULL,
  `hasil_panen` int DEFAULT NULL,
  `total_panen` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `data_panen`
--

INSERT INTO `data_panen` (`id_panen`, `id_karyawan`, `tanggal_panen`, `hasil_panen`, `total_panen`) VALUES
('1', 'K001', '2000-01-01', 3, 30000),
('2', 'K001', '2000-01-03', 1, 10000),
('3', 'K001', '2000-01-14', 2, 20000),
('P001', 'K001', '2024-04-20', 10, 100000),
('P002', 'K001', '2024-04-24', 30, 300000),
('P003', 'K002', '2024-04-15', 20, 200000),
('P004', 'K002', '2024-04-25', 32, 320000),
('P005', 'K003', '2024-04-18', 12, 120000),
('P006', 'K003', '2024-04-26', 18, 180000);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `data_gaji`
--
ALTER TABLE `data_gaji`
  ADD PRIMARY KEY (`id_gaji`),
  ADD KEY `id_karyawan` (`id_karyawan`);

--
-- Indexes for table `data_inventory`
--
ALTER TABLE `data_inventory`
  ADD PRIMARY KEY (`id_barang`);

--
-- Indexes for table `data_karyawan`
--
ALTER TABLE `data_karyawan`
  ADD PRIMARY KEY (`id_karyawan`);

--
-- Indexes for table `data_panen`
--
ALTER TABLE `data_panen`
  ADD PRIMARY KEY (`id_panen`),
  ADD KEY `id_karyawan` (`id_karyawan`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `data_gaji`
--
ALTER TABLE `data_gaji`
  ADD CONSTRAINT `data_gaji_ibfk_1` FOREIGN KEY (`id_karyawan`) REFERENCES `data_karyawan` (`id_karyawan`);

--
-- Constraints for table `data_panen`
--
ALTER TABLE `data_panen`
  ADD CONSTRAINT `data_panen_ibfk_1` FOREIGN KEY (`id_karyawan`) REFERENCES `data_karyawan` (`id_karyawan`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
