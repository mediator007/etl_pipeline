FROM apache/airflow

USER airflow

WORKDIR /opt/airflow

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./src /opt/airflow/dags/

USER root

ENV AIRFLOW__WEBSERVER__AUTHENTICATE=True
ENV AIRFLOW__WEBSERVER__AUTH_BACKEND=airflow.contrib.auth.backends.password_auth
ENV AIRFLOW__WEBSERVER__BASE_URL=http://localhost:8080
ENV AIRFLOW__WEBSERVER__AUTH_USER=admin
ENV AIRFLOW__WEBSERVER__AUTH_PASSWORD=admin

ENV PYTHON_PATH=/opt/airflow/dags/

RUN airflow db init

CMD ["airflow", "scheduler"]
