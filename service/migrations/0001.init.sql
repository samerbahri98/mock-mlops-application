--
-- file: migrations/0001.init.sql
--
CREATE TABLE `logs` (
  `id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `branch` varchar(50) NOT NULL DEFAULT 'main',
  `name` varchar(50) NOT NULL,
  `resourceVersion` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `created_at` timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);