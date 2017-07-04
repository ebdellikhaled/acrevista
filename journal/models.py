from django.db import models
from django.contrib.auth.models import User
from .validators import FileValidator


def user_id_path(instance, filename):
    return "papers/{0}_{3}/{1}/{2}".format(instance.user.id, instance.title, filename, instance.user.username)


class Paper(models.Model):
    user = models.ForeignKey(User, related_name='papers')
    title = models.CharField(max_length=64, blank=False)
    description = models.TextField(max_length=2000, blank=False)
    # File validator.
    validate_file = FileValidator(max_size=1024 * 1024 * 50,  # Max size is 50Mb
                                  content_types=('application/pdf', 'text/html', 'application/msword',
                                                 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                                                 'application/vnd.ms-powerpoint',
                                                 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
                                                 'text/plain',))
    manuscript = models.FileField(upload_to=user_id_path, blank=False, validators=[validate_file])
    cover_letter = models.FileField(upload_to=user_id_path, blank=False, validators=[validate_file])
    supplementary_materials = models.FileField(upload_to=user_id_path, null=True, default=None,
                                               validators=[validate_file])
