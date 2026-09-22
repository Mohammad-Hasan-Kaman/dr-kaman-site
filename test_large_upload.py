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

# Test 5MB
r = c.get("/admin/videos/videowork/add/", HTTP_HOST="drkaman.ir")
print("GET:", r.status_code)

csrf_match = re.search(r'csrfmiddlewaretoken.*?value="([^"]+)"', r.content.decode())
csrf = csrf_match.group(1) if csrf_match else None
print("CSRF:", csrf[:20] if csrf else "NONE")

if csrf:
    content = b'x' * 5_000_000
    f = SimpleUploadedFile("test_5mb.mp4", content, content_type="video/mp4")
    r2 = c.post("/admin/videos/videowork/add/", {"title":"Test 5MB","description":"","video_file":f,"category":"","_save":"Save","csrfmiddlewaretoken":csrf}, HTTP_HOST="drkaman.ir")
    print("POST 5MB:", r2.status_code)
    if r2.status_code != 302:
        print("Error:", r2.content.decode()[:500])

# Test 50MB
content = b'x' * 50_000_000
f = SimpleUploadedFile("test_50mb.mp4", content, content_type="video/mp4")
r2 = c.post("/admin/videos/videowork/add/", {"title":"Test 50MB","description":"","video_file":f,"category":"","_save":"Save","csrfmiddlewaretoken":csrf}, HTTP_HOST="drkaman.ir")
print("POST 50MB:", r2.status_code)
if r2.status_code != 302:
    print("Error:", r2.content.decode()[:500])

# Test 100MB
content = b'x' * 100_000_000
f = SimpleUploadedFile("test_100mb.mp4", content, content_type="video/mp4")
r2 = c.post("/admin/videos/videowork/add/", {"title":"Test 100MB","description":"","video_file":f,"category":"","_save":"Save","csrfmiddlewaretoken":csrf}, HTTP_HOST="drkaman.ir")
print("POST 100MB:", r2.status_code)
if r2.status_code != 302:
    print("Error:", r2.content.decode()[:500])