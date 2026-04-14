"""
HTML templates for the vulnerable web application UI.
Barebones, light theme.
"""

COMMON_STYLE = """
<style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        background: #f5f5f5;
        color: #222;
        min-height: 100vh;
    }
    nav {
        background: #fff;
        border-bottom: 1px solid #ddd;
        padding: 12px 24px;
        display: flex;
        align-items: center;
        gap: 24px;
    }
    nav a {
        color: #333;
        text-decoration: none;
        font-size: 14px;
        font-weight: 500;
    }
    nav a:hover { color: #000; text-decoration: underline; }
    nav .brand { font-weight: 700; font-size: 16px; color: #000; }
    .container {
        max-width: 560px;
        margin: 40px auto;
        background: #fff;
        border: 1px solid #ddd;
        border-radius: 6px;
        padding: 32px;
    }
    h1 {
        font-size: 20px;
        margin-bottom: 20px;
        font-weight: 600;
    }
    label {
        display: block;
        font-size: 13px;
        font-weight: 500;
        margin-bottom: 4px;
        color: #444;
    }
    input[type="text"],
    input[type="password"],
    input[type="file"] {
        width: 100%;
        padding: 8px 10px;
        border: 1px solid #ccc;
        border-radius: 4px;
        font-size: 14px;
        margin-bottom: 16px;
        background: #fafafa;
    }
    input:focus {
        outline: none;
        border-color: #888;
    }
    button {
        background: #222;
        color: #fff;
        border: none;
        padding: 9px 20px;
        border-radius: 4px;
        font-size: 14px;
        cursor: pointer;
        font-weight: 500;
    }
    button:hover { background: #444; }
    .result {
        margin-top: 20px;
        padding: 12px;
        background: #f9f9f9;
        border: 1px solid #eee;
        border-radius: 4px;
        font-size: 13px;
        white-space: pre-wrap;
        word-break: break-all;
        display: none;
    }
    .result.show { display: block; }
    .result.error { border-color: #e55; background: #fff5f5; }
    .result.success { border-color: #5a5; background: #f5fff5; }
</style>
"""

NAV = """
<nav>
    <span class="brand">Student Mgmt</span>
    <a href="/">Home</a>
    <a href="/login">Login</a>
    <a href="/profile">Profile</a>
    <a href="/update-role">Update Role</a>
    <a href="/upload">Upload</a>
    <a href="/download">Download</a>
</nav>
"""


