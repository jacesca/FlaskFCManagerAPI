from db import db


class TeamsManager(db.Model):
    __tablename__ = "teams_managers"

    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"))
    manager_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __repr__(self):
        return f"Team {self.id} - {self.team_id}/{self.manager_id}"
