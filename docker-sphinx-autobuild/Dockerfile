FROM sphinxdoc/sphinx

# git is required by sphinx-multiversion to read each version's content
RUN apt-get update && apt-get install -y --no-install-recommends git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /docs
ADD requirements.pip /docs
RUN pip3 install -r requirements.pip

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000

CMD ["/entrypoint.sh"]
