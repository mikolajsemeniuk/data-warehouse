import pymssql
import random as r
from datetime import datetime as dt


SERVER = 'localhost'
USER = 'sa'
PASSWORD = 'P@ssw0rd'
DB = 'DataWarehouse'

conn = pymssql.connect(SERVER, USER, PASSWORD, DB)
cursor = conn.cursor()


companies = [
    ('Ernst & Young', 1000, 1000000000, 30),
    ('Takeda', 500, 500000000, 10),
    ('Smith & Nephew', 10000, 2000000000, 15),
    ('Wavin', 200, 100000, 10),
    ('Admiral group', 10000, 5000000000, 30),
    ('Pfeizer', 15000, 3000000000, 13)
]
cursor.executemany(
    '''
        insert into 
            companies (company_name, company_size, assets_value, years_on_market) 
        values (%s, %d, %d, %d)
    ''', companies)
conn.commit()


employees = [
    ('John Doe', 3000, 2000, 1, 0, 21, 3),
    ('Mike Mock', 4000, 2500, 1, 7, 14, 5),
    ('Lucy Applegate', 4000, 3000, 0, 3, 18, 7),
    ('Ian Evans', 3500, 3500, 1, 0, 21, 1),
    ('Sam Cooke', 5500, 4500, 1, 0, 21, 10),
    ('Jessica George', 3000, 3000, 0, 1, 20, 1),
    ('Britney Gross', 7000, 5500, 0, 21, 0, 15),
    ('Felicia Nelson', 7500, 5600, 0, 14, 7, 14),
    ('Gary Bateman', 8000, 7000, 1, 0, 21, 19),
    ('Ivy Cole', 4500, 4000, 1, 21, 0, 4)
]
cursor.executemany(
    '''
        insert into 
            employees (employee_name, gross_salary_per_month, net_salary_per_month, sex, vacation_used, vacation_not_taken, years_in_company) 
        values (%s, %d, %d, %d, %d, %d, %d)
    ''', employees)
conn.commit()


services = [
    ('electronic', 100_000_000, 5, 2_000_000),
    ('construction', 200_000_000, 10, 1_000_000),
    ('heating', 50_000_000, 1, 10_000_000),
    ('railroad', 160_000_000, 10, 1_220_000),
    ('machinery', 500_000_000, 8, 10_000_000),
    ('industrial', 400_000_000, 5, 100_000_000),
    ('medical', 50_000_000, 4, 1_000_000),
    ('automotive', 1_000_000_000, 19, 100_000_000),
    ('estates', 10_000_000_000, 26, 500_000_000),
    ('fuels', 10_000_000, 3, 500_000)
]
cursor.executemany(
    '''
        insert into 
            services (service_field, turnover_per_year, market_share, taxes_paid) 
        values (%s, %d, %d, %d)
    ''', services)
conn.commit()


countries = [
    ('Poland', 36_000_000, 100_000, 100_000),
    ('Australia', 26_000_000, 500_000, 100_000),
    ('USA', 330_000_000, 1_000_000, 10_000_000),
    ('Italy', 60_000_000, 300_000, 500_000),
    ('Germany', 83_000_000, 1_000_000, 3_000_000),
    ('Turkey', 84_000_000, 3_000_000, 2_000_000),
    ('France', 67_000_000, 1_000_000, 2_000_000),
    ('Japan', 130_000_000, 2_000_000, 10_000_000),
    ('Norway', 5_000_000, 500_000, 200_000),
    ('Switzerland', 8_000_000, 1_000_000, 800_000)
]
cursor.executemany(
    '''
        insert into 
            countries (country_name, country_population, import_of_goods, export_of_goods) 
        values (%s, %d, %d, %d)
    ''', countries)
conn.commit()


projects_period = [
    (dt(2021, 1, 1), dt(2021, 4, 1), dt(2021, 4, 1)),
    (dt(2021, 3, 1), dt(2021, 6, 14), dt(2021, 7, 28)),
    (dt(2021, 2, 15), dt(2021, 10, 4), dt(2021, 11, 5)),
    (dt(2021, 4, 28), dt(2021, 11, 2), dt(2021, 10, 27)),
    (dt(2021, 1, 12), dt(2021, 5, 16), dt(2021, 7, 21)),
    (dt(2022, 1, 9), dt(2021, 3, 11), dt(2021, 3, 28)),
    (dt(2022, 2, 10), dt(2021, 6, 12), dt(2021, 7, 12)),
    (dt(2021, 5, 5), dt(2021, 8, 8), dt(2021, 9, 10)),
    (dt(2021, 6, 15), dt(2021, 12, 15), dt(2022, 2, 7)),
    (dt(2021, 11, 1), dt(2022, 6, 1), dt(2022, 7, 28))
]
cursor.executemany(
    '''
        insert into 
            projects_period (start_project_date, estimated_end_project_date, real_end_project_date) 
        values (%s, %s, %s)
    ''', projects_period)
conn.commit()


number_of_samples = 100
projects_sales = []
for _ in range(number_of_samples):
    gross_salary = r.randint(100_000, 50_000_000)
    net_salary = round(gross_salary * r.uniform(.5, .8), 2)

    threshold = round(r.uniform(.1, .9), 2)

    polish_taxes = round((gross_salary - net_salary) * threshold, 2)
    eu_taxes = round((gross_salary - net_salary) * (1 - threshold), 2)
    projects_sales.append(
        (
            r.randint(1, len(employees)),
            r.randint(1, len(companies)),
            r.randint(1, len(services)),
            r.randint(1, len(countries)),
            r.randint(1, len(projects_period)),
            gross_salary,
            net_salary,
            eu_taxes,
            polish_taxes
        )
    )
cursor.executemany(
    '''
        insert into 
            projects_sales (employee_id, company_id, service_id, country_id, project_period_id, gross_salary, net_salary, eu_taxes, polish_taxes) 
        values (%d, %d, %d, %d, %d, %d, %d, %d, %d)
    ''', projects_sales)
conn.commit()


conn.close()
