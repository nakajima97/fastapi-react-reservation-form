import pytest
import pytest_asyncio
import starlette.testclient

from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from source.db import get_db, Base
from source.main import app

ASYNC_DB_URL = "sqlite+aiosqlite:///./:memory:"

@pytest_asyncio.fixture
async def async_client() -> AsyncClient:
  async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
  async_session = sessionmaker(autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession)

  # テスト用にオンメモリのSQLiteテーブルを初期化
  async with async_engine.begin() as conn:
    await conn.run_sync(Base.metadata.drop_all)
    await conn.run_sync(Base.metadata.create_all)

  # DIを使ってFastAPIのアプリケーションをテスト用のDBセッションで初期化
  async def get_test_db():
    async with async_session() as session:
      yield session

  app.dependency_overrides[get_db] = get_test_db

  # テスト用に非同期HTTPクライアントを返却
  async with AsyncClient(app=app, base_url="http://test") as client:
    yield client

@pytenst.mark.asyncio
async def test_get_calendars(async_client: AsyncClient):
  response = await async_client.get("/calendars")
  assert response.status_code == starlette.status.HTTP_200_OK