def home_page():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Management System</title>
    {COMMON_STYLE}
    <style>
        .home-container {{
            max-width: 560px;
            margin: 60px auto;
            background: #fff;
            border: 1px solid #ddd;
            border-radius: 6px;
            padding: 40px 32px;
            text-align: center;
        }}
        .home-container h1 {{ font-size: 22px; margin-bottom: 8px; }}
        .home-container p {{ color: #666; font-size: 14px; margin-bottom: 28px; }}
        .links {{ display: flex; flex-direction: column; gap: 10px; align-items: center; }}
        .links a {{
            display: block;
            width: 220px;
            padding: 10px;
            background: #222;
            color: #fff;
            text-decoration: none;
            border-radius: 4px;
            font-size: 14px;
            font-weight: 500;
        }}
        .links a:hover {{ background: #444; }}
    </style>
</head>
<body>
    {NAV}
    <div class="home-container">
        <h1>Student Management System</h1>
        <p>Vulnerable web app — for educational purposes only.</p>
        <div class="links">
            <a href="/login">Login</a>
            <a href="/profile">View Profile</a>
            <a href="/update-role">Update Role</a>
            <a href="/upload">Upload File</a>
            <a href="/download">Download File</a>
        </div>
    </div>
</body>
</html>"""


def login_page():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    {COMMON_STYLE}
</head>
<body>
    {NAV}
    <div class="container">
        <h1>Login</h1>
        <form id="loginForm">
            <label for="username">Username</label>
            <input type="text" id="username" name="username" placeholder="Enter username" required>
            <label for="password">Password</label>
            <input type="password" id="password" name="password" placeholder="Enter password" required>
            <button type="submit">Login</button>
        </form>
        <div id="result" class="result"></div>
    </div>
    <script>
        document.getElementById('loginForm').addEventListener('submit', async (e) => {{
            e.preventDefault();
            const res = document.getElementById('result');
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            try {{
                const response = await fetch('/login', {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify({{ username, password }})
                }});
                const data = await response.json();
                res.className = response.ok ? 'result show success' : 'result show error';
                res.textContent = JSON.stringify(data, null, 2);
            }} catch (err) {{
                res.className = 'result show error';
                res.textContent = err.message;
            }}
        }});
    </script>
</body>
</html>"""


def profile_page():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>View Profile</title>
    {COMMON_STYLE}
</head>
<body>
    {NAV}
    <div class="container">
        <h1>View Profile</h1>
        <form id="profileForm">
            <label for="username">Username</label>
            <input type="text" id="username" name="username" placeholder="Enter username" required>
            <button type="submit">Get Profile</button>
        </form>
        <div id="result" class="result"></div>
    </div>
    <script>
        document.getElementById('profileForm').addEventListener('submit', async (e) => {{
            e.preventDefault();
            const res = document.getElementById('result');
            const username = document.getElementById('username').value;
            try {{
                const response = await fetch('/profile/' + encodeURIComponent(username));
                const data = await response.json();
                res.className = response.ok ? 'result show success' : 'result show error';
                res.textContent = JSON.stringify(data, null, 2);
            }} catch (err) {{
                res.className = 'result show error';
                res.textContent = err.message;
            }}
        }});
    </script>
</body>
</html>"""


def update_role_page():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Update Role</title>
    {COMMON_STYLE}
</head>
<body>
    {NAV}
    <div class="container">
        <h1>Update Role</h1>
        <form id="roleForm">
            <label for="username">Username</label>
            <input type="text" id="username" name="username" placeholder="Enter username" required>
            <label for="role">New Role</label>
            <input type="text" id="role" name="role" placeholder="e.g. admin, student" required>
            <button type="submit">Update Role</button>
        </form>
        <div id="result" class="result"></div>
    </div>
    <script>
        document.getElementById('roleForm').addEventListener('submit', async (e) => {{
            e.preventDefault();
            const res = document.getElementById('result');
            const username = document.getElementById('username').value;
            const role = document.getElementById('role').value;
            try {{
                const response = await fetch('/profile/update-role', {{
                    method: 'PUT',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify({{ username, role }})
                }});
                const data = await response.json();
                res.className = response.ok ? 'result show success' : 'result show error';
                res.textContent = JSON.stringify(data, null, 2);
            }} catch (err) {{
                res.className = 'result show error';
                res.textContent = err.message;
            }}
        }});
    </script>
</body>
</html>"""


def upload_page():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload File</title>
    {COMMON_STYLE}
</head>
<body>
    {NAV}
    <div class="container">
        <h1>Upload File</h1>
        <form id="uploadForm">
            <label for="file">Choose file</label>
            <input type="file" id="file" name="file" required>
            <button type="submit">Upload</button>
        </form>
        <div id="result" class="result"></div>
    </div>
    <script>
        document.getElementById('uploadForm').addEventListener('submit', async (e) => {{
            e.preventDefault();
            const res = document.getElementById('result');
            const fileInput = document.getElementById('file');
            const formData = new FormData();
            formData.append('file', fileInput.files[0]);
            try {{
                const response = await fetch('/upload', {{
                    method: 'POST',
                    body: formData
                }});
                const data = await response.json();
                res.className = response.ok ? 'result show success' : 'result show error';
                res.textContent = JSON.stringify(data, null, 2);
            }} catch (err) {{
                res.className = 'result show error';
                res.textContent = err.message;
            }}
        }});
    </script>
</body>
</html>"""


def download_page():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Download File</title>
    {COMMON_STYLE}
</head>
<body>
    {NAV}
    <div class="container">
        <h1>Download File</h1>
        <form id="downloadForm">
            <label for="filename">Filename</label>
            <input type="text" id="filename" name="filename" placeholder="e.g. report.pdf" required>
            <button type="submit">Download</button>
        </form>
        <div id="result" class="result"></div>
    </div>
    <script>
        document.getElementById('downloadForm').addEventListener('submit', async (e) => {{
            e.preventDefault();
            const res = document.getElementById('result');
            const filename = document.getElementById('filename').value;
            try {{
                const response = await fetch('/download/' + filename);
                if (!response.ok) {{
                    const data = await response.json();
                    res.className = 'result show error';
                    res.textContent = JSON.stringify(data, null, 2);
                    return;
                }}
                // trigger download
                const blob = await response.blob();
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = filename;
                a.click();
                URL.revokeObjectURL(url);
                res.className = 'result show success';
                res.textContent = 'Download started.';
            }} catch (err) {{
                res.className = 'result show error';
                res.textContent = err.message;
            }}
        }});
    </script>
</body>
</html>"""
