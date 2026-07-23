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

### Option 1

```
$ uv run hello-world.py
(...)
+ uv run streamlit run --server.headless True --server.address 127.0.0.1 --server.port 16666 --logger.level debug hello-world.py
(...)
```

### Option 2

```
$ ./run.sh hello-world.py
(...)
+ uv run streamlit run --server.headless True --server.address 127.0.0.1 --server.port 16666 --logger.level debug hello-world.py
(...)
```
