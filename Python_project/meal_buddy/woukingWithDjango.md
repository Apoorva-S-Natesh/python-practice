In Django, the core pattern is **MTV** – **Model, Template, View** 

### 🔁 **High-Level MTV Flow**

1. **User requests a URL** → Django routes it using `urls.py`.
2. **View** handles the request:

   * Fetches/updates data using **Model**.
   * Renders output using a **Template**.
3. **Model** talks to the database.
4. **Template** renders HTML with context from the **View**.

---

### 🧠 **Conceptual Starting Point**

Start by thinking of your app's **data** and **user interactions**:

1. **What data is being managed?**

   * → Define **Models** for that data.
2. **What does the user see or do?**

   * → Define **Views** to handle those actions.
3. **What should the UI look like?**

   * → Design **Templates** to render pages.

---

### ⚙️ **Step-by-Step Coordination**

#### 1. **Define Models (models.py)**

* Create classes inheriting from `models.Model`.
* These define your DB schema.

```python
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

* Run `makemigrations` and `migrate` to apply.

#### 2. **Create Views (views.py)**

* Fetch or process data using the model.
* Return a `HttpResponse` or `render()` to a template.

```python
from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
```

#### 3. **Configure URLs (urls.py)**

* Connect URLs to views.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
```

#### 4. **Design Templates (templates/)**

* Create HTML files using Django's template language.
* Use variables and loops passed from the view.

```html
<!-- blog/post_list.html -->
{% for post in posts %}
  <h2>{{ post.title }}</h2>
  <p>{{ post.content }}</p>
{% endfor %}
```
