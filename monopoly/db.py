from sqlalchemy import create_engine, Column, Integer, String, Boolean, LargeBinary
from sqlalchemy.orm import declarative_base, sessionmaker
import pickle
from player import Player

# SQLite DB URL
DB_URL = "sqlite:///monopoly.db"

engine = create_engine(DB_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

class PlayerModel(Base):
    __tablename__ = "players"

    name = Column(String, primary_key=True, index=True)
    money = Column(Integer, nullable=False, default=1500)
    position = Column(Integer, nullable=False, default=0)
    properties = Column(LargeBinary)  # pickled list[Tile]
    in_jail = Column(Boolean, default=False)
    jail_turns = Column(Integer, default=0)

def init_db():
    Base.metadata.create_all(bind=engine)
    print("✅ Database setup complete!")

def save_player(player: Player):
    session = SessionLocal()
    try:
        db_player = session.get(PlayerModel, player.name)
        if not db_player:
            db_player = PlayerModel(name=player.name)

        db_player.money = player.money
        db_player.position = player.position
        db_player.properties = pickle.dumps(player.properties) if player.properties is not None else None
        db_player.in_jail = player.in_jail
        db_player.jail_turns = player.jail_turns

        session.add(db_player)
        session.commit()
    finally:
        session.close()

def load_players():
    session = SessionLocal()
    players = []
    try:
        for row in session.query(PlayerModel).all():
            p = Player(row.name, row.money)
            p.position = row.position
            p.properties = pickle.loads(row.properties) if row.properties else []
            p.in_jail = row.in_jail
            p.jail_turns = row.jail_turns
            players.append(p)
    finally:
        session.close()
    return players
