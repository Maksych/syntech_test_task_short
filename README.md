# Syntech Test Task Short

## Requirements
- Docker and Docker-Compose
- 2.5 Gb disk memory

## How to run?
```shell
git clone https://github.com/Maksych/syntech_test_task_short.git
cd syntech_test_task_short
docker-compose up
```
#### Additional
Created 10 tables

## How to test REST?
- Swagger UI: \
  http://loalhsot:8000/api/schema/swagger-ui/
- Get tables: \
  GET \
  http://localhost:8000/api/v1/tables/?date={year-month-day} \
  NOTE: query param "date" is required
- Reserve table: \
  POST \
  http://localhost:8000/api/v1/reservations/ \
  JSON BODY \
  {"date": "{year}-{month}-{day}", "table": {table_id}, "email": "{email}"}
   
