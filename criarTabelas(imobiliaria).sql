#script para MYSQL - apenas tabelas do tipo de operação, fato, imoveis e as relacionadas a localização criadas

create database db;
use db;

create table cidade (idCidade numeric(6) not null, nome varchar(50) not null, estado varchar(2) not null);
alter table cidade add primary key (idCidade);

create table bairro (idBairro numeric(3) not null, idCidade numeric(6) not null, nome varchar(50));
alter table bairro add primary key (idBairro);
alter table bairro add foreign key (idCidade) references cidade (idCidade);

create table localizacao (cep numeric(8) not null, idBairro numeric(3) not null, rua varchar(100) not null);
alter table localizacao add primary key (cep);
alter table localizacao add foreign key (idBairro) references bairro (idBairro);

create table areaUtil (idAreaUtil numeric(3) not null, descricao varchar(100) not null);
alter table areaUtil add primary key (idAreaUtil);

create table faixaPreco (idFaixaPreco numeric(3) not null, descricao varchar(100) not null);
alter table faixaPreco add primary key (idFaixaPreco);

create table categoriaImovel (idCategoriaImovel numeric(2) not null, descricao varchar(200) not null);
alter table categoriaImovel add primary key (idCategoriaImovel);
 
create table numeroQuartos (idNumeroQuartos numeric(2) not null, descricao varchar(100) not null);
alter table numeroQuartos add primary key (idNumeroQuartos);

create table imovel (idImovel numeric(5) not null, idNumeroQuartos numeric(2) not null, idAreaUtil numeric(3) not null,
idCategoriaImovel numeric(2) not null, vagasGaragem numeric(2) not null, banheiros numeric(2) not null);
alter table imovel add primary key (idImovel);
alter table imovel add foreign key (idNumeroQuartos) references numeroQuartos (idNumeroQuartos);
alter table imovel add foreign key (idAreaUtil) references areaUtil (idAreaUtil);
alter table imovel add foreign key (idCategoriaImovel) references categoriaImovel (idCategoriaImovel);

create table tipoOperacao (idTipoOperacao numeric(2) not null, idImovel numeric(5) not null, idFaixaPreco numeric(3) not null, descricao varchar(100) not null);
alter table tipoOperacao add primary key (idTipoOperacao, idImovel);
alter table tipoOperacao add foreign key (idImovel) references imovel (idImovel);
alter table tipoOperacao add foreign key (idFaixaPreco) references faixaPreco (idFaixaPreco);

create table fato 
(idFato numeric(10) not null, idGrupoConsumidor numeric(5), idAnunciante numeric(3), idModalidadePagamento numeric(2), idImovel numeric(5), idTempoDiario numeric(5),
cep numeric(8));
alter table fato add primary key (idFato);
alter table fato add foreign key (cep) references localizacao (cep);
alter table fato add foreign key (idImovel) references imovel(idImovel);

