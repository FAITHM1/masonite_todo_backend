"""Web Routes."""

from masonite.routes import Get, Post,Put,Delete,RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),
    RouteGroup([
        Get("/","TodoController@index").name("index"),
        Get("/@id","TodoController").name("show"),
        Post("/","TodoController@create").name("create"),
        Put("/@id","TodoController@update").name("update"),
        Delete("/@id","TodoController@destroy").name("destroy")
    ],prefix="/todos",name="todos")
]

