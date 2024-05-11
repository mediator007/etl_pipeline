FROM apache/airflow

USER root

COPY ./src /opt/airflow/dags/

ENV AIRFLOW__WEBSERVER__AUTHENTICATE=True
ENV AIRFLOW__WEBSERVER__AUTH_BACKEND=airflow.contrib.auth.backends.password_auth
ENV AIRFLOW__WEBSERVER__BASE_URL=http://localhost:8080
ENV AIRFLOW__WEBSERVER__AUTH_USER=admin
ENV AIRFLOW__WEBSERVER__AUTH_PASSWORD=admin

ENV PYTHON_PATH=/opt/airflow/dags/

RUN airflow db init

CMD ["airflow", "scheduler"]
