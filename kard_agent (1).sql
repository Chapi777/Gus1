-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Апр 11 2023 г., 12:04
-- Версия сервера: 8.0.29
-- Версия PHP: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `kard_agent`
--

-- --------------------------------------------------------

--
-- Структура таблицы `doljnost`
--

CREATE TABLE `doljnost` (
  `id_dolj` int NOT NULL,
  `name_dolj` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `doljnost`
--

INSERT INTO `doljnost` (`id_dolj`, `name_dolj`) VALUES
(1, 'Frontend_разработчик'),
(2, 'Backend_программист'),
(3, 'Разработчик мобильных приложений'),
(4, 'Системный программист'),
(5, 'Разработчик игр'),
(6, 'Программист 1С');

-- --------------------------------------------------------

--
-- Структура таблицы `level_vlad_comp`
--

CREATE TABLE `level_vlad_comp` (
  `id_levc` int NOT NULL,
  `name_levc` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `level_vlad_comp`
--

INSERT INTO `level_vlad_comp` (`id_levc`, `name_levc`) VALUES
(1, 'Начальный'),
(2, 'Базовый'),
(3, 'Опытный'),
(4, 'Профессиональный');

-- --------------------------------------------------------

--
-- Структура таблицы `obrazovanie`
--

CREATE TABLE `obrazovanie` (
  `id_obraz` int NOT NULL,
  `name_obraz` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `obrazovanie`
--

INSERT INTO `obrazovanie` (`id_obraz`, `name_obraz`) VALUES
(1, 'Высшее'),
(2, 'Высшее специальное'),
(3, 'Начальное профессиональное'),
(4, 'Среднее'),
(5, 'Неоконченное среднее / высшее');

-- --------------------------------------------------------

--
-- Структура таблицы `profesion`
--

CREATE TABLE `profesion` (
  `id_profs` int NOT NULL,
  `name_profs` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `profesion`
--

INSERT INTO `profesion` (`id_profs`, `name_profs`) VALUES
(1, 'Программист'),
(2, 'Системный администратор'),
(3, 'Бугалтер');

-- --------------------------------------------------------

--
-- Структура таблицы `vakansia`
--

CREATE TABLE `vakansia` (
  `id_vak` int NOT NULL,
  `data_opubl` date NOT NULL,
  `kod_dolj` int NOT NULL,
  `actual` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `kod_profs` int NOT NULL,
  `kod_obraz` int NOT NULL,
  `kod_levc` int NOT NULL,
  `FIO` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `doljnost`
--
ALTER TABLE `doljnost`
  ADD PRIMARY KEY (`id_dolj`);

--
-- Индексы таблицы `level_vlad_comp`
--
ALTER TABLE `level_vlad_comp`
  ADD PRIMARY KEY (`id_levc`);

--
-- Индексы таблицы `obrazovanie`
--
ALTER TABLE `obrazovanie`
  ADD PRIMARY KEY (`id_obraz`);

--
-- Индексы таблицы `profesion`
--
ALTER TABLE `profesion`
  ADD PRIMARY KEY (`id_profs`);

--
-- Индексы таблицы `vakansia`
--
ALTER TABLE `vakansia`
  ADD PRIMARY KEY (`id_vak`),
  ADD KEY `kod_profs` (`kod_profs`,`kod_obraz`,`kod_levc`),
  ADD KEY `kod_levc` (`kod_levc`),
  ADD KEY `kod_obraz` (`kod_obraz`),
  ADD KEY `kod_dolj` (`kod_dolj`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `doljnost`
--
ALTER TABLE `doljnost`
  MODIFY `id_dolj` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT для таблицы `level_vlad_comp`
--
ALTER TABLE `level_vlad_comp`
  MODIFY `id_levc` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `obrazovanie`
--
ALTER TABLE `obrazovanie`
  MODIFY `id_obraz` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `profesion`
--
ALTER TABLE `profesion`
  MODIFY `id_profs` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `vakansia`
--
ALTER TABLE `vakansia`
  MODIFY `id_vak` int NOT NULL AUTO_INCREMENT;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `vakansia`
--
ALTER TABLE `vakansia`
  ADD CONSTRAINT `vakansia_ibfk_1` FOREIGN KEY (`kod_profs`) REFERENCES `profesion` (`id_profs`),
  ADD CONSTRAINT `vakansia_ibfk_2` FOREIGN KEY (`kod_levc`) REFERENCES `level_vlad_comp` (`id_levc`),
  ADD CONSTRAINT `vakansia_ibfk_3` FOREIGN KEY (`kod_obraz`) REFERENCES `obrazovanie` (`id_obraz`),
  ADD CONSTRAINT `vakansia_ibfk_4` FOREIGN KEY (`kod_dolj`) REFERENCES `doljnost` (`id_dolj`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
