drop table if exists "gin_test";
create table "gin_test"("id" bigserial primary key, "string" text, "gin_vector" tsvector);
insert into "gin_test"("string") select substr(characters, (random() * length(characters) + 1)::integer, 10) from (values('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) as symbols(characters), generate_series(1,1000000) as q;
update "gin_test" set "gin_vector" = to_tsvector("string");