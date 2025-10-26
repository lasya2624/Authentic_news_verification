from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    category = models.CharField(max_length=100, default='General')
    source_url = models.URLField()
    image_url = models.URLField(null=True, blank=True,default ='')
    publication_date = models.DateTimeField(null=True)
    credibility_score = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)
    verified_at = models.DateTimeField(null=True, blank=True)
    image_analysis_score = models.IntegerField(default=0)
    source_name = models.CharField(max_length=100, default='Unknown')
    verified_by_sources = models.CharField(max_length=500, default='Not available')
    email_sent = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            models.Index(fields=["-publication_date"]),
            models.Index(fields=["-verified_at"]),
            models.Index(fields=["is_verified"]),
        ]  # ← FIXED: Added closing bracket

class UserSubscription(models.Model):  # ← Now properly outside Meta
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_subscribed = models.BooleanField(default=False)
    subscribed_categories = models.CharField(max_length=255, default='')

    def __str__(self):
        return f"{self.user.username} Subscription"

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    reason = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for {self.article.title} by {self.user.username if self.user else 'Anonymous'}"
    

class Meta:
    indexes = [
        models.Index(fields=["-publication_date"]),
        models.Index(fields=["-verified_at"]),
        models.Index(fields=["is_verified"]),
    ]
    constraints = [
        models.UniqueConstraint(
            name="uniq_title_sourceurl",
            fields=["title", "source_url"],
        )
    ]

# from django.db import models

# class Subscriber(models.Model):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=100, blank=True, null=True)
#     last_name = models.CharField(max_length=100, blank=True, null=True)
#     is_active = models.BooleanField(default=True)  # Only active subscribers get emails
#     subscribed_date = models.DateTimeField(auto_now_add=True)
#     categories = models.JSONField(default=list, blank=True)  # Optional: category preferences
    
#     def __str__(self):
#         return f"{self.email} ({'Active' if self.is_active else 'Inactive'})"
    
#     class Meta:
#         ordering = ['-subscribed_date']

# class EmailDigest(models.Model):
#     sent_at = models.DateTimeField(auto_now_add=True)
#     articles_count = models.IntegerField(default=0)
    
#     def __str__(self):
#         return f"Digest: {self.articles_count} articles at {self.sent_at}"