
-- Crear tabla SERIES
CREATE TABLE SERIES (
    IDSERIE NUMBER NOT NULL,
    SERIE NVARCHAR2(160),
    IMAGEN NVARCHAR2(350),
    ANYO NUMBER,
    CONSTRAINT PK_SERIES PRIMARY KEY (IDSERIE)
);

-- Crear tabla PERSONAJES
CREATE TABLE PERSONAJES (
    IDPERSONAJE NUMBER NOT NULL,
    PERSONAJE NVARCHAR2(60),
    IMAGEN NVARCHAR2(350),
    IDSERIE NUMBER,
    CONSTRAINT PK_PERSONAJES PRIMARY KEY (IDPERSONAJE)
);

INSERT INTO SERIES (IDSERIE, SERIE, IMAGEN, ANYO) VALUES (1, 'Juego de tronos', 'https://cadenaser00.epimg.net/ser/imagenes/2019/05/23/television/1558591913_020782_1558595107_noticia_normal.jpg', 2011);
INSERT INTO SERIES (IDSERIE, SERIE, IMAGEN, ANYO) VALUES (2, 'The Mandaloria', 'https://images-na.ssl-images-amazon.com/images/I/71bBDuXUvOL.jpg', 2019);
INSERT INTO SERIES (IDSERIE, SERIE, IMAGEN, ANYO) VALUES (3, 'Stranger Things', 'https://static.posters.cz/image/750/posters/stranger-things-one-sheet-season-2-i67844.jpg', 2016);
INSERT INTO SERIES (IDSERIE, SERIE, IMAGEN, ANYO) VALUES (4, 'Narcos', 'https://www.espanolavanzado.com/images/articles/spanish/narcos.jpg', 2015);
INSERT INTO SERIES (IDSERIE, SERIE, IMAGEN, ANYO) VALUES (5, 'The Boys', 'https://as01.epimg.net/epik/imagenes/2020/09/14/portada/1600093038_124653_1600093183_noticia_normal_recorte1.jpg', 2019);
INSERT INTO SERIES (IDSERIE, SERIE, IMAGEN, ANYO) VALUES (6, 'The Big Bang Theory', 'https://www.camaracivica.com/wp-content/uploads/2016/12/The-Big-Bang-Theory.jpg', 2007);
INSERT INTO SERIES (IDSERIE, SERIE, IMAGEN, ANYO) VALUES (7, 'Campeones: Oliver y Benji', 'https://www.dibujos-animados.net/wp-content/uploads/2016/11/serie-oliver-benji-campeones.jpg', 1983);
INSERT INTO SERIES (IDSERIE, SERIE, IMAGEN, ANYO) VALUES (8, 'Como conocí a vuestra madre', 'https://www.tendenciashoy.com/wp-content/uploads/2021/04/Como-conoci%CC%81-a-vuestra-madre.jpg', 2005);
INSERT INTO SERIES (IDSERIE, SERIE, IMAGEN, ANYO) VALUES (9, 'La casa de papel', 'https://s1.eestatic.com/2019/07/23/cultura/series/Netflix-Series-Ursula_Corbero-Series_415970383_130773402_1024x576.jpg', 2017);
INSERT INTO SERIES (IDSERIE, SERIE, IMAGEN, ANYO) VALUES (10, 'Futurama', 'https://i.blogs.es/5bcb58/futurama/1366_2000.jpeg', 1999);

