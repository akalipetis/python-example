from apistar import App, Route


def welcome(name=None):
    if name is None:
        return {"message": "Welcome to Code Learn woohoo!"}
    return {"message": "Welcome to Code Learn, %s yeah!!" % name}


routes = [Route("/", method="GET", handler=welcome)]

app = App(routes=routes)


if __name__ == "__main__":
    app.serve("0.0.0.0", 5000, debug=True)
