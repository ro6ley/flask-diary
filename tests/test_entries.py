def test_main_route_status_code(client):
    route = "/"
    resp = client.get(route)
    assert resp.status_code == 200


def test_entry_create(client, init_db):
    resp = client.post("/entries", json={
        "title": "Test title",
        "content": "Test content"
    })

    assert resp.get_json().get("title") == "Test title"
    assert resp.status_code == 200


def test_entry_create_without_title(client, init_db):
    resp = client.post("/entries", json={
        "content": "Test content"
    })

    assert resp.status_code == 400


def test_list_entries(client, init_db):
    resp = client.get("/entries")

    assert resp.status_code == 200
    assert len(resp.get_json()) == 2


def test_update_entry(client, init_db):
    resp_1 = client.patch("/entries/1", json={
        "title": "Updated title"
    })
    assert resp_1.status_code == 200

    resp_2 = client.get("/entries/1")

    assert resp_2.status_code == 200
    assert resp_2.get_json().get("title") == "Updated title"


def test_delete_entry(client, init_db):
    resp_1 = client.delete("/entries/2")
    assert resp_1.status_code == 204

    resp_2 = client.get("/entries/2")
    assert resp_2.status_code == 404


def test_missing_entry(client, init_db):
    resp_1 = client.patch("/entries/3", json={
        "title": "Updated title"
    })
    assert resp_1.status_code == 404

    resp_2 = client.delete("/entries/3")
    assert resp_2.status_code == 404
