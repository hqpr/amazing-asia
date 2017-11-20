from django.core.management.base import BaseCommand

from apps.offers.models import Offer
from apps.resort.models import Resort, Destination


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Destination.objects.create(name='Maldives')
        # Destination.objects.create(name='Mautirius')
        # Destination.objects.create(name='Seychelles')
        # Destination.objects.create(name='Indonesia')
        # Destination.objects.create(name='Thailand')
        # Destination.objects.create(name='Malaysia')
        # Destination.objects.create(name='Singapore')
        # Destination.objects.create(name='Sri Lanka')
        # Destination.objects.create(name='Dubai')
        # Destination.objects.create(name='Vietnam')

        for x in range(10):
            Offer.objects.create(name='Anantara Veli Resort & Spa Summer Escape',
                                 description='The rooms are very specially designed in the phonetic arrangement '
                                             '<br> Your friendship means a lot to me and I won’t say another word',
                                 expires_at='2018-01-18',
                                 stays_from='2018-09-15',
                                 stays_to='2018-12-15',
                                 is_active=True)

        destination = Destination.objects.filter(name='Maldives')[0]
        description = 'As the water flows down the bamboo, air passes through the tube and vibrates every fiber ' \
                      'of the instrument, skillfully blown through the shakuhachi by a figure sitting upon a wooden' \
                      ' chair, whose identity has no relevance to the situation; a situation that allows deep and' \
                      ' unexpected emotions to crawl from the dark corners within the innocently twisted minds' \
                      ' and hearts of the people who hear the lonely tune and purify them.'
        Resort.objects.create(destination=destination,
                              name='Adaaran Club Rannalhi',
                              description=description,
                              villa_view='SUNSET BEACH VIEW',
                              max_occupancy='3',
                              is_active=True)
        Resort.objects.create(destination=destination,
                              name='Amilla Fushi',
                              description=description,
                              villa_view='SUNSET BEACH VIEW',
                              max_occupancy='3',
                              is_active=True)
        Resort.objects.create(destination=destination,
                              name='Sheraton Full Moon Resort',
                              description=description,
                              villa_view='SUNSET BEACH VIEW',
                              max_occupancy='3',
                              is_active=True)
        Resort.objects.create(destination=destination,
                              name='BEACH BUNGALOW',
                              description=description,
                              villa_view='SUNSET BEACH VIEW',
                              max_occupancy='3',
                              is_active=True)
        Resort.objects.create(destination=destination,
                              name='WATER SUITE',
                              description=description,
                              villa_view='SUNSET BEACH VIEW',
                              max_occupancy='3',
                              is_active=True)