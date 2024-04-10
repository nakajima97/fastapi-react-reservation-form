# v2への移行
テストコードとかエンドポイントとかを整理するためにゼロから開発しなおすことにした  
version2として以下リポジトリを作成
https://github.com/nakajima97/fastapi-react-reservation-form-v2

# fastapi-react-reservation-form
## Clone後に実行するコマンド
`docker compose up`  
`docker compose run --entrypoint "poetry install --no-root" api`  

マイグレーションの実行  
`docker compose exec api poetry run python -m source.migrate_db`  

# テストコードの実行
## api
`docker compose run --entrypoint "poetry run pytest" api`
