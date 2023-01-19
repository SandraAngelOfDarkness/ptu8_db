-- SQLite
SELECT * FROM DARBUOTOJAS;
SELECT * FROM PROJEKTAS;
SELECT * FROM SKYRIUS;

--Išrinkite darbuotojų vardus ir pavardes kartu su projekto pavadinimu, kuriame jie dirba.
SELECT VARDAS, PAVARDĖ, PROJEKTAS_ID FROM DARBUOTOJAS;
--Išsirinkite darbuotojų dirbančių projekte Galerija vardus, pavardes ir projekto pavadinimą.
SELECT VARDAS, PAVARDĖ, PROJEKTAS_ID FROM DARBUOTOJAS
    JOIN PROJEKTAS ON DARBUOTOJAS.PROJEKTAS_ID = PROJEKTAS.ID
    WHERE PROJEKTAS = "Galerija"
    ORDER BY VARDAS DESC;

--Išrinkite visus projekto Projektų valdymas vykdytojus dirbančius Pardavimų skyriuje.
SELECT VARDAS, PAVARDĖ FROM DARBUOTOJAS
    JOIN DARBUOTOJAS ON DARBUOTOJAS.SKYRIUS_ID = SKYRIUS.ID
    JOIN PROJEKTAS ON DARBUOTOJAS.PROJEKTAS_ID = PROJEKTAS.ID
    WHERE PROJEKTAS.PAVADINIMAS = "PROJEKTAS"; 

--Išrinkite visas moteris, dirbančias projekte Projektų valdymas ir išveskite į ekraną jų vardus, pavardes ir projekto pavadinimą.
SELECT VARDAS, PAVARDĖ, PROJEKTAS_ID FROM DARBUOTOJAS
    JOIN DARBUOTOJAS ON DARBUOTOJAS.PROJEKTAS_ID = PROJEKTAS.ID
    JOIN SKYRIUS ON DARBUOTOJAS.SKYRIUS_ID = SKYRIUS.ID
    WHERE ASMENS_KODAS LIKE "4%" OR ASMENS_KODAS LIKE "6%" AND PROJEKTAS = "projektu valdymas";

--+Išrinkite skyrių pavadinimus su juose dirbančių darbuotojų skaičiumi.
SELECT SKYRIUS.PAVADINIMAS, count(*) AS count
    FROM DARBUOTOJAS
    JOIN SKYRIUS 
    ON DARBUOTOJAS.SKYRIUS_ID = SKYRIUS.ID
    GROUP BY SKYRIUS.PAVADINIMAS;
--+Apribokite #5 užklausos rezultatą taip, kad rodytų tik tuos skyrius kur dirba bent 5 darbuotojai.
SELECT SKYRIUS.PAVADINIMAS, count(*) as count
    FROM DARBUOTOJAS
    JOIN SKYRIUS
    ON DARBUOTOJAS.SKYRIUS_ID = skyrius.ID
    GROUP BY SKYRIUS.PAVADINIMAS HAVING count() > 3;

--+Išrinkite darbuotojus (vardus, pavardes, pareigas) kartu su skyrių, kuriuose jie dirba pavadinimais, tačiau nesančius tų skyrių vadovais.
SELECT VARDAS, PAVARDĖ, PAREIGOS, SKYRIUS_ID
    FROM DARBUOTOJAS
    WHERE PAREIGOS NOT LIKE "Vadovas";

--+Sukurkite naują įrašą lentelėje “DARBUOTOJAS” (asmens kodas: 38807117896, vardas: Pranas, pavardė:Logis, Dirba nuo: 2009-11-12, visa kita - Null).
INSERT INTO DARBUOTOJAS (VARDAS, PAVARDĖ, ASMENS_KODAS, DIRBA_NUO)
    VALUES("Pranas", "Logis", "38807117896", "2009-11-12");
SELECT * FROM DARBUOTOJAS;

--+Išrinkite darbuotojų vardus, pavardes ir skyriaus pavadinimą. Rodykite, net ir tuos darbuotojus, kurie nedirba jokiame skyriuje (skyriaus pavadinimą pasiimkite iš lentelės SKYRIUS).
SELECT VARDAS, PAVARDĖ, SKYRIUS_ID
    FROM DARBUOTOJAS
    LEFT JOIN SKYRIUS
    ON DARBUOTOJAS.SKYRIUS_ID = SKYRIUS.ID;

--+1# punkto užklausą pataisykite taip, kad rodytų tik tuos vardus ir projektų pavadinimus kuriuose dirba daugiau nei 4 darbuotojai.
SELECT VARDAS, PAVARDĖ, PROJEKTAS_ID, count(*) as count
    FROM DARBUOTOJAS
    JOIN SKYRIUS
    ON DARBUOTOJAS.SKYRIUS_ID = skyrius.ID
    GROUP BY SKYRIUS.PAVADINIMAS HAVING count() > 4;

--+Naujame stulpeyje parodyti kiekvieno darbuotojo bazinio atlyginimo ir priedų sumą.
-- SELECT make, model, year, price, ROUND(price / 1.21, 2) AS price_ex_vat FROM cars;
-- SELECT sum(price), count(price) as kiekis FROM cars;
SELECT VARDAS, PAVARDĖ,
    ROUND(BAZINIS_ATLYGINIMAS + PRIEDAI, 2) as ALGA FROM DARBUOTOJAS;

--+Parodyti bendrą atlyginimų, priedų sumą, vidutinį, maksimalų, minimalų atlyginimą.
SELECT sum(BAZINIS_ATLYGINIMAS), min(BAZINIS_ATLYGINIMAS), max(BAZINIS_ATLYGINIMAS), avg(BAZINIS_ATLYGINIMAS), count(BAZINIS_ATLYGINIMAS), 
sum(PRIEDAI), min(PRIEDAI), max(PRIEDAI), avg(PRIEDAI), count(PRIEDAI) AS bendras FROM DARBUOTOJAS;