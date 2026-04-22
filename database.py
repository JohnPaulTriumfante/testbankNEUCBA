import sqlite3

def create_database():
    conn = sqlite3.connect("testbank.db")
    cursor = conn.cursor()

    # Enable foreign keys
    cursor.execute("PRAGMA foreign_keys = ON")

    # Drop tables in correct order
    cursor.execute("DROP TABLE IF EXISTS exam_history")
    cursor.execute("DROP TABLE IF EXISTS review_history")
    cursor.execute("DROP TABLE IF EXISTS choices")
    cursor.execute("DROP TABLE IF EXISTS questions")
    cursor.execute("DROP TABLE IF EXISTS problems")
    cursor.execute("DROP TABLE IF EXISTS chapters")
    cursor.execute("DROP TABLE IF EXISTS topics")
    cursor.execute("DROP TABLE IF EXISTS subjects")

    # 1️⃣ Subjects table
    cursor.execute("""
        CREATE TABLE subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        );
    """)

    # 2️⃣ Topics table
    cursor.execute("""
        CREATE TABLE topics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            description TEXT,
            FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE
        );
    """)

    # 3️⃣ Chapters table (now linked to topics)
    cursor.execute("""
        CREATE TABLE chapters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id INTEGER NOT NULL,
            chapter_number INTEGER NOT NULL,
            chapter_title TEXT NOT NULL,
            FOREIGN KEY (topic_id) REFERENCES topics(id) ON DELETE CASCADE
        );
    """)

    # 4️⃣ Question Groups table (question numbers like "2-3")
    cursor.execute("""
        CREATE TABLE question_groups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chapter_id INTEGER NOT NULL,
            question_number TEXT NOT NULL,   -- 1-1, 2-3, 3-5, etc.
            section TEXT,                    -- optional (Basic, Comprehensive)
            standard TEXT,                   -- IFRS, AICPA, AICA, etc.
            FOREIGN KEY (chapter_id) REFERENCES chapters(id) ON DELETE CASCADE
        );
    """)

    # 5️⃣ Questions table (now with question_type)
    cursor.execute("""
        CREATE TABLE questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_group_id INTEGER NOT NULL,
            question_text TEXT NOT NULL,
            correct_choice TEXT NOT NULL,
            explanation TEXT,
            question_type TEXT DEFAULT 'multiple_choice',
            FOREIGN KEY (question_group_id) REFERENCES question_groups(id) ON DELETE CASCADE
        );
    """)

    # 6️⃣ Choices table
    cursor.execute("""
        CREATE TABLE choices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_id INTEGER NOT NULL,
            choice_label TEXT NOT NULL,
            choice_text TEXT NOT NULL,
            FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE
        );
    """)

    # 7️⃣ Review History table (for REVIEW mode sessions)
    cursor.execute("""
        CREATE TABLE review_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chapter_id INTEGER NOT NULL,
            filename TEXT NOT NULL,
            file_path TEXT NOT NULL,
            created_date TEXT NOT NULL,
            num_questions INTEGER NOT NULL,
            timer_per_question INTEGER,
            FOREIGN KEY (chapter_id) REFERENCES chapters(id) ON DELETE CASCADE
        );
    """)

    # 8️⃣ Exam History table (for EXAM mode sessions)
    cursor.execute("""
        CREATE TABLE exam_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chapter_id INTEGER NOT NULL,
            filename TEXT NOT NULL,
            file_path TEXT NOT NULL,
            created_date TEXT NOT NULL,
            num_questions INTEGER NOT NULL,
            total_time_limit INTEGER,
            score INTEGER,
            FOREIGN KEY (chapter_id) REFERENCES chapters(id) ON DELETE CASCADE
        );
    """)

    conn.commit()
    conn.close()
    print("Database recreated successfully.")


if __name__ == "__main__":
    create_database()
