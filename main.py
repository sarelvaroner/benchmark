import logging

from const import QUERY, DESCRIPTION
from db import session, get_total_run_time
from queries import QUERIES



NUMBER_OF_ITERATIONS = 10


def get_average_run_time(query: str, iterations: int = NUMBER_OF_ITERATIONS):
    total_run_time = get_total_run_time(query=query, iterations=iterations)
    return total_run_time / NUMBER_OF_ITERATIONS


if __name__ == '__main__':
    print(f"Start benchmarking now please wait.")

    try:
        for q in QUERIES:
            result = get_average_run_time(query=(q[QUERY]))
            print(f"Result run time of {round(result, 2)} sec for {q[DESCRIPTION]}")
    except Exception as e:
        logging.exception(e)
    finally:
        session.close()
        print(f"End.")
