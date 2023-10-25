# gateway/urls.py
urls = {
    "math": {
        "add": ("http://math-service:5000/add", "GET"),
        "sub": ("http://math-service:5000/sub", "GET"),
        "mul": ("http://math-service:5000/mul", "GET"),
        "div": ("http://math-service:5000/div", "GET"),
        "mod": ("http://math-service:5000/mod", "GET"),
    },
    "str": {
        "concat": ("http://string-service:5000/concat", "GET"),
        "upper": ("http://string-service:5000/upper", "GET"),
        "lower": ("http://string-service:5000/lower", "GET"),
    },
}
