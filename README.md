# etl_pipeline

### Runthe Project  
Use `git clone --recurse-submodules <project>` command to clone project  
Run project using docker compose v.2 with commands:  
- `sudo docker compose build`  
- `sudo docker compose up` 
Launch ETL DAG with commands:
- `docker exec etl airflow dags trigger mydag`  
- `docker exec etl airflow dags unpause mydag` 


### Scheduler setting
For changing scheduling fix `/src/settings.py`