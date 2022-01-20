
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
    years_in_company smallint not null,
    relationship_status varchar(10) not null check (relationship_status in ('Single', 'Married', 'Divorced', 'Other')),
)

drop table if exists companies
create table companies
(
    company_id int primary key identity(1, 1),
    company_name varchar(30) unique not null,
    company_size bigint not null,
    assets_value money not null
)

drop table if exists services
create table services
(
    service_id int primary key identity(1, 1),
    service_field varchar(30) unique not null,
    turnover_per_year money not null,
    market_share smallint not null,
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
    end_project_date datetime not null,
)

drop table if exists projects_sales
create table projects_sales (
    employee_id int references employees,
    company_id int references companies,
    service_id int references services,
    country_id int references countries,
    project_period_id int references projects_period,
    gross_salary money not null,
    net_salary money not null,
    eu_taxes money not null,
    polish_taxes money not null,
)

select * from projects_sales