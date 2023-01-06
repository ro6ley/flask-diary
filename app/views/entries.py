from datetime import datetime
from flask import views, jsonify, make_response, abort, request

from app.models import Entry
from app import db


class EntryView(views.MethodView):
    def get(self, entry_id=None):
        """List all diary entries or return the entry matching the ID provided """
        if not entry_id:
            # TODO: pagination
            entries = [e.to_dict() for e in Entry.query.all()]
            return make_response(jsonify(entries), 200)
        else:
            entry = db.session.get(Entry, entry_id)
            if not entry:
                return abort(404)
            return make_response(jsonify(entry.to_dict()), 200)

    def post(self):
        """ Create a single entry """
        request_data = request.get_json()

        if not request_data.get("title"):
            return abort(400)

        new_entry = Entry(title=request_data.get("title"), content=request_data.get("content"), created_at=datetime.utcnow())
        db.session.add(new_entry)
        db.session.commit()

        return make_response(jsonify(new_entry.to_dict()), 200)


    def patch(self, entry_id):
        """ Update a single entry """
        entry = db.session.get(Entry, entry_id)
        if not entry:
            return abort(404)

        entry.title = request.get_json().get("title", entry.title)
        entry.content = request.get_json().get("content", entry.content)
        db.session.commit()

        return make_response(jsonify(entry.to_dict()), 200)


    def delete(self, entry_id):
        """ Delete a single entry """
        entry = db.session.get(Entry, entry_id)
        if not entry:
            return abort(404)

        db.session.delete(entry)
        db.session.commit()

        return make_response(jsonify(entry.to_dict()), 204)
