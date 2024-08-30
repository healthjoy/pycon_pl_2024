import cProfile

import pyinstrument

from demo.example_job import report_eligible_ids


if __name__ == '__main__':
    with cProfile.Profile() as pr:
        report_eligible_ids()
        pr.print_stats()

    with pyinstrument.profile():
        report_eligible_ids()
