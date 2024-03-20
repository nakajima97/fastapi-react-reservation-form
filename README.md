# fastapi-react-reservation-form
## Clone後に実行するコマンド
`docker compose up`  
`docker compose run --entrypoint "poetry install --no-root" api`  

マイグレーションの実行  
`docker compose exec api poetry run python -m source.migrate_db`  