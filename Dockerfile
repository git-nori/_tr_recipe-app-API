FROM python:3.7-alpine
MAINTAINER London App Developer Ltd

# 環境変数
ENV PYTHONUNBUFFERED 1

# [requirements.txtをDockerイメージの/requirements.txtにコピー]
COPY ./requirements.txt /requirements.txt
# 指定したパッケージのインストール
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
# 作業後の不要なパッケージの削除
# 指定したパッケージ(命名したパッケージ郡の.tmp-build-deps)をアンインストール
RUN apk del .tmp-build-deps

# [アプリのディレクトリをDockerイメージ内に作成]
RUN mkdir /app
# アプリのルートディレクトリを設定
WORKDIR /app
COPY ./app /app

# アプリ用にアプリを実行するユーザーの作成と設定
RUN adduser -D user
USER user