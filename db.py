from timeit import timeit

import trino
from pystarburst import Session

db_parameters = {
    "host": "sarv-free-cluster.trino.galaxy.starburst.io",
    "port": 443,
    "http_scheme": "https",
    "catalog": "covid_19",
    "schema": "covid_tutorial",
    "auth": trino.auth.BasicAuthentication("sarhel.s@gmail.com/accountadmin", "rSbDTY77vCCbv9R")
}
session = Session.builder.configs(db_parameters).create()


def get_total_run_time(query: str, iterations: int) -> float:
    sql = session.sql(query)
    return timeit('sql.collect()', number=iterations, globals=locals())
