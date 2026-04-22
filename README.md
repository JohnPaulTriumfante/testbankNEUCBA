# Test Bank System v2 - Enhanced Edition

A professional test management system with EXAM and REVIEW modes, hierarchical subject/topic/chapter organization, and support for multiple question types.

## 🎯 Key Features

### **REVIEW Mode** 📖
- Per-question timer (customizable: 10-300 seconds)
- Instant answer reveal after each question
- Immediate feedback with explanations
- No scoring pressure - pure learning environment
- Random question selection from chosen chapter

### **EXAM Mode** ⏱️
- Total time limit for entire exam (configurable)
- No answer reveals during exam
- Automatic scoring for multiple-choice questions
- Detailed results shown after submission
- Support for both objective and descriptive questions

### **Question Types**
- **Multiple Choice**: Auto-graded with immediate feedback
- **Descriptive**: Model answer shown after exam, designed for manual instructor review

### **Hierarchical Organization**
```
Subject (e.g., Accounting Fundamentals)
├── Topic (e.g., Financial Statements)
│   ├── Chapter 1: Balance Sheet
│   └── Chapter 2: Income Statement
└── Topic (e.g., Journal Entries)
    ├── Chapter 3: Recording Transactions
    └── Chapter 4: Adjusting Entries
```

## 🚀 Quick Start

### Installation

```bash
cd testbanksystem_v2

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install flask reportlab python-docx

# Initialize database
python database.py

# Run application
python app.py
```

✅ Application starts at: **http://localhost:5001**

## 📋 Database Schema (v2 Enhancements)

### New Tables

| Table | Purpose |
|-------|---------|
| `subjects` | Top-level course categories (NEW) |
| `topics` | Sub-categories under subjects (NEW) |
| `chapters` | Study units linked to topics (MODIFIED) |
| `problems` | Problems/scenarios within chapters |
| `questions` | Individual questions with type field (MODIFIED) |
| `choices` | Answer options for MC questions |
| `review_history` | Review session records (NEW) |
| `exam_history` | Exam session records with scores (MODIFIED) |

### Question Types

```sql
-- question_type field in questions table:
'multiple_choice'  -- Has A, B, C, D choices; auto-graded
'descriptive'      -- Text-based answer; shown for manual review
```

## 🎮 User Flow

### Review Mode Workflow
```
1. Home page → Click "Start Review"
2. Select Subject → Topic → Chapter
3. Configure settings:
   - Number of questions (randomized)
   - Timer per question (seconds)
4. Answer question within timer
5. Auto/manual submit → See answer + explanation
6. Progress to next question
7. Repeat until all questions reviewed
```

### Exam Mode Workflow
```
1. Home page → Click "Take Exam"
2. Select Subject → Topic → Chapter
3. Configure settings:
   - Number of questions
   - Total time limit (minutes)
4. Answer ALL questions
5. Submit exam when ready (or timeout)
6. View score (MC only)
7. Review all answers with model answers
```

## ⏱️ Timer Implementation

### Review Mode: Per-Question Timer
- **User Controls**: Choose duration for each question (10-300 seconds)
- **Visual Feedback**: Countdown display, color changes to red at ≤10s
- **Auto-Submit**: Automatically submits answer when time expires
- **Purpose**: Build time management skills, practice speed

### Exam Mode: Total Time Limit
- **Fixed Duration**: Selected during exam setup
- **Header Display**: Always visible countdown in red
- **Critical Alert**: Header pulses when <5 minutes remain
- **Auto-Submit**: Entire exam submitted when time expires
- **Purpose**: Simulate real exam conditions, enforce time limits

## 📊 Scoring System

### Multiple-Choice Questions
- ✓ Correct answer = 1 point
- ✗ Incorrect/blank = 0 points
- **Score Calculation**: (Correct Answers / Total MC Questions) × 100%

### Descriptive Questions
- ⚠️ **Not auto-graded**
- User answer displayed alongside model answer
- Designed for instructor manual review
- Shows critical thinking, writing ability, detailed explanations

### Performance Feedback
| Score | Performance |
|-------|-------------|
| 90%+ | Excellent 🌟 |
| 80-89% | Very Good 👏 |
| 70-79% | Good 👍 |
| 60-69% | Passing ✓ |
| <60% | Needs Improvement |

## 🔧 Architecture

### Backend Routes

```
GET  /                      - Mode selector
GET  /review                - Review chapter picker
POST /review/start          - Start review session
GET  /exam                  - Exam chapter picker
POST /exam/start            - Start exam session
POST /exam/submit           - Grade exam, return results

GET  /api/subjects          - List all subjects
GET  /api/topics/<id>       - Get topics for subject
GET  /api/chapters/<id>     - Get chapters for topic

GET  /admin/subjects        - Admin panel
POST /admin/subjects        - Create/delete subjects/topics
```

### Technology Stack
- **Backend**: Flask (Python)
- **Frontend**: Bootstrap 5 + Vanilla JavaScript
- **Database**: SQLite3 with cascading deletes
- **Documents**: ReportLab (PDF), python-docx (Word)

