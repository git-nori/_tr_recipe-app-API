FROM python:3.7-alpine
MAINTAINER London App Developer Ltd

# 環境変数
ENV PYTHONUNBUFFERED 1

# [requirements.txtをDockerイメージの/requirements.txtにコピー]
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# [アプリのディレクトリをDockerイメージ内に作成]
RUN mkdir /app
# アプリのルートディレクトリを設定
WORKDIR /app
COPY ./app /app

# アプリ用にアプリを実行するユーザーの作成と設定
RUN adduser -D user
USER user