def test_category_create(client, init_db):
    resp = client.post("/categories", json={
        "name": "Test category",
        "description": "Test description"
    })

    assert resp.get_json().get("name") == "Test category"
    assert resp.status_code == 200


def test_category_create_without_name(client, init_db):
    resp = client.post("/categories", json={
        "description": "Test content"
    })

    assert resp.status_code == 400


def test_list_categories(client, init_db):
    resp = client.get("/categories")

    assert resp.status_code == 200
    assert len(resp.get_json()) == 2


def test_update_category(client, init_db):
    resp_1 = client.patch("/categories/1", json={
        "name": "Updated name"
    })
    assert resp_1.status_code == 200

    resp_2 = client.get("/categories/1")

    assert resp_2.status_code == 200
    assert resp_2.get_json().get("name") == "Updated name"


def test_delete_category(client, init_db):
    resp_1 = client.delete("/categories/2")
    assert resp_1.status_code == 204

    resp_2 = client.get("/categories/2")
    assert resp_2.status_code == 404


def test_missing_category(client, init_db):
    resp_1 = client.patch("/categories/3", json={
        "title": "Updated title"
    })
    assert resp_1.status_code == 404

    resp_2 = client.delete("/categories/3")
    assert resp_2.status_code == 404
