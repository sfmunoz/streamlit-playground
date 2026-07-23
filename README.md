# streamlit-playground

Streamlit playground

## References

- https://streamlit.io/
- [Streamlit Mini Course - Make Websites With ONLY Python](https://www.youtube.com/watch?v=o8p7uQCGD0U)

## Install

```
$ uv sync
```

## Run

```
$ ./run.sh hello-world.py
(...)
+ uv run streamlit run --server.headless True --server.address 127.0.0.1 --server.port 16666 --logger.level debug hello-world.py
(...)
2026-07-23 14:49:29.035 Uvicorn server started on 127.0.0.1:16666

  You can now view your Streamlit app in your browser.

  URL: http://127.0.0.1:16666
(...)
```