## 🎓 Usage Recommendations

### For Accounting Courses

**Organizational Structure**
```
Subject: Financial Accounting
├── Topic: Balance Sheet & Assets
│   ├── Chapter 1: Cash & Receivables
│   ├── Chapter 2: Inventory
│   └── Chapter 3: Fixed Assets
├── Topic: Liabilities & Equity
│   ├── Chapter 4: Current Liabilities
│   └── Chapter 5: Long-term Debt
```

**Assessment Strategy**
- **Chapter Reviews**: 10-15 MC questions, 3-min per question
- **Topic Practice**: 20-25 MC + 2 descriptive, 30-min total
- **Midterm Exam**: 35 MC questions, 60 minutes
- **Final Exam**: 40 MC + 2 essays, 90 minutes

### For Students

**REVIEW Mode** (Learning)
- ✓ Use during studying
- ✓ Take your time reading explanations
- ✓ Focus on understanding concepts
- ✓ Compare your answer to model answer

**EXAM Mode** (Assessment)
- ✓ Simulate real test conditions
- ✓ Practice time management
- ✓ Don't look up answers
- ✓ Review results after exam

## 🔄 Running Both Versions

You can run both systems simultaneously:

```bash
# Terminal 1 - Original (Port 5000)
cd testbanksystem
python app.py

# Terminal 2 - Enhanced v2 (Port 5001)
cd testbanksystem/testbanksystem_v2
python app.py
```

- **v1**: http://127.0.0.1:5000
- **v2**: http://127.0.0.1:5001

Each has separate:
- Database (`testbank.db`)
- Generated files
- Template files

## ✨ v2 Improvements Over v1

| Feature | v1 | v2 |
|---------|----|----|
| Organization | Flat chapters | Subject → Topic → Chapter |
| Modes | Export only | REVIEW + EXAM modes |
| Timers | None | Per-question + total time |
| Question Types | MC only | MC + Descriptive |
| Auto-Grading | None | MC only in EXAM mode |
| Feedback | None | Instant in REVIEW mode |
| Results | None | Detailed scoring page |

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Database error on startup | Delete `testbank.db`, run `python database.py` |
| "No questions found" | Add questions to chapter first |
| Timer stuck | Refresh page, check browser console |
| Choices not shuffling | Ensure all MC questions have 4 choices (A, B, C, D) |
| Can't select chapter | Ensure subject/topic/chapter hierarchy is created |

## 📋 Admin Setup Checklist

- [ ] Create at least one Subject
- [ ] Add at least one Topic to subject
- [ ] Create chapters in topics
- [ ] Import or manually add questions to chapters
- [ ] Set question_type for each question
- [ ] Add explanations and model answers
- [ ] Test REVIEW mode with sample questions
- [ ] Configure exam settings (time limits)
- [ ] Test EXAM mode before deploying to students

## 📝 FAQ

**Q: Can I mix multiple-choice and descriptive questions in one exam?**
A: Yes! Both types are supported. MC auto-grades, descriptive shows model answer.

**Q: What happens if a student runs out of time?**
A: Exam/review automatically submits with whatever answers they provided.

**Q: Can I export exams from v2?**
A: Current version shows results on screen. PDF/Word export coming in future version.

**Q: How do I migrate questions from v1?**
A: Export v1 database, write import script, or manually recreate in v2.

**Q: Can students retake exams?**
A: Yes - each exam session is independent. No limit on retakes.

**Q: Are answers stored?**
A: Currently displayed on screen only. Implement save-to-database for future record-keeping.

## 🔐 Security Considerations

Before deploying to production:
- [ ] Add user authentication
- [ ] Validate all inputs server-side
- [ ] Store exam results in database
- [ ] Implement session management
- [ ] Use HTTPS
- [ ] Sanitize all user input
- [ ] Add CSRF protection
- [ ] Rate limit API endpoints

## 📦 Dependencies

```
Flask==2.3.0
reportlab==4.0.0
python-docx==0.8.11
Werkzeug==2.3.0
```

## 📄 License

Internal use - Accounting Department only

## 📞 Support

For issues or questions, contact your system administrator.

---

**Last Updated**: April 2026  
**Version**: 2.0 - Initial Release
- ✅ Search and filter questions
- ✅ Exam history tracking
- ✅ Delete chapters with cascading cleanup

## Future Enhancements (To Be Added)

Plan your additional features here:
- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3

## Project Structure

```
testbanksystem_v2/
├── app.py              # Main Flask application
├── database.py         # Database schema and initialization
├── templates/          # HTML templates (to be copied)
├── generated_exams/    # Folder for exported exams
├── testbank.db         # SQLite database
└── README.md           # This file
```

## Notes

- This v2 is a fresh start with its own database
- You'll need to copy template files from the original to make it fully functional
- The port is set to 5001 to avoid conflicts
- Both versions can be developed independently
