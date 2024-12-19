from flask import Flask

from sql_practice import add_post,delete_post,update_post,get_posts

app = Flask(__name__)

weather = {
    "astana" : -10.3,
    "almaty" : -6.7,
    "vienna" : 0}

todos = []


@app.route("/todos/new/<title>")
def add_todos(title):
    todos.append(title)
    return title

@app.route("/todos")
def get_todos():
    return todos


@app.route("/")
def welcome():
    return"Это моё первое API"

@app.route("/name")
def get_name():
    return"Kirill"

@app.route("/city/<city_name>")
def weather_by_city(city_name):
    city_name_lower = city_name.lower()

    if city_name_lower in weather:
        temp = weather[city_name_lower]
        return f"Погода в {city_name} {temp} цельсия"

    return f"нет инфы о погоде в {city_name}"



# 1
@app.route("/posts/add/<post_title>/<post_content>")
def add_new_post(post_title, post_content):
    return add_post(title=post_title,content=post_content)


# 2
@app.route("/posts")
def get_all_posts():
    return get_posts()


# 3
@app.route("/posts/delete/<post_id>")
def delete_post_by_id(post_id):
    return delete_post(post_id)


# 4
@app.route("/posts/update/<post_id>/<new_title>/<new_content>")
def update_post_by_id(post_id, new_title, new_content):
    return update_post(post_id=post_id,new_title=new_title,new_content=new_content)


if __name__ == "__main__":
    app.run(port = 5112, host="0.0.0.0", debug=True)