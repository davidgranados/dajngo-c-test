from rest_framework.generics import ListAPIView

from creators.models import Content
from creators.api.serializers import ContentSerializer


class ContentList(ListAPIView):
    """
    List view for the Content model.
    """

    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def get_queryset(self):
        """
        Prefetch the creator model.
        """
        return super().get_queryset().select_related("creator")

    def filter_queryset(self, queryset):
        """
        Filter the queryset based on the platform query parameter.
        """
        qs = super().filter_queryset(queryset)

        platform = self.request.query_params.get("platform")
        if platform:
            qs = qs.filter(creator__platform=platform)

        return qs
