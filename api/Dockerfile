# BASE IMAGE bookworm = debian
FROM python:3.13.0a5-bookworm

WORKDIR /app

# install poetry
RUN pip install poetry

# poetryの設定ファイルをコピー
COPY pyproject.toml* poetry.lock* ./

# 仮想環境の構築
RUN poetry config virtualenvs.in-project true

# poetryでライブラリをインストールする
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi

# Uvicornサーバの起動
ENTRYPOINT ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload"]