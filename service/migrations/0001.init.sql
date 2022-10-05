--
-- file: migrations/0001.init.sql
--
CREATE TABLE `logs` (
  `id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `branch` text NOT NULL,
  `name` text NOT NULL,
  `resourceVersion` text NOT NULL,
  `state` text NOT NULL,
  `created_at` timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);