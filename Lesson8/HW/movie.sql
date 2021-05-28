--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

-- Started on 2021-05-14 21:09:53

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 202 (class 1259 OID 16407)
-- Name: actors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.actors (
    num integer,
    name text
);


ALTER TABLE public.actors OWNER TO postgres;

--
-- TOC entry 201 (class 1259 OID 16401)
-- Name: directors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.directors (
    num integer,
    name text
);


ALTER TABLE public.directors OWNER TO postgres;

--
-- TOC entry 200 (class 1259 OID 16395)
-- Name: films; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.films (
    num integer,
    title text
);


ALTER TABLE public.films OWNER TO postgres;

--
-- TOC entry 2991 (class 0 OID 16407)
-- Dependencies: 202
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.actors (num, name) VALUES (1, 'Viggo Mortensen');
INSERT INTO public.actors (num, name) VALUES (2, 'Leonardo Di Caprio');
INSERT INTO public.actors (num, name) VALUES (3, 'Jodie Foster');
INSERT INTO public.actors (num, name) VALUES (4, 'Geoffrey Rush');
INSERT INTO public.actors (num, name) VALUES (5, 'Daniel Craig');
INSERT INTO public.actors (num, name) VALUES (6, 'Hilary Swank');
INSERT INTO public.actors (num, name) VALUES (7, 'Arnold Schwarzenegger');
INSERT INTO public.actors (num, name) VALUES (8, 'Julia Roberts');
INSERT INTO public.actors (num, name) VALUES (9, 'Matthew McConaughey');
INSERT INTO public.actors (num, name) VALUES (10, 'Christian Bale');


--
-- TOC entry 2990 (class 0 OID 16401)
-- Dependencies: 201
-- Data for Name: directors; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.directors (num, name) VALUES (1, 'Peter Farrelly');
INSERT INTO public.directors (num, name) VALUES (2, 'Martin Scorsese');
INSERT INTO public.directors (num, name) VALUES (3, 'Jonathan Demme');
INSERT INTO public.directors (num, name) VALUES (4, 'Giuseppe Tornatore');
INSERT INTO public.directors (num, name) VALUES (5, 'Rian Johnson');
INSERT INTO public.directors (num, name) VALUES (6, 'Clint Eastwood');
INSERT INTO public.directors (num, name) VALUES (7, 'James Cameron');
INSERT INTO public.directors (num, name) VALUES (8, 'Stephen Chbosky');
INSERT INTO public.directors (num, name) VALUES (9, 'Christopher Nolan');
INSERT INTO public.directors (num, name) VALUES (10, 'Christopher Nolan');


--
-- TOC entry 2989 (class 0 OID 16395)
-- Dependencies: 200
-- Data for Name: films; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.films (num, title) VALUES (1, 'Green Book');
INSERT INTO public.films (num, title) VALUES (2, 'The Wolf of Wall Street');
INSERT INTO public.films (num, title) VALUES (3, 'The Silence of the Lambs');
INSERT INTO public.films (num, title) VALUES (4, 'La migliore offerta');
INSERT INTO public.films (num, title) VALUES (5, 'Knives Out');
INSERT INTO public.films (num, title) VALUES (6, 'Millions Dollar Baby');
INSERT INTO public.films (num, title) VALUES (7, 'Terminator2:Judgment Day');
INSERT INTO public.films (num, title) VALUES (8, 'Wonder');
INSERT INTO public.films (num, title) VALUES (9, 'Interstellar');
INSERT INTO public.films (num, title) VALUES (10, 'The Dark Knidht');


-- Completed on 2021-05-14 21:09:54

--
-- PostgreSQL database dump complete
--

