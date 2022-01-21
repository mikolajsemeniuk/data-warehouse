use master
go
drop database if exists DataWarehouse
create database DataWarehouse
go
use DataWarehouse

drop table if exists employees
create table employees
(
    employee_id int primary key identity(1, 1),
    employee_name varchar(30) unique not null,
    gross_salary_per_month money not null,
    net_salary_per_month money not null,
    sex bit not null,
    vacation_used int not null,
    vacation_not_taken int not null,
    years_in_company smallint not null
)

drop table if exists companies
create table companies
(
    company_id int primary key identity(1, 1),
    company_name varchar(30) unique not null,
    company_size bigint not null,
    assets_value money not null,
    years_on_market int not null
)

drop table if exists services
create table services
(
    service_id int primary key identity(1, 1),
    service_field varchar(30) unique not null,
    turnover_per_year money not null,
    market_share smallint not null,
    taxes_paid money not null
)

drop table if exists countries
create table countries
(
    country_id int primary key identity(1, 1),
    country_name varchar(30) unique not null,
    country_population int not null,
    import_of_goods int not null,
    export_of_goods int not null,
)

drop table if exists projects_period
create table projects_period
(
    project_period_id int primary key identity(1, 1),
    start_project_date datetime not null,
    estimated_end_project_date datetime not null,
    real_end_project_date datetime not null,
)

drop table if exists projects_sales
create table projects_sales (
    project_sale_id int primary key identity(1, 1),
    employee_id int references employees not null,
    company_id int references companies not null,
    service_id int references services not null,
    country_id int references countries not null,
    project_period_id int references projects_period not null,
    gross_salary money not null,
    net_salary money not null,
    eu_taxes money not null,
    polish_taxes money not null,
)

-- insert into 
--     companies (company_name, company_size, assets_value, years_on_market)
-- values
--     ('Ernst & Young', 1000, 1000000000, 30),
--     ('Takeda', 500, 500000000, 10),
--     ('Smith & Nephew', 10000, 2000000000, 15),
--     ('Wavin', 200, 100000, 10),
--     ('Admiral group', 10000, 5000000000, 30)

-- select * from companies
-- select * from projects_sales