from models import Post, session
from pydantic import BaseModel, constr
import bleach

# Pydantic schema
class PostSchema(BaseModel):
    title: constr(min_length=1, max_length=100)
    content: str

# Simulated user input
title = "First Secure Post"
content = "<script>alert('XSS')</script> Welcome!"

# Validate and sanitize
try:
    data = PostSchema(title=title, content=content)
    clean_content = bleach.clean(data.content)

    # Insert using SQLAlchemy
    post = Post(title=data.title, content=clean_content)
    session.add(post)
    session.commit()

    print("✅ Post inserted securely.")
except Exception as e:
    print("❌ Error:", e)
