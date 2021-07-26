# For ubuntu, the latest tag points to the LTS version, since that is
# recommended for general use.
FROM python:3.6-slim

RUN apt-get update && apt-get install -y --no-install-recommends wget unzip dirmngr ca-certificates ffmpeg gosu
RUN pip install --no-cache-dir youtube-dl flask setuptools

# install youtube-dl-webui
ENV YOUTUBE_DL_WEBUI_SOURCE /usr/src/youtube_dl_webui
WORKDIR $YOUTUBE_DL_WEBUI_SOURCE

COPY youtube_dl_webui /usr/src/youtube_dl_webui
COPY setup.py /usr/src/
RUN ln -s $YOUTUBE_DL_WEBUI_SOURCE/example_config.json /etc/youtube-dl-webui.json \
	&& apt-get purge -y --auto-remove wget unzip dirmngr \
	&& rm -fr /var/lib/apt/lists/*

COPY dockerfile/docker-entrypoint.sh /usr/local/bin
COPY dockerfile/default_config.json /config.json
RUN cd /usr/src && pip install . --use-feature=in-tree-build -v
ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["python", "-m", "youtube_dl_webui"]
