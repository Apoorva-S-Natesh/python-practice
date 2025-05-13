You can hide sensitive information like API keys and secrets by using environment variables and configuring `.env` files. Here’s how to do it effectively in a Django project:

### ✅ **Step 1: Install `python-decouple`**

Run the following command to install `python-decouple`:

```bash
pip install python-decouple
```

---

### ✅ **Step 2: Create a `.env` File**

In the root of your project (where `manage.py` is located), create a `.env` file:

```
E:\Python\Python_project\meal_buddy\.env
```

Add your sensitive information to the `.env` file:

```env
RAZORPAY_API_KEY=your_api_key_here
RAZORPAY_SECRET_KEY=your_secret_key_here
```

---

### ✅ **Step 3: Update `settings.py` to Use Environment Variables**

In your `settings.py`, import `config` from `decouple` and update the Razorpay configuration:

```python
from decouple import config

RAZORPAY_API_KEY = config('RAZORPAY_API_KEY')
RAZORPAY_SECRET_KEY = config('RAZORPAY_SECRET_KEY')
```

---

### ✅ **Step 4: Add `.env` to `.gitignore`**

In the root of your project, locate (or create) a `.gitignore` file and add the following line:

```
.env
```

---

### ✅ **Step 5: Secure Existing Keys**

If you have already committed your API keys to the repository, follow these steps to remove them:

1. Remove the keys from the `settings.py` file.
2. Add the `.env` file to `.gitignore`.
3. Remove the `.env` file from Git’s tracking:

```bash
git rm --cached .env
```

4. Commit the changes:

```bash
git commit -m "Remove .env from tracking and update settings.py"
```

5. Push the changes:

```bash
git push
```

---

### ✅ **Step 6: Access `.env` in Production (Optional)**

In production, ensure that the `.env` file is present and that `python-decouple` is installed. Configure the environment variables in your server (e.g., using Docker, Heroku, or environment settings).
