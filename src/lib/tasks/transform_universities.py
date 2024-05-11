from airflow.models.taskinstance import TaskInstance
from pydantic import ValidationError

from lib.tasks.models import University, Types
from utils.logger import get_logger


log = get_logger()


def transform_universities(**kwargs) -> list[University]:
    """
    Transform data from the get_data task.
    """
    transformed_data = list()
    ti: TaskInstance = kwargs['ti']
    response: list[dict] = ti.xcom_pull(task_ids='get_data')
    log.info(f"Response quantity {len(response)}")
    for university in response:
        try:
            university = University(**university)
        except ValidationError as e:
            log.error(f"Incorrect university data: {university}. Error: {e}")
            continue
        _validate_university_type(university)
        transformed_data.append(university)
    return transformed_data


def _validate_university_type(university: University) -> None:
    for type in Types:
        if type.value in university.name:
            university.type = type.value
            break