INSERT INTO PERSONAJES (IDPERSONAJE, PERSONAJE, IMAGEN, IDSERIE) VALUES (2, 'Barney Stinso', 'https://i.pinimg.com/originals/b9/e2/b3/b9e2b367ec3cdd3db683803f36e40b64.jpg', 8);
INSERT INTO PERSONAJES (IDPERSONAJE, PERSONAJE, IMAGEN, IDSERIE) VALUES (3, 'Dustin Henderso', 'https://phantom-marca.unidadeditorial.es/4f95e661dc8eaa8c0773c1412bd064cc/assets/multimedia/imagenes/2021/02/16/16134683192170.jpg', 3);
INSERT INTO PERSONAJES (IDPERSONAJE, PERSONAJE, IMAGEN, IDSERIE) VALUES (4, 'Oliver Atom', 'https://i.pinimg.com/originals/d6/da/4a/d6da4a6d4a2bc7029845abb5a59f702b.jpg', 7);
INSERT INTO PERSONAJES (IDPERSONAJE, PERSONAJE, IMAGEN, IDSERIE) VALUES (5, 'Benji Price', 'https://media.revistagq.com/photos/5e7212ac9da1570008d603e5/16:9/w_1920,c_limit/benji-price-campeones-serie.jpg', 7);
INSERT INTO PERSONAJES (IDPERSONAJE, PERSONAJE, IMAGEN, IDSERIE) VALUES (6, 'Once', 'https://vader.news/__export/1598037970333/sites/gadgets/img/2020/08/21/once.jpg_691115875.jpg', 3);
INSERT INTO PERSONAJES (IDPERSONAJE, PERSONAJE, IMAGEN, IDSERIE) VALUES (7, 'Sheldon Cooper', 'https://www.bolsamania.com/cine/wp-content/uploads/2015/04/26.jpg', 4);
INSERT INTO PERSONAJES (IDPERSONAJE, PERSONAJE, IMAGEN, IDSERIE) VALUES (9, 'El Mandaloriano', 'https://static.wikia.nocookie.net/esstarwars/images/8/8a/Pascal_as_The_Mando-Advanced_Graphics.png', 2);
INSERT INTO PERSONAJES (IDPERSONAJE, PERSONAJE, IMAGEN, IDSERIE) VALUES (10, 'Baby Yoda', 'https://static2.abc.es/media/play/2020/11/13/baby-yoda-kdIH--620x349@abc.jpg', 2);
INSERT INTO PERSONAJES (IDPERSONAJE, PERSONAJE, IMAGEN, IDSERIE) VALUES (12, 'Daenerys Targarye', 'https://assets.afcdn.com/story/20150813/736968_w980h638c1cx494cy293.jpg', 1);
INSERT INTO PERSONAJES (IDPERSONAJE, PERSONAJE, IMAGEN, IDSERIE) VALUES (14, 'Tyrion Lannister', 'https://vader.news/__export/1593841129501/sites/gadgets/img/2020/07/04/tyrion_lannister_game_of_thrones.jpg_1255757245.jpg', 1);
INSERT INTO PERSONAJES (IDPERSONAJE, PERSONAJE, IMAGEN, IDSERIE) VALUES (15, 'Pablo Escobar', 'https://api.time.com/wp-content/uploads/2016/09/narcos_season_2.jpg', 4);
INSERT INTO PERSONAJES (IDPERSONAJE, PERSONAJE, IMAGEN, IDSERIE) VALUES (17, 'Agente Peña', 'https://cadenaser00.epimg.net/ser/imagenes/2017/09/28/television/1506579243_820899_1506581069_noticia_normal.jpg', 4);
INSERT INTO PERSONAJES (IDPERSONAJE, PERSONAJE, IMAGEN, IDSERIE) VALUES (18, 'Patriota', 'https://e00-elmundo.uecdn.es/blogs/elmundo/asesinoenserie/imagenes_posts/2019/09/10/200156_540x309.jpg', 5);
INSERT INTO PERSONAJES (IDPERSONAJE, PERSONAJE, IMAGEN, IDSERIE) VALUES (19, 'Luz Estelar', 'https://arsrolica.files.wordpress.com/2019/08/starlight.jpg', 5);
INSERT INTO PERSONAJES (IDPERSONAJE, PERSONAJE, IMAGEN, IDSERIE) VALUES (20, 'Tokio', 'https://images.clarin.com/2017/12/20/SyJOzIdzG_1256x620.jpg', 9);
INSERT INTO PERSONAJES (IDPERSONAJE, PERSONAJE, IMAGEN, IDSERIE) VALUES (21, 'Berli', 'https://tvserieswelove.com/wp-content/uploads/2022/09/Berlin-Money-Heist-1200-1-870x500.jpg', 9);
INSERT INTO PERSONAJES (IDPERSONAJE, PERSONAJE, IMAGEN, IDSERIE) VALUES (22, 'Penny', 'https://hips.hearstapps.com/es.h-cdn.co/fotoes/images/noticias-cine/the-big-bang-theory-y-el-secreto-del-apellido-de-penny/109791953-1-esl-ES/The-Big-Bang-Theory-y-el-secreto-del-apellido-de-Penny.jpg', 6);
INSERT INTO PERSONAJES (IDPERSONAJE, PERSONAJE, IMAGEN, IDSERIE) VALUES (23, 'Robin Scherbatsky', 'https://i.pinimg.com/originals/00/29/68/0029683aad5d3c861b621dc1036113af.png', 8);
INSERT INTO PERSONAJES (IDPERSONAJE, PERSONAJE, IMAGEN, IDSERIE) VALUES (24, 'Fry', 'https://i.pinimg.com/236x/19/d2/97/19d2974d5270ffb5b70ce1421bc5d33e--futurama-slug.jpg', 10);
INSERT INTO PERSONAJES (IDPERSONAJE, PERSONAJE, IMAGEN, IDSERIE) VALUES (25, 'Bender', 'https://www.pintzap.com/storage/img/memegenerator/templates/bender.jpg', 10);
commit;
