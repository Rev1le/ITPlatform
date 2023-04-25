from app.db import entities, mentors_table, database


async def create_mentor(mentor: entities.Mentor):
    query = mentors_table\
        .insert()\
        .values(mentor.dict())

    database.execute(query)