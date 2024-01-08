import json

from django.core.management.base import BaseCommand

from creators.models import Creator, Platform


class Command(BaseCommand):
    help = "Seed the database with creators."

    def handle(self, *args, **kwargs):
        platforms = {
            "Instagram": Platform.INSTAGRAM,
            "TikTok": Platform.TIKTOK,
            "User Generated Content": Platform.USER_GENERATED_CONTENT,
        }

        with open("creators-seed.json", "r") as file:
            data = json.load(file)

            for creator in data:
                new_creator, created = Creator.objects.get_or_create(
                    name=creator["name"],
                    username=creator["username"],
                    defaults={"rating": creator["rating"], "platform": platforms[creator["platform"]]},
                )

                new_creator.content_set.create(url=creator["content"])
        self.stdout.write("Database seed success.")
