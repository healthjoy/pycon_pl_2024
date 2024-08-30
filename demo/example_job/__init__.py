from demo.example_job.constants import MAX_N
from demo.example_job import ver1
from demo.example_job import ver2
from demo.example_job import ver3


def report_eligible_ids() -> None:
    """Generate the identities, verify their eligibility and output the number of eligible ones"""
    get_current_ids = list(range(MAX_N))
    # print(ver1.get_eligible_ids_count(get_current_ids))
    print(ver2.get_eligible_ids_count(get_current_ids))
    # print(ver3.get_eligible_ids_count(get_current_ids))
