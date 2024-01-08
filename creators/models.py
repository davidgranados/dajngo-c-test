from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel


class Platform(models.TextChoices):
    """
    Platform choices for the Creator model.
    """

    INSTAGRAM = "IG", _("Instagram")
    TIKTOK = "TT", _("TikTok")
    USER_GENERATED_CONTENT = "UGC", _("User Generated Content")


class Creator(TimeStampedModel):
    """
    Creator model that stores information about a creator.
    """

    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    platform = models.CharField(max_length=3, choices=Platform)

    def __str__(self):
        return self.name


class Content(TimeStampedModel):
    """
    Content model that stores information about a piece of content.
    """

    creator = models.ForeignKey(
        Creator,
        on_delete=models.CASCADE,
        related_name="content_set",
        related_query_name="content",
    )
    url = models.URLField()

    @property
    def is_video(self):
        """
        Return True if the content is a video, False otherwise.
        """
        return self.url.endswith(".mp4") or self.url.endswith(".mov")

    def __str__(self):
        return f"Created by {self.creator.name} at {self.created}"
