def test_article_create(client, init_db):
    resp = client.post("/categories/1/articles", json={
        "title": "Test article",
        "description": "Test description",
        "url": "google.com"
    })

    assert resp.get_json().get("title") == "Test article"
    assert resp.status_code == 200


def test_article_create_without_title(client, init_db):
    resp = client.post("/categories/1/articles", json={
        "description": "Test content"
    })

    assert resp.status_code == 400


def test_list_articles(client, init_db):
    resp = client.get("/categories/1/articles")

    assert resp.status_code == 200
    assert len(resp.get_json()) == 2


def test_update_article(client, init_db):
    resp_1 = client.patch("/categories/1/articles/1", json={
        "title": "Updated title",
        "read_status": True
    })
    assert resp_1.status_code == 200

    resp_2 = client.get("/categories/1/articles/1")

    assert resp_2.status_code == 200
    assert resp_2.get_json().get("title") == "Updated title"
    assert resp_2.get_json().get("read_status") == True


def test_delete_article(client, init_db):
    resp_1 = client.delete("/categories/1/articles/2")
    assert resp_1.status_code == 204

    resp_2 = client.get("/categories/1/articles/2")
    assert resp_2.status_code == 404


def test_missing_article(client, init_db):
    resp_1 = client.patch("/categories/1/articles/3", json={
        "title": "Updated title"
    })
    assert resp_1.status_code == 404

    resp_2 = client.delete("/categories/1/articles/3")
    assert resp_2.status_code == 404
