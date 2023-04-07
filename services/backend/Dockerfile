FROM python:3.11 as base
RUN pip install poetry

RUN mkdir /app
WORKDIR /app

# so we speed up local dev.
COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY . .

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
