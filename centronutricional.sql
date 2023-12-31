PGDMP                         {            centronutricional    15.2    15.2                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    24582    centronutricional    DATABASE     �   CREATE DATABASE centronutricional WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Argentina.1252';
 !   DROP DATABASE centronutricional;
                postgres    false            �            1255    24598    guardareliminados()    FUNCTION       CREATE FUNCTION public.guardareliminados() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    insert into pacientes_eliminados(id_paciente,nombre,apellido,peso,altura,imc) values (old.id_paciente,old.nombre,old.apellido,old.peso,old.altura,old.imc);
   RETURN NEW; 
END;
$$;
 *   DROP FUNCTION public.guardareliminados();
       public          postgres    false            �            1259    24584    paciente    TABLE        CREATE TABLE public.paciente (
    id_paciente integer NOT NULL,
    nombre character varying NOT NULL,
    apellido character varying NOT NULL,
    peso double precision NOT NULL,
    altura double precision NOT NULL,
    imc double precision NOT NULL
);
    DROP TABLE public.paciente;
       public         heap    postgres    false            �            1259    24583    paciente_id_paciente_seq    SEQUENCE     �   CREATE SEQUENCE public.paciente_id_paciente_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.paciente_id_paciente_seq;
       public          postgres    false    215                       0    0    paciente_id_paciente_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.paciente_id_paciente_seq OWNED BY public.paciente.id_paciente;
          public          postgres    false    214            �            1259    24592    pacientes_eliminados    TABLE     �   CREATE TABLE public.pacientes_eliminados (
    id_paciente integer NOT NULL,
    nombre character varying,
    apellido character varying,
    peso double precision,
    altura double precision,
    imc double precision
);
 (   DROP TABLE public.pacientes_eliminados;
       public         heap    postgres    false            j           2604    24587    paciente id_paciente    DEFAULT     |   ALTER TABLE ONLY public.paciente ALTER COLUMN id_paciente SET DEFAULT nextval('public.paciente_id_paciente_seq'::regclass);
 C   ALTER TABLE public.paciente ALTER COLUMN id_paciente DROP DEFAULT;
       public          postgres    false    214    215    215            �          0    24584    paciente 
   TABLE DATA           T   COPY public.paciente (id_paciente, nombre, apellido, peso, altura, imc) FROM stdin;
    public          postgres    false    215   m       �          0    24592    pacientes_eliminados 
   TABLE DATA           `   COPY public.pacientes_eliminados (id_paciente, nombre, apellido, peso, altura, imc) FROM stdin;
    public          postgres    false    216                     0    0    paciente_id_paciente_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.paciente_id_paciente_seq', 15, true);
          public          postgres    false    214            l           2606    24591    paciente paciente_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.paciente
    ADD CONSTRAINT paciente_pkey PRIMARY KEY (id_paciente);
 @   ALTER TABLE ONLY public.paciente DROP CONSTRAINT paciente_pkey;
       public            postgres    false    215            m           2620    24599    paciente pac_elimnadosad    TRIGGER     y   CREATE TRIGGER pac_elimnadosad AFTER DELETE ON public.paciente FOR EACH ROW EXECUTE FUNCTION public.guardareliminados();
 1   DROP TRIGGER pac_elimnadosad ON public.paciente;
       public          postgres    false    217    215            �   �   x�M�=
�@���Sx�!���O)���[�ń�`vd5��7�����oZ�r�	�W��<$��$�c���O�<�V�!��#l�S�׳��G���P�^��'�.�w��ђ�T6���[�&tnugaZ�@&�7'E      �   H   x�34�t�IJ-*��tK-�K�KI��0�4�3��42�32�24�t.�,.��KDRcVc�id�gd����� /|     