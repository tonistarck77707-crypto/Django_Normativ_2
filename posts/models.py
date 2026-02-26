from django.db import models


class PostQuerySet(models.QuerySet):
    def delete(self):
        """QuerySet delete() buyuruq bersa, soft delete ishlasin"""
        return super().update(is_deleted=True)

    def hard_delete(self):
        """Butunlay o'chirish"""
        return super().delete()


class DeletedManager(models.Manager):
    def get_queryset(self):
        """Default queryset shu buyuruq kelsa is_deleted=False obyektlarni tiklaydi"""
        return PostQuerySet(self.model, using=self._db).filter(is_deleted=False)


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)


    objects = DeletedManager()
    all_objects = models.Manager()

    # Instance-level delete
    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()

    def hard_delete(self):
        """Instance’ni  borligicha o'chirish"""
        super(Post, self).delete()

    def __str__(self):
        return self.title