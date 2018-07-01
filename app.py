from apistar import App, Route


def welcome(name=None):
    if name is None:
        return {"message": "Welcome to Athens Tech!"}
    return {"message": "Welcome to Athens Tech, %s!" % name}


routes = [Route("/", method="GET", handler=welcome)]

app = App(routes=routes)


if __name__ == "__main__":
    app.serve("0.0.0.0", 5000, debug=True)
