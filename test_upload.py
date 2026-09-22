import django
import os
django.setup()
from django.test import Client
from django.core.files.uploadedfile import SimpleUploadedFile
import re

c = Client()
# WARNING: never commit real credentials — export TEST_ADMIN_USER/_PASSWORD locally
c.login(
    username=os.environ.get("TEST_ADMIN_USER", ""),
    password=os.environ.get("TEST_ADMIN_PASSWORD", ""),
)
r = c.get("/admin/videos/videowork/add/", HTTP_HOST="drkaman.ir")
print("GET:", r.status_code)

csrf_match = re.search(r'csrfmiddlewaretoken.*?value="([^"]+)"', r.content.decode())
csrf = csrf_match.group(1) if csrf_match else None
print("CSRF:", csrf[:20] if csrf else "NONE")

if csrf:
    test_content = b"fake mp4 content for testing"
    video_file = SimpleUploadedFile("test.mp4", test_content, content_type="video/mp4")
    post_data = {
        "title": "Test Video",
        "description": "Test",
        "video_file": video_file,
        "category": "",
        "_save": "Save",
        "csrfmiddlewaretoken": csrf
    }
    r2 = c.post("/admin/videos/videowork/add/", post_data, HTTP_HOST="drkaman.ir")
    print("POST:", r2.status_code)
    if r2.status_code != 302:
        print("Error content:", r2.content.decode()[:2000])
else:
    print("No CSRF token")