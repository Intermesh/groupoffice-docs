FROM keimlink/sphinx-doc

COPY --chown=1000:1000 requirements.pip ./

RUN . .venv/bin/activate \
    && python -m pip install --requirement requirements.pip

EXPOSE 8000

CMD ["sphinx-autobuild", "--host", "0.0.0.0", "--port", "8000", "/home/python/docs", "/home/python/docs/_build/html"]