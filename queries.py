from const import DESCRIPTION, QUERY

TPC_H_QUERY_6_ENIGMA_JHU = """
select sum(confirmed * active) as just_number
from enigma_jhu
where try_cast(last_update AS date) >= date '1970-10-08'
  and try_cast(last_update AS date) < date '2024-10-08' + interval '1' year
  and deaths between 0 - 0.01 and 180 + 0.01
  and recovered < 1000"""

TPC_H_QUERY_6_HOSPITAL_BEDS = """
select sum(cast(num_staffed_beds as decimal) * cast(avg_ventilator_usage as decimal)) as just_number
from hospital_beds
where try_cast(cnty_fips AS integer) >= 10
  and try_cast(cnty_fips AS integer) < 200
  and latitude between 0 - 0.01 and 180 + 0.01
  and longtitude < 0
"""
TPC_H_QUERY_6_DESC = "TPC-H/TPC-R (Q6) for table: {table}"
QUERY_6_ENIGMA_JHU = {DESCRIPTION: TPC_H_QUERY_6_DESC.format(table="enigma_jhu"),
                      QUERY: TPC_H_QUERY_6_ENIGMA_JHU}
QUERY_6_HOSPITAL_BEDS = {DESCRIPTION: TPC_H_QUERY_6_DESC.format(table="hospital_beds"),
                         QUERY: TPC_H_QUERY_6_HOSPITAL_BEDS}

QUERIES = (QUERY_6_ENIGMA_JHU, QUERY_6_HOSPITAL_BEDS)
