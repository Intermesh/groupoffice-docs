FROM sphinxdoc/sphinx

WORKDIR /docs
ADD requirements.pip /docs
RUN pip3 install -r requirements.pip

EXPOSE 8000

CMD ["sphinx-autobuild", "--host", "0.0.0.0", "--port", "8000", "/docs", "/docs/_build/html", "--ignore", "**/.idea/**", "--ignore", "**/.git/**", "--ignore", "**/docker/**",  "--ignore", "**/*.*~", "--ignore", "conf.py"]
