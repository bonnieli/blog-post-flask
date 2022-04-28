import json
from tests.utils import make_token
from tests import client
from tests.utils import SYSTEM_TIME


def test_get_posts(client):
    """should return all posts of author ID 2 in specific order."""

    token = make_token(2)
    query_params = {"authorIds": "2"}
    response = client.get(
        "/api/posts", headers={"x-access-token": token}, query_string=query_params
    )

    assert response.json == posts_of_user_2


def test_update_posts(client):
    """should update properties of a post."""

    token = make_token(1)
    post_id = 1
    data = {"tags": ["travel", "vacation"], "text": "my text", "authorIds": [1, 5]}

    response = client.patch(
        f"/api/posts/{post_id}",
        headers={"x-access-token": token},
        data=json.dumps(data),
    )

    assert response.json == updated_post


# mock data
posts_of_user_2 = {
    "posts": [
        {
            "tags": ["food", "recipes", "baking"],
            "id": 1,
            "text": "Excepteur occaecat minim reprehenderit cupidatat dolore voluptate velit labore pariatur culpa esse mollit. Veniam ipsum amet eu dolor reprehenderit quis tempor pariatur labore. Tempor excepteur velit dolor commodo aute. Proident aute cillum dolor sint laborum tempor cillum voluptate minim. Amet qui eiusmod duis est labore cupidatat excepteur occaecat nulla.",
            "likes": 12,
            "reads": 5,
            "popularity": 0.19,
            "createdAt": SYSTEM_TIME,
            "updatedAt": SYSTEM_TIME,
        },
        {
            "tags": ["travel", "hotels"],
            "id": 2,
            "text": "Ea cillum incididunt consequat ullamco nisi aute labore cupidatat exercitation et sunt nostrud. Occaecat elit tempor ex anim non nulla sit culpa ipsum aliquip. In amet in Lorem ut enim. Consectetur ea officia reprehenderit pariatur magna eiusmod voluptate. Nostrud labore id adipisicing culpa sunt veniam qui deserunt magna sint mollit. Cillum irure pariatur occaecat amet reprehenderit nisi qui proident aliqua.",
            "likes": 104,
            "reads": 200,
            "popularity": 0.7,
            "createdAt": SYSTEM_TIME,
            "updatedAt": SYSTEM_TIME,
        },
        {
            "tags": ["travel", "airbnb", "vacation"],
            "id": 3,
            "text": "Voluptate consequat minim commodo nisi minim ut. Exercitation incididunt eiusmod qui duis enim sunt dolor sit nisi laboris qui enim mollit. Proident pariatur elit est elit consectetur. Velit anim eu culpa adipisicing esse consequat magna. Id do aliquip pariatur laboris consequat cupidatat voluptate incididunt sint ea.",
            "likes": 10,
            "reads": 32,
            "popularity": 0.7,
            "createdAt": SYSTEM_TIME,
            "updatedAt": SYSTEM_TIME,
        },
    ],
}

updated_post = {
    "post": {
        "authorIds": [1, 5],
        "createdAt": SYSTEM_TIME,
        "id": 1,
        "likes": 12,
        "popularity": 0.19,
        "reads": 5,
        "tags": ["travel", "vacation"],
        "text": "my text",
        "updatedAt": SYSTEM_TIME,
    },
}
