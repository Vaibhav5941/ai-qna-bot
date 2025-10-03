# 🔧 Troubleshooting Guide

This guide covers common issues you might encounter while setting up and running the AI Q&A Bot, along with their solutions.

## Table of Contents
- [Installation Issues](#installation-issues)
- [API Key Problems](#api-key-problems)
- [Runtime Errors](#runtime-errors)
- [Streamlit Issues](#streamlit-issues)
- [Deployment Problems](#deployment-problems)
- [Performance Issues](#performance-issues)

---

## 🔨 Installation Issues

### Problem: `python: command not found`

**Symptoms:**
```bash
$ python app.py
bash: python: command not found
```

**Solutions:**

1. **Try `python3` instead:**
   ```bash
   python3 app.py
   ```

2. **Verify Python installation:**
   ```bash
   which python3
   # or on Windows:
   where python
   ```

3. **Reinstall Python:**
   - Download from [python.org](https://www.python.org/downloads/)
   - ✅ Check "Add Python to PATH" during installation
   - Restart your terminal after installation

---

### Problem: `pip: command not found`

**Symptoms:**
```bash
$ pip install -r requirements.txt
bash: pip: command not found
```

**Solutions:**

1. **Try `pip3`:**
   ```bash
   pip3 install -r requirements.txt
   ```

2. **Use Python module:**
   ```bash
   python -m pip install -r requirements.txt
   ```

3. **Install pip manually:**
   ```bash
   # Download get-pip.py
   curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
   python get-pip.py
   ```

---

### Problem: Permission denied during installation

**Symptoms:**
```bash
ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied
```

**Solutions:**

1. **Use a virtual environment (RECOMMENDED):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Install for user only:**
   ```bash
   pip install --user -r requirements.txt
   ```

3. **Use sudo (Linux/Mac, NOT RECOMMENDED):**
   ```bash
   sudo pip install -r requirements.txt
   ```

---

## 🔑 API Key Problems

### Problem: `COHERE_API_KEY not found in .env file`

**Symptoms:**
```
ValueError: COHERE_API_KEY not found in .env file
```

**Solutions:**

1. **Check if `.env` file exists:**
   ```bash
   # On Mac/Linux:
   ls -la | grep .env
   
   # On Windows:
   dir /a
   ```

2. **Create `.env` file if missing:**
   ```bash
   # On Mac/Linux:
   touch .env
   
   # On Windows:
   echo. > .env
   ```

3. **Add your API key to `.env`:**
   ```
   COHERE_API_KEY=your_actual_api_key_here
   ```
   
   ⚠️ **Important**: No spaces around the `=` sign!

4. **Verify the file contents:**
   ```bash
   # On Mac/Linux:
   cat .env
   
   # On Windows:
   type .env
   ```

5. **Check file location:**
   - The `.env` file must be in the same directory as your Python scripts
   - Not in a subdirectory or parent directory

---

### Problem: Invalid API key error

**Symptoms:**
```
cohere.error.CohereAPIError: invalid api token
```

**Solutions:**

1. **Get a new API key:**
   - Go to [cohere.com](https://cohere.com)
   - Sign in to your account
   - Navigate to Dashboard → API Keys
   - Copy the key (click the eye icon to reveal it)

2. **Update your `.env` file:**
   ```
   COHERE_API_KEY=new_api_key_here
   ```

3. **Check for hidden characters:**
   - Make sure there are no spaces before or after the key
   - No quotes around the key value
   - No line breaks in the middle of the key

4. **Verify the key format:**
   - Cohere keys typically start with a specific prefix
   - They're usually quite long (40+ characters)

---

## 🐛 Runtime Errors

### Problem: Module not found error

**Symptoms:**
```python
ModuleNotFoundError: No module named 'cohere'
```

**Solutions:**

1. **Install the missing module:**
   ```bash
   pip install cohere
   # or install all requirements:
   pip install -r requirements.txt
   ```

2. **Check if you're in the right environment:**
   ```bash
   which python  # Should point to your venv if you're using one
   ```

3. **Activate virtual environment:**
   ```bash
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate     # Windows
   ```

4. **Reinstall all dependencies:**
   ```bash
   pip install --force-reinstall -r requirements.txt
   ```

---

### Problem: `Connection Error` or timeout

**Symptoms:**
```
requests.exceptions.ConnectionError: Failed to establish a new connection
```

**Solutions:**

1. **Check internet connection:**
   ```bash
   ping cohere.com
   ```

2. **Check if you're behind a proxy:**
   - If using a corporate network, you may need proxy settings
   - Contact your network administrator

3. **Try a different network:**
   - Switch from WiFi to mobile hotspot or vice versa
   - Some networks block API calls

4. **Check Cohere service status:**
   - Visit Cohere's status page if available
   - Check Cohere's social media for updates

5. **Increase timeout:**
   ```python
   response = client.chat(
       message=question,
       model='command-r-plus',
       timeout=60  # Add timeout parameter
   )
   ```

---

### Problem: Rate limit exceeded

**Symptoms:**
```
cohere.error.CohereAPIError: rate limit exceeded
```

**Solutions:**

1. **Wait before making next request:**
   ```python
   import time
   time.sleep(1)  # Wait 1 second between requests
   ```

2. **Check your Cohere plan limits:**
   - Free tier has limited API calls per minute
   - Upgrade plan if needed

3. **Implement rate limiting in code:**
   ```python
   from time import sleep
   from datetime import datetime
   
   last_request_time = None
   
   def ask_question(client, question):
       global last_request_time
       
       if last_request_time:
           elapsed = (datetime.now() - last_request_time).total_seconds()
           if elapsed < 1:  # Wait at least 1 second between requests
               sleep(1 - elapsed)
       
       response = client.chat(message=question, model='command-r-plus')
       last_request_time = datetime.now()
       return response.text
   ```

---

## 🎨 Streamlit Issues

### Problem: Streamlit not opening in browser

**Symptoms:**
- Command runs but browser doesn't open
- Shows URL but nothing happens

**Solutions:**

1. **Manually open the URL:**
   - Copy the URL from terminal (usually `http://localhost:8501`)
   - Paste in your browser

2. **Check if port is already in use:**
   ```bash
   # Try a different port:
   streamlit run streamlit_app.py --server.port 8502
   ```

3. **Kill existing Streamlit processes:**
   ```bash
   # On Mac/Linux:
   pkill -f streamlit
   
   # On Windows:
   taskkill /F /IM streamlit.exe
   ```

4. **Disable auto-browser opening:**
   ```bash
   streamlit run streamlit_app.py --server.headless true
   ```

---

### Problem: Streamlit app keeps rerunning

**Symptoms:**
- App refreshes constantly
- Infinite loop of reruns

**Solutions:**

1. **Check for file watchers:**
   - Don't edit files while the app is running
   - Save files before running the app

2. **Disable file watcher:**
   ```bash
   streamlit run streamlit_app.py --server.fileWatcherType none
   ```

3. **Check for infinite loops in code:**
   - Make sure you're not calling `st.rerun()` unconditionally
   - Review any loops in your code

---

### Problem: Session state not persisting

**Symptoms:**
- Chat history disappears
- Variables reset unexpectedly

**Solutions:**

1. **Always initialize session state:**
   ```python
   if "messages" not in st.session_state:
       st.session_state.messages = []
   ```

2. **Don't reinitialize within conditionals:**
   ```python
   # BAD:
   if some_condition:
       st.session_state.messages = []  # This resets it!
   
   # GOOD:
   if "messages" not in st.session_state:
       st.session_state.messages = []
   ```

3. **Check Streamlit version:**
   ```bash
   pip install --upgrade streamlit
   ```

---

## 🚀 Deployment Problems

### Problem: Streamlit Community Cloud deployment fails

**Symptoms:**
- Build fails on Streamlit Cloud
- App crashes after deployment
- "App is sleeping" message

**Solutions:**

1. **Check build logs:**
   - Go to Streamlit Community Cloud dashboard
   - Click on your app
   - Check "Manage app" → "Logs" for errors

2. **Verify `requirements.txt`:**
   ```bash
   # Make sure all dependencies are listed:
   pip freeze > requirements.txt
   ```
   
   Your `requirements.txt` should have:
   ```
   cohere
   python-dotenv
   streamlit
   ```

3. **Check Python version:**
   - Streamlit Cloud uses Python 3.9-3.11 by default
   - If you need a specific version, create `.streamlit/config.toml`:
   ```toml
   [server]
   headless = true
   port = 8501
   ```

4. **Verify Secrets (Environment Variables):**
   - Go to Streamlit Cloud dashboard
   - Click on your app → "Settings" → "Secrets"
   - Add your secrets in TOML format:
   ```toml
   COHERE_API_KEY = "your_actual_api_key_here"
   ```
   - ⚠️ No extra spaces, and use quotes around the value

5. **Update your code to read secrets:**
   ```python
   import streamlit as st
   import os
   
   # Try to get from Streamlit secrets first (for cloud deployment)
   try:
       api_key = st.secrets["COHERE_API_KEY"]
   except:
       # Fall back to .env for local development
       from dotenv import load_dotenv
       load_dotenv()
       api_key = os.getenv('COHERE_API_KEY')
   ```

---

### Problem: App works locally but not on Streamlit Cloud

**Symptoms:**
- Works on your computer
- Fails in production
- Module not found errors

**Solutions:**

1. **Check file paths:**
   ```python
   # BAD:
   open('C:\\Users\\MyName\\Desktop\\file.txt')
   
   # GOOD:
   import os
   file_path = os.path.join(os.path.dirname(__file__), 'file.txt')
   open(file_path)
   ```

2. **Environment-specific code:**
   ```python
   import os
   import streamlit as st
   
   # Detect environment
   def is_cloud_deployment():
       return hasattr(st, 'secrets')
   
   if is_cloud_deployment():
       # Production settings (Streamlit Cloud)
       api_key = st.secrets["COHERE_API_KEY"]
   else:
       # Development settings (Local)
       from dotenv import load_dotenv
       load_dotenv()
       api_key = os.getenv('COHERE_API_KEY')
   ```

3. **Don't use `.env` files in deployment:**
   - `.env` files won't work on Streamlit Cloud
   - Always use Streamlit Secrets for sensitive data
   - Make sure `.env` is in `.gitignore` so it doesn't get pushed

4. **Check GitHub repository:**
   - Make sure all necessary files are pushed
   - Verify `.gitignore` is not blocking important files
   - Streamlit Cloud needs: `streamlit_app.py`, `requirements.txt`

---

## ⚡ Performance Issues

### Problem: Slow response times

**Symptoms:**
- Bot takes too long to respond
- Timeout errors

**Solutions:**

1. **Use a faster model:**
   ```python
   # Try command instead of command-r-plus:
   response = client.chat(
       message=question,
       model='command'  # Faster but slightly less capable
   )
   ```

2. **Reduce max tokens:**
   ```python
   response = client.chat(
       message=question,
       model='command-r-plus',
       max_tokens=500  # Limit response length
   )
   ```

3. **Add loading indicators:**
   ```python
   # In Streamlit:
   with st.spinner('Thinking...'):
       response = client.chat(message=prompt, model='command-r-plus')
   ```

4. **Check your internet speed:**
   - Run a speed test
   - Try a different network

---

## 📞 Still Having Issues?

If you're still experiencing problems:

1. **Enable debug mode:**
   ```python
   import logging
   logging.basicConfig(level=logging.DEBUG)
   ```

2. **Check GitHub Issues:**
   - Visit the repository's Issues page
   - Search for similar problems
   - Create a new issue with:
     - Error message (full traceback)
     - Steps to reproduce
     - Your environment details

3. **Community Support:**
   - [Cohere Discord](https://discord.gg/cohere)
   - [Streamlit Community Forum](https://discuss.streamlit.io/)
   - Stack Overflow with tags: `python`, `cohere`, `streamlit`

4. **Provide system information:**
   ```bash
   # Get system info:
   python --version
   pip --version
   pip list
   
   # OS info:
   # On Mac/Linux:
   uname -a
   
   # On Windows:
   systeminfo | findstr /B /C:"OS Name" /C:"OS Version"
   ```

---

## 📝 Reporting Bugs

When reporting issues, please include:

1. **What you were trying to do**
2. **What you expected to happen**
3. **What actually happened**
4. **Full error message** (copy the entire traceback)
5. **Your environment:**
   - Operating system
   - Python version
   - Package versions (`pip list`)
6. **Steps to reproduce** the issue
7. **Any relevant code snippets**

---

**Remember:** Most issues have simple solutions! Don't hesitate to ask for help. The community is here to support you. 🙂

**Good luck with your AI Q&A Bot!** 🚀