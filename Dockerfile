FROM python:3.7-alpine
MAINTAINER London App Developer Ltd

# 環境変数
ENV PYTHONUNBUFFERED 1

# [requirements.txtをDockerイメージの/requirements.txtにコピー]
COPY ./requirements.txt /requirements.txt
# 指定したパッケージのインストール
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
# 作業後の不要なパッケージの削除
# 指定したパッケージ(命名したパッケージ郡の.tmp-build-deps)をアンインストール
RUN apk del .tmp-build-deps

# [アプリのディレクトリをDockerイメージ内に作成]
RUN mkdir /app
# アプリのルートディレクトリを設定
WORKDIR /app
COPY ./app /app

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
# アプリ用にアプリを実行するユーザーの作成と設定
RUN adduser -D user
# /vol/配下のディレクトリに対して所有者を一括設定
RUN chown -R user:user /vol/
# /vol/web配下のディレクトリに対してパーミッション(755)を設定
RUN chown -R 755 /vol/web

USER